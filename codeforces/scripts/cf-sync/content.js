// Runs on:
//   codeforces.com/contest/{id}/my         — post-submit redirect, live verdict table
//   codeforces.com/contest/{id}/submission/{submId} — individual submission view
//   codeforces.com/problemset/status*      — problemset submit redirect

// In-memory dedupe for this page session. Persistent dedupe lives in
// chrome.storage.local (background.js). This prevents duplicate messages when
// both the initial row scan and the MutationObserver fire for the same row.
const pushed = new Set();
console.log('[cf-sync] loaded on', location.href);

// ── helpers ──────────────────────────────────────────────────────────────────

// submId is always the last path segment regardless of URL format:
//   /contest/{id}/submission/{submId}      (contest pages)
//   /problemset/submission/{id}/{submId}   (problemset pages)
const subIdFromHref = (href) => {
  const last = href?.split('/').pop()?.split('?')[0];
  return last && /^\d+$/.test(last) ? last : null;
};

const readCode = (root) => {
  for (const sel of ['pre#program-source-text', 'pre.prettyprint', '.source pre']) {
    const el = root.querySelector(sel);
    const text = el && (el.innerText || el.textContent);
    if (text?.trim()) return text;
  }
  return null;
};

// credentials:'include' sends CF session cookies so the fetched page shows
// the actual source code (CF hides code on submission pages when logged out)
const fetchCFPage = async (url) => {
  const res = await fetch(url, { credentials: 'include' });
  if (!res.ok) return null;
  const html = await res.text();
  return new DOMParser().parseFromString(html, 'text/html');
};

const push = ({ contestId, index, name, lang, submId, code }) => {
  const key = `${contestId}-${index}`;
  if (pushed.has(key)) return;
  pushed.add(key);
  chrome.runtime.sendMessage(
    { action: 'push', contestId, index, name, lang, submId, code },
    // Remove from Set on failure so a page reload can retry
    (res) => { if (!res?.ok) pushed.delete(key); }
  );
};

// ── /contest/{id}/my  — submission list ──────────────────────────────────────

// On contest pages the contestId is in the URL; on /problemset/status we pull
// it from each row's problem link instead (e.g. /problemset/problem/53/D → 53)
const contestIdFromUrl = location.pathname.match(/\/contest\/(\d+)/)?.[1];

