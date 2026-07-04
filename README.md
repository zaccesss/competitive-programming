# competitive-programming

> **One repo. Three platforms.** Every Codeforces, LeetCode and NeetCode solution I write, synced automatically into a single long-term archive.

<p align="center">
  <a href="https://isaacadjei.me">
    <img src="https://img.shields.io/badge/Portfolio-isaacadjei.me-000000?style=for-the-badge&logo=googlechrome&logoColor=06ffa5" alt="Portfolio badge" />
  </a>
  <a href="https://www.linkedin.com/in/isaacadjei">
    <img src="https://img.shields.io/badge/LinkedIn-Isaac_Adjei-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn badge" />
  </a>
  <a href="mailto:code@isaacadjei.me">
    <img src="https://img.shields.io/badge/Email-Contact-ff6f61?style=for-the-badge&logo=gmail&logoColor=white" alt="Email badge" />
  </a>
</p>

<p align="center">
  <a href="https://codeforces.com/profile/zaccesss">
    <img src="https://img.shields.io/badge/Codeforces-zaccesss-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white" alt="Codeforces badge" />
  </a>
  <a href="https://leetcode.com/u/zacadjei">
    <img src="https://img.shields.io/badge/LeetCode-zacadjei-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="LeetCode badge" />
  </a>
  <a href="https://neetcode.io/profile/zaccess">
    <img src="https://img.shields.io/badge/NeetCode-zaccess-00C7B7?style=for-the-badge&logo=googlechrome&logoColor=white" alt="NeetCode badge" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/zaccesss/competitive-programming/actions/workflows/sync.yml">
    <img src="https://github.com/zaccesss/competitive-programming/actions/workflows/sync.yml/badge.svg" alt="Sync workflow status" />
  </a>
</p>

---

## About

This repository is the single place to browse all of my competitive programming work. I never commit solutions here directly. Instead, each platform has its own private source repo that the platform tooling writes to, and a sync workflow clones them with a read-only token and copies every source into its platform folder here. This archive is the public face of the whole collection.

That split is deliberate. LeetHub and the NeetCode GitHub Sync each expect to own a whole repository, so they keep their own. This repo adds the part they cannot do: one archive, one structure, one place to send people.

**Anything inside `codeforces/`, `leetcode/` or `neetcode/` is a synced snapshot.** Solutions change on the platforms (or in the source repos) and flow here automatically - direct edits to those folders would be overwritten by the next sync. The root of this repo (this README, LICENSE, SECURITY.md, the workflow) is owned here and never touched by the sync.

---

## Platforms

