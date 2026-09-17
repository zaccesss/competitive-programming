# Workflows

| Workflow | Runs on | What it does |
| --- | --- | --- |
| [`sync.yml`](sync.yml) | `repository_dispatch`, hourly schedule, manual | Pulls the three source repos and reconciles their platform folders here |
| [`gitleaks-scan.yml`](gitleaks-scan.yml) | Push to `main`, every pull request | Scans for accidentally committed secrets |
| [`markdownlint.yml`](markdownlint.yml) | Push to `main`, every pull request | Lints the root markdown files and `.github/` against [`.markdownlint.json`](../../.markdownlint.json) |

`markdownlint.yml` only checks the root docs and `.github/`, not the synced `codeforces/`, `leetcode/` and `neetcode/` folders, since those are overwritten by the next sync regardless. `markdownlint.yml` is also runnable manually via `workflow_dispatch` from the Actions tab.
