# Contributing to CRUCIBLE

Thank you for your interest in contributing to CRUCIBLE. This framework exists to eliminate sycophancy and analytical blindness from AI-assisted research — and that mission applies to its own codebase as well. We welcome rigorous contributions, unflinching critique, and methodological challenges.

Before contributing, please read this guide in full.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Getting Started](#getting-started)
4. [Development Workflow](#development-workflow)
5. [Commit Message Format](#commit-message-format)
6. [CRUCIBLE Linter Requirement](#crucible-linter-requirement)
7. [Style Guidelines](#style-guidelines)
8. [Submitting a Methodology Critique](#submitting-a-methodology-critique)
9. [Reporting Bugs](#reporting-bugs)
10. [Requesting Features](#requesting-features)
11. [Review Process](#review-process)

---

## Code of Conduct

This project enforces a standard of intellectual honesty. In practice:
- **Be rigorous, not hostile.** Critique ideas and methodology, not people.
- **Be concrete.** "This doesn't work" is not a contribution; "Layer 4 fails to detect Simpson's Paradox in [specific case] because [reason]" is.
- **No sycophancy.** Do not submit pull requests or issues designed to agree with the maintainers. If you find a flaw, report the flaw.

---

## How to Contribute

There are several ways to contribute:

| Contribution Type | Description |
|---|---|
| **Methodology Critique** | Challenge CRUCIBLE's 10-layer normative architecture with evidence |
| **Bug Reports** | Report linter failures, regex mismatches, or documentation errors |
| **New Showcase Reports** | Submit CRUCIBLE-audited monographies on new academic texts |
| **Benchmark Expansion** | Add new target dossiers and validated analyses to `benchmarks/` |
| **Linter Improvements** | Extend `scripts/crucible_linter.py` with new validation rules |
| **Documentation** | Improve clarity, fix typos, add translations |
| **CI/CD** | Expand GitHub Actions workflows |

---

## Getting Started

### Prerequisites

- **Python 3.10+** — Required for the deterministic linter.
- **Git** — For version control.
- **`markdown` Python package** — Install via `pip install markdown`.

### Setup

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/<your-username>/crucible.git
cd crucible

# 3. Add upstream remote
git remote add upstream https://github.com/efegok73/crucible.git

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify the linter works
python scripts/crucible_linter.py showcase/en/01_Judith_Butler_Report.md
```

---

## Development Workflow

We use a **Fork & Pull Request** model:

1. **Sync with upstream** before starting work:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```

3. **Make your changes.** Keep commits atomic and focused.

4. **Run the CRUCIBLE linter** on any modified or new report files (see [below](#crucible-linter-requirement)).

5. **Push to your fork** and open a Pull Request against `upstream/main`.

---

## Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>

[optional body]

[optional footer(s)]
```

### Types

| Type | When to Use |
|---|---|
| `feat` | New feature, new showcase report, new benchmark |
| `fix` | Bug fix in linter, regex correction, broken link |
| `docs` | Documentation only (README, methodology docs, translations) |
| `refactor` | Code restructuring with no behavior change |
| `test` | Adding or updating tests |
| `ci` | Changes to CI/CD configuration |
| `chore` | Maintenance tasks (dependency updates, file reorganization) |

### Examples

```
feat(benchmark): add target dossier for Popper's falsificationism
fix(linter): correct Layer 8 source criticism regex for Turkish reports
docs(readme): clarify two-stage extraction workflow
```

---

## CRUCIBLE Linter Requirement

**Every Markdown report** (showcase monographies, benchmark analyses, new contributions under `showcase/` or `benchmarks/`) **must pass the deterministic linter before a PR can be merged.**

```bash
python scripts/crucible_linter.py <path-to-your-report.md>
```

The linter validates:
- **Core Section Integrity** — All required sections (Epistemic Triage, Steelmanning, Auto-Falsification, Damage Report, Surgeon Checklist) are present.
- **Dynamic Triage Verification** — If Layer 8 is declared active, the Claim-Source Audit Matrix table must exist.
- **Rhetorical Hygiene** — Forbidden sycophantic and dogmatic terms are flagged.
- **Structural Compliance** — Section headers, table formatting, and report architecture.

The CI pipeline (`ci.yml`) runs this automatically on every push and pull request. **If the linter returns `[FAIL]`, the PR will not be merged.**

---

## Style Guidelines

### Python (`scripts/`)

- Follow **PEP 8**.
- Use **type hints** for function signatures.
- All scripts must run on Python 3.10+ without external dependencies beyond `requirements.txt`.
- Include docstrings for public functions.

### Markdown (Reports, Documentation)

- Use **ATX-style headers** (`#`, `##`, `###`).
- Tables must use proper Markdown pipe syntax with alignment.
- Do not use HTML inside Markdown files unless absolutely necessary.
- Reports must follow the CRUCIBLE output template structure:
  1. `[EPISTEMIC TRIAGE]` — Layer activation and justification.
  2. `[ANALYSIS, STEELMAN & SOURCE CRITICISM]` — Core audit body.
  3. `[AUTO-FALSIFICATION, DAMAGE REPORT & SURGEON CARD]` — Self-audit and external checklist.

### File Naming

- Showcase reports: `XX_Author_Name_Report.md` (and `.html`).
- Benchmark dossiers: `XX_Author_Name_Dossier.md`.
- Use underscores, not spaces. Use ASCII characters in filenames.

---

## Submitting a Methodology Critique

CRUCIBLE is an epistemic auditing framework — it must be able to withstand its own audit. **We explicitly invite methodological challenges.**

To submit a critique:

1. **Open a GitHub Issue** using the "Methodology Critique" template.
2. Specify:
   - **Which layer(s)** of the 10-layer normative gauntlet you are challenging (L1–L10).
   - **The specific failure mode** you identified (e.g., "Layer 5 cannot detect collider bias in [this case]").
   - **Evidence** — A concrete example, preferably with a target dossier and CRUCIBLE output demonstrating the failure.
3. If your critique is validated, it will be:
   - Documented in `CHANGELOG.md`.
   - Addressed with a patch or acknowledged in `docs/LIMITATIONS.md`.
   - Credited in the changelog entry.

**Critiques that improve CRUCIBLE's analytical integrity are the most valuable contributions possible.**

---

## Reporting Bugs

Use the "Bug Report" issue template. Include:
- **Environment:** OS, Python version, model used (if applicable).
- **Steps to reproduce** the issue.
- **Expected behavior** vs. **actual behavior**.
- **Linter output** if relevant (copy the full terminal output).

---

## Requesting Features

Use the "Feature Request" issue template. Include:
- **Problem statement:** What gap or limitation does this address?
- **Proposed solution:** How should it work?
- **Alternatives considered:** What other approaches did you evaluate?

---

## Review Process

1. All PRs require **at least 1 maintainer review**.
2. The CI pipeline must pass (linter `[PASS]` on all affected reports).
3. Methodology-related PRs (changes to `docs/`, `templates/`, or `scripts/crucible_linter.py`) receive heightened scrutiny and may require discussion in a linked Issue first.
4. Cosmetic or typo-fix PRs are fast-tracked.
5. **No PR is merged if it introduces sycophantic language, removes self-critique sections, or weakens the analytical gauntlet.** This is a hard rule.

---

## License

By contributing to CRUCIBLE, you agree that your contributions will be licensed under the [MIT License](LICENSE).
