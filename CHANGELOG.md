# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [v1.1.2] - 2026-07-08

### Fixed

- The sync workflow no longer fails when a source repo is pushed several times in quick succession. Platform tooling can fan one action out into a burst of pushes - LeetHub commits the solution, its README, the topic tags and the stats separately - so a single accepted submission fired several `repository_dispatch` events within seconds, and the overlapping runs raced to push, leaving the losers rejected as non-fast-forward. The concurrency group now cancels an in-flight run when a new one starts (`cancel-in-progress: true`), so a burst collapses into one sync, and the push step re-fetches, rebases and retries if two runs still race, so a run is never left failing on a non-fast-forward push

---

## [v1.1.1] - 2026-07-04

### Changed

- `neetcode-submissions` is public again. NeetCode's GitHub integration cannot see private repositories - it reported the repo as not found and then tried to recreate it - so the private flip broke its sync. codeforces-submissions and leetcode-submissions stay private since LeetHub and my own tooling handle private repos fine

---

## [v1.1.0] - 2026-07-04

### Changed

- The three source repos are now private. The sync clones them with a read-only fine-grained token (the SOURCES_TOKEN secret), so this archive is the public face of the whole collection
- Sync commits are authored with my GitHub noreply address, so no file in this repo carries an address code search can harvest
- README and SECURITY.md no longer link to the source repos, which are not visible to visitors anymore

### Removed

- The mirror workflows in the three source repos, ahead of the central mirror-ops system taking over all mirroring

---

## [v1.0.0] - 2026-07-03

### Changed

- Converted the repository from a hand-maintained scaffold into an auto-synced archive. My three submission repos stay the write targets (LeetHub for LeetCode, the official NeetCode GitHub Sync for NeetCode, my own scripts for Codeforces) and a sync workflow copies each one into its platform folder here - hourly on a schedule, instantly via `repository_dispatch` once my mirror-ops Worker starts fanning out source pushes and manually on demand
- Rewrote the README around the synced layout: each platform folder now keeps its source repo's native structure instead of the old language/difficulty scaffold

### Added

- `.github/workflows/sync.yml` - the three-trigger sync engine
- `SECURITY.md` and `CODE_OF_CONDUCT.md` following the same format as my other repositories
- This changelog

### Removed

- The empty `platform/language/difficulty` scaffold directories - the synced content defines the structure now
