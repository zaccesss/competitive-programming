# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