const processRow = async (row) => {
  if (!row.querySelector('.verdict-accepted, [class*="verdict-format-accepted"]')) return;

  // submission link is in the first column on both contest and problemset pages
  const submLink = row.querySelector('a[href*="/submission/"]');
  const submId   = subIdFromHref(submLink?.href);
  console.log('[cf-sync] submLink:', submLink?.href, '→ submId:', submId);
  if (!submId) return;

  const probLink  = row.querySelector('td a[href*="/problem/"]');
  // index is the last path segment in both /contest/{id}/problem/{index}
  // and /problemset/problem/{id}/{index}
  const index     = probLink?.href?.split('/').pop()?.split('?')[0] || null;
  const name      = probLink?.textContent?.trim();
  // extract contestId from problem href when not on a contest page
  const contestId = contestIdFromUrl || probLink?.href?.match(/\/(?:contest|problem)\/(\d+)\//)?.[1];
  console.log('[cf-sync] index:', index, 'name:', name, 'contestId:', contestId);
  if (!index || !name || !contestId) return;

  const langCell = row.querySelector('.source-code-cell, td:nth-child(5)');
  const lang     = langCell?.textContent?.trim() || 'C++';

  // The list view never shows the actual code — only the submission detail page
  // does. We fetch it here (same-origin, cookies auto-included). Fetch the URL
  // form the row itself links to: problemset submissions live at
  // /problemset/submission/{id}/{submId} and CF does not reliably serve their
  // source at the constructed /contest/... form, which made this exit silently.
  const doc  = await fetchCFPage(submLink.href);
  const code = doc && readCode(doc);
  if (!code) { console.log('[cf-sync] no code found at', submLink.href); return; }

  push({ contestId, index, name, lang, submId, code });
};

const isMyPage = /\/my(\?|$)/.test(location.pathname + location.search);
const isProblemsetStatus = location.pathname.startsWith('/problemset/status');

if (contestIdFromUrl && isMyPage || isProblemsetStatus) {
  // Sweep accepted rows top-down, one code fetch at a time with spacing so CF
  // never 503s. Rows already recorded in synced storage cost nothing (no
  // fetch), and the sweep ends after 3 consecutive already-synced rows — that
  // boundary means everything older was pushed long ago, so pre-extension
  // history is never bulk-imported by accident. A hard cap of 10 pushes per
  // page load bounds the worst case; refresh again to continue past it.
  const sweep = async () => {
    const { synced = {} } = await chrome.storage.local.get('synced');
    const rows = [...document.querySelectorAll('table tr')];
    console.log('[cf-sync] sweeping', rows.length, 'rows');
    let seenSynced = 0;
    let pushes = 0;
    for (const row of rows) {
      if (!row.querySelector('.verdict-accepted, [class*="verdict-format-accepted"]')) continue;
      const submId   = subIdFromHref(row.querySelector('a[href*="/submission/"]')?.href);
      const probLink = row.querySelector('td a[href*="/problem/"]');
      const index    = probLink?.href?.split('/').pop()?.split('?')[0];
      const cid      = contestIdFromUrl || probLink?.href?.match(/\/(?:contest|problem)\/(\d+)\//)?.[1];
      if (!submId || !index || !cid) continue;
      // CF submission ids increase monotonically: at-or-below the recorded id
      // means the same or an OLDER attempt, which must never overwrite newer code.
      const last = synced[`${cid}-${index}`];
      if (last && Number(submId) <= Number(last)) {
        if (++seenSynced >= 3) { console.log('[cf-sync] sweep done - reached synced history'); return; }
        continue;
      }
      seenSynced = 0;
      if (++pushes > 10) { console.log('[cf-sync] sweep cap reached - refresh the page to continue'); return; }
      await processRow(row);
      await new Promise((r) => setTimeout(r, 2000)); // spacing between code fetches
    }
    console.log('[cf-sync] sweep done - end of table');
  };
  sweep();

  new MutationObserver((mutations) => {
    for (const m of mutations) {
      if (m.type === 'childList') {
        for (const node of [...m.addedNodes]) {
          if (node.nodeType !== 1) continue;
          if (node.tagName === 'TR') {
            processRow(node);
          } else {
            // CF updates verdict by injecting a span inside an existing TR —
            // find the ancestor row and re-evaluate it
            const rows = [...node.querySelectorAll('tr')];
            if (rows.length) rows.forEach(processRow);
            else { const r = node.closest?.('tr'); if (r) processRow(r); }
          }
        }
      }
      if (m.type === 'characterData') {
        // m.target is a Text node — climb to its parent element then find the row
        const row = m.target.parentElement?.closest?.('tr');
        if (row) processRow(row);
      }
    }
  }).observe(document.body, { childList: true, subtree: true, characterData: true });
}

// ── /contest/{id}/submission/{submId}  — direct view ─────────────────────────

const submId = location.pathname.match(/\/submission\/(\d+)/)?.[1];

if (contestIdFromUrl && submId && !location.pathname.endsWith('/my')) {
  if (document.querySelector('.verdict-accepted, [class*="verdict-format-accepted"]')) {
    const code     = readCode(document);
    const lang     = document.querySelector('.lang, .source-code-cell')?.textContent?.trim() || 'C++';
    const probLink = document.querySelector('a[href*="/problem/"]');
    const index    = probLink?.href?.match(/\/problem\/([A-Z0-9]+)/i)?.[1];
    const name     = probLink?.textContent?.trim();

    if (code && index && name) push({ contestId: contestIdFromUrl, index, name, lang, submId, code });
  }
}
