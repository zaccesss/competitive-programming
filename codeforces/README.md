# Codeforces Solutions

> **@zaccesss** · Solutions pushed manually after each contest or practice session

[![Markdown Lint](https://github.com/zaccesss/codeforces-submissions/actions/workflows/markdownlint.yml/badge.svg)](https://github.com/zaccesss/codeforces-submissions/actions/workflows/markdownlint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## About

This repository is a long-term archive of my Codeforces solutions. Solutions are pushed here manually after each contest or practice session. I started at Div. 4 and Div. 3 contests, working through 800-rated problems first before progressing to 900 and 1000 as my rating improves.

The goal is consistent practice and steady rating growth alongside my LeetCode and NeetCode work, building genuine competitive programming skills from scratch.

---

## Structure

Solutions are organised by contest or rating, then by problem letter.

```
contests/
  round-994-div4/
    A-solution.cpp
    B-solution.cpp

practice/
  800/
    watermelon.cpp
  900/
    nearly-lucky-number.cpp
```

Commit messages follow the format:

```
[Codeforces] Round 994 Div4 - A. Watermelon - C++
[Codeforces] Practice 800 - Nearly Lucky Number - C++
```

---

## Local Builds

Compiled executables are kept out of Git and should be built into `bin/`.

To build a C++ solution:

```powershell
.\scripts\build.ps1 practice/800/4A-watermelon.cpp
```

To build and run it:

```powershell
.\scripts\build.ps1 practice/800/4A-watermelon.cpp -Run
```

The output keeps the same folder structure under `bin/`, for example:

```text
bin/practice/800/4A-watermelon.exe
```

VS Code users can also run the default build task with `Ctrl+Shift+B`.

---

## Languages

| Icon | Language | Extension | Notes |
|:---:|---|---|---|
| <img src="https://techstack-generator.vercel.app/cpp-icon.svg" width="28"/> | C++ | `.cpp` | Primary language for competitive programming |
| <img src="https://techstack-generator.vercel.app/python-icon.svg" width="28"/> | Python | `.py` | Occasionally used for simpler problems |
| <img src="https://techstack-generator.vercel.app/java-icon.svg" width="28"/> | Java | `.java` | Used when practising interview crossover problems |

---

## Approach

1. Start with Div. 4 and Div. 3 contests to build contest rhythm.
2. Begin with 800-rated problems then move to 900 and 1000.
3. Always attempt problems in contest mode first before looking anything up.
4. After each contest, review problems that were not solved and understand the solution.
5. Push solutions here with clear commit messages after each session.

---

## Platforms

| Platform | Username | Profile |
|---|---|---|
| Codeforces | `zaccesss` | [codeforces.com/profile/zaccesss](https://codeforces.com/profile/zaccesss) |
| LeetCode | `zacadjei` | [leetcode.com/u/zacadjei](https://leetcode.com/u/zacadjei) |
| NeetCode | `zaccess` | [neetcode.io/profile/zaccess](https://neetcode.io/profile/zaccess) |

---

## Contact and Support

Open an [issue](https://github.com/zaccesss/codeforces-submissions/issues) in this repository for questions or bugs. See [SUPPORT.md](SUPPORT.md) for the full breakdown of where to go.

> [!TIP]
> Reach me directly at [code@isaacadjei.me](mailto:code@isaacadjei.me) or through the [website contact page](https://isaacadjei.me/contact).

> [!IMPORTANT]
> For a security issue, follow [SECURITY.md](SECURITY.md) rather than posting publicly.

---

Made by [Isaac Adjei](https://isaacadjei.me).