| Platform   | Profile                                                                     | Folder        | Source repo (private)     | How solutions land                                     |
| ---------- | --------------------------------------------------------------------------- | ------------- | ------------------------- | ------------------------------------------------------ |
| Codeforces | [codeforces.com/profile/zaccesss](https://codeforces.com/profile/zaccesss) | `codeforces/` | `codeforces-submissions`  | pushed by my own scripts after each session            |
| LeetCode   | [leetcode.com/u/zacadjei](https://leetcode.com/u/zacadjei)                 | `leetcode/`   | `leetcode-submissions`    | pushed by LeetHub the moment a submission is accepted  |
| NeetCode   | [neetcode.io/profile/zaccess](https://neetcode.io/profile/zaccess)         | `neetcode/`   | `neetcode-submissions`    | pushed by the official NeetCode GitHub Sync            |

Each platform folder keeps the exact structure its tooling produces, and each contains its own README describing that layout in detail.

---

## How the sync works

One workflow, [`sync.yml`](.github/workflows/sync.yml), with three triggers - the same instant-plus-safety-net pattern as my mirror system:

| Trigger                        | When                                                                    | Purpose                                        |
| ------------------------------ | ----------------------------------------------------------------------- | ---------------------------------------------- |
| `repository_dispatch` (`sync`) | Instantly, fired by my mirror-ops Worker when a source repo is pushed   | A solution appears here within a minute        |
| `schedule`                     | Hourly                                                                   | Safety net that heals anything the instant path missed |
| `workflow_dispatch`            | Manually                                                                 | The first run or a forced resync               |

Each run shallow-clones the three private source repos with a read-only fine-grained token, copies each working tree over its platform folder (deletions included) and commits only if something actually changed, with a message naming the sources that moved:

```text
sync: leetcode @ 0ab979a
sync: codeforces @ ad7e501, neetcode @ 6f08a5a
```

The sources' `.github/` and `LICENSE` files stay behind, so this repo carries exactly one licence and no inherited workflows.

---

## Structure

```text
competitive-programming/
├── codeforces/                          ← codeforces-submissions
│   ├── contests/
│   │   └── round-994-div4/A-solution.cpp
│   ├── practice/
│   │   └── 800/watermelon.cpp
│   └── README.md
├── leetcode/                            ← leetcode-submissions
│   ├── 0001-two-sum/
│   │   ├── solution.py
│   │   └── README.md                    (problem statement, generated by LeetHub)
│   └── README.md
├── neetcode/                            ← neetcode-submissions
│   ├── Data Structures & Algorithms/
│   │   └── two-integer-sum/submission-0.py
│   └── README.md
├── CHANGELOG.md · CODE_OF_CONDUCT.md · LICENSE · SECURITY.md
└── README.md                            ← owned here, never touched by the sync
```

### `codeforces/`

Contest practice and rating climbs. Organised by contest round or practice rating, one file per problem. Commit messages in the source repo follow `[Codeforces] Practice 800 - Nearly Lucky Number - C++`.

### `leetcode/`

Interview-style practice following the NeetCode 250 roadmap. One folder per problem (`0001-two-sum/`), each with the solution and a LeetHub-generated problem statement.

### `neetcode/`

Roadmap-based preparation. Organised by course topic, then problem, with every attempt stored as `submission-0`, `submission-1` and so on.

---

## Languages

| Icon | Language | Extension | Where it shows up |
|:---:|---|---|---|
| <img src="https://techstack-generator.vercel.app/python-icon.svg" width="28" alt="Python icon" /> | Python | `.py` | Primary language on LeetCode and NeetCode |
| <img src="https://techstack-generator.vercel.app/cpp-icon.svg" width="28" alt="C++ icon" /> | C++ | `.cpp` | Primary language on Codeforces |
| <img src="https://techstack-generator.vercel.app/java-icon.svg" width="28" alt="Java icon" /> | Java | `.java` | Interview crossover problems |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg" width="28" alt="Kotlin icon" /> | Kotlin | `.kt` | Modern JVM rounds |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" width="28" alt="C icon" /> | C | `.c` | Low-level practice |
| <img src="https://techstack-generator.vercel.app/csharp-icon.svg" width="28" alt="C sharp icon" /> | C# | `.cs` | Enterprise interview rounds |
| <img src="https://techstack-generator.vercel.app/js-icon.svg" width="28" alt="JavaScript icon" /> | JavaScript | `.js` | Frontend and full-stack rounds |
| <img src="https://techstack-generator.vercel.app/ts-icon.svg" width="28" alt="TypeScript icon" /> | TypeScript | `.ts` | Typed full-stack rounds |

New languages appear here automatically the moment a solution in one lands in a source repo - there is nothing to configure.

---

## Goals

- build a long-term archive of solved problems across all three platforms
- at least one problem solved every single day
- improve algorithmic thinking through repetition and pattern recognition
- keep the whole record in one browsable, shareable place without changing how any platform pushes

---

## Contact and Support

Open an [issue](https://github.com/zaccesss/competitive-programming/issues) in this repository for questions or bugs.

You can also reach me directly at [code@isaacadjei.me](mailto:code@isaacadjei.me) or via my [website contact page](https://isaacadjei.me/contact).

---

<div align="center">

<br />

Made with 💻 by [Isaac Adjei](https://isaacadjei.me)

<br />

[![isaacadjei.me](https://img.shields.io/badge/isaacadjei.me-000000?style=for-the-badge)](https://isaacadjei.me)
[![zacess.com](https://img.shields.io/badge/zacess.com-000000?style=for-the-badge)](https://zacess.com)

<br />

</div>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=110&section=footer" alt="Footer banner" />
</p>
