# ⚖️ CRUCIBLE — Epistemic Auditing Framework for AI-Assisted Research

**Force AI to critique research like a senior scientific referee, not a diplomat.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-6.0-emerald.svg)](CHANGELOG.md)
[![Whitepaper](https://img.shields.io/badge/Whitepaper-Technical_Report-blueviolet.svg)](docs/CRUCIBLE_v6_Whitepaper.md)
[![Benchmarks](https://img.shields.io/badge/Benchmarks-9_Cases_Validated-success.svg)](docs/BENCHMARKS.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-informational.svg)](https://www.python.org/)

> *Originally conceived as* ***Mayın Tarlası*** *(Epistemic Minefield Model) — the testing ground where unstated axioms are either detonated or survive.*

---

## What Is CRUCIBLE?

CRUCIBLE is an **open-source prompt framework** that transforms commercial AI models (ChatGPT, Claude, Gemini) into rigorous, adversarial scientific auditors.

When you ask a standard AI to "review this paper," it produces polite, non-committal summaries that agree with the author and avoid confrontation. This is a well-documented failure mode called **sycophancy** — and it makes AI useless for serious research evaluation.

CRUCIBLE solves this by injecting a structured analytical constitution into the AI at inference time. No fine-tuning. No API keys. No model retraining. The same AI model, constrained by CRUCIBLE's 10-layer normative protocol, produces forensic-grade analysis instead of diplomatic handwaving.

**Who is this for?**
- Researchers who want a brutally honest second opinion on a paper, thesis, or book — including their own work.
- Students preparing thesis defenses who want to discover their weak points before their committee does.
- Science journalists and policy analysts who need to distinguish robust evidence from rhetorical confidence.
- Anyone who is tired of AI telling them what they want to hear.

### 🏛️ The Four Epistemic Pillars

CRUCIBLE is not a polite summarizer; it is an inference-time forensic harness operating on four non-negotiable principles of scientific inquiry:

1. **Enforcement of Frontier Methodological Standards:**  
   Audits claims against formal scientific demarcation (Popperian falsifiability, Bradford Hill causal criteria, GRADE evidentiary hierarchies) rather than consensus rhetoric.
2. **Forensic Evidence & Denominator Surgery:**  
   Dissects the empirical foundation of the thesis—hunting denominator inflation, sample attrition, and unsubstantiated leaps from proxy data to ontological reality.
3. **Detection of Semantic Equivocation & Unstated Axioms:**  
   Exposes motte-and-bailey defenses, circular definitions, and dogma masquerading as settled methodology behind academic prose.
4. **Radical Auto-Falsification (The Gödel-Tarski Boundary):**  
   Acknowledging that no AI can formally validate its own meta-language, it subjects its own critique to adversarial self-examination, explicitly cataloging its own blind spots, disciplinary biases, and single-source risks before handing the verdict to a human researcher.

---

## The Problem — and What CRUCIBLE Does About It

### What a normal AI produces when asked to "analyze this book":

> *"Butler's Gender Trouble is a groundbreaking and thought-provoking work that has profoundly influenced feminist theory. While some scholars have raised methodological questions, the text presents a compelling and nuanced argument for the performative nature of gender..."*

This tells you **nothing**. It's a book-jacket blurb, not an analysis.

### What CRUCIBLE produces from the same source material:

> **[Layer 3 — Hermeneutic Audit]:** The term "performativity" is deployed with three semantically distinct definitions across Chapters 1–3 — (a) involuntary citation of norms under duress, (b) Nietzschean metalepsis of cause/effect, (c) Austinian speech-act derivation — without explicit disambiguation. This creates a motte-and-bailey structure: when the strong ontological claim is challenged, the author retreats to the weaker epistemological reading.
>
> **[Layer 8 — Source Criticism Matrix]:**
>
> | Claim | Primary Source | Source Type | Verdict |
> |:---|:---|:---|:---|
> | Biological sex is discursively constructed | Foucault, *History of Sexuality* Vol. 1 | Post-structuralist discourse analysis | **Proxy Leap:** Unsubstantiated jump from "language mediates our description of anatomy" to "anatomy itself is a cultural artifact" |
>
> **[Layer 10 — Auto-Falsification]:** This audit's own analysis relies heavily on Anglo-American analytic philosophy of science as its evaluative benchmark, which may systematically underweight the Continental tradition's distinct epistemological commitments...

*— Condensed from [Case 01: Judith Butler – Gender Trouble](showcase/en/01_Judith_Butler_Report.html) (Full report: 25 KB, 192 lines, 5 active layers, 8 fallacies detected)*

---

## Quick Start: Step-by-Step Guide

### ⚡ 10-Second Preview (Inspect a Real Report)
Want to see what CRUCIBLE actually produces without installing anything?  
👉 [**Open the Judith Butler – Gender Trouble Sealed Report (HTML)**](showcase/en/01_Judith_Butler_Report.html) or browse all [9 Verified Benchmark Cases](#9-verified-benchmark-cases).

---

### 0. Prerequisites: Download the Repository (For All Users)
1. On the GitHub page under the **Code** tab, click the green **`<> Code`** button on the top-right and select **`Download ZIP`**.
2. Right-click the downloaded `.zip` archive and select **"Extract All"**. All directives, templates, and validation scripts are now available on your local drive.  
*(Developer alternative: `git clone https://github.com/efegok73/crucible.git`)*

---

### 💻 Option A (Recommended): Autonomous Auditing with Agentic IDE
*(For Antigravity, Cursor, VS Code + Roo/Cline, or Claude Code users)*

In this mode, you never manually copy-paste prompts; your AI agent adopts the workspace constitutions (`.cursorrules`, `AGENTS.md`) and executes the entire pipeline autonomously.

1. **Open the Workspace with Trust:**  
   Open your IDE, select `File > Open Folder`, and choose the extracted `crucible-main` directory. When prompted, select **"Trust Authors"** *(mandatory; otherwise background linter execution and agent tools are restricted)*.
2. **Create Your Workspace Directory:**  
   To keep repository constitutions pristine, create your own working subfolder in the file explorer (e.g., `cases/`).
3. **Import Your Dossier:**  
   Drag and drop the work to be audited (PDF, Word, or Markdown) into your new subfolder.
4. **Issue the Command Based on Document Scale:**
   - **Short Works (< 20 Pages / < 10,000 Words — Standalone Paper or Essay):**  
     Issue a direct instruction in your agent panel:  
     > *"Analyze `@cases/paper.pdf` using CRUCIBLE v6.0 protocol and seal the report."*
   - **Long Works (> 20 Pages — Book, Doctoral Thesis, Monograph):**  
     Instruct your agent to execute the mandatory two-stage pipeline:
     - **Stage 1:** *"Apply `templates/CRUCIBLE_EXTRACTION_DIRECTIVE.md` to this book and output a Target Dossier (`target_dossier.md`)."*
     - **Stage 2:** *"Now audit `target_dossier.md` using the CRUCIBLE constitution and seal the report."*
5. **Receive Your Sealed Output:**  
   The agent completes the audit, saves the report to disk, runs `crucible_linter.py` in the background, achieves `[PASS]`, and compiles a publication-ready `.html` report. Double-click the HTML file to inspect the monograph in your browser.

---

### 🌐 Option B: Direct Auditing via Web Interfaces
*(For Claude.ai, ChatGPT Plus, Google AI Studio web interfaces — Zero Installation)*

1. **Initiate the Audit Based on Document Scale:**
   - **Short Works (< 20 Pages / < 10,000 Words):**  
     Open [`templates/CRUCIBLE_WEB_PROMPT_EN.md`](templates/CRUCIBLE_WEB_PROMPT_EN.md) in any text editor, copy its contents, paste them into your web AI chat, attach your document, and submit.
   - **Long Works (> 20 Pages — Book, Doctoral Thesis):**  
     - **Stage 1 (Target Dossier Extraction):** Copy [`templates/CRUCIBLE_EXTRACTION_DIRECTIVE.md`](templates/CRUCIBLE_EXTRACTION_DIRECTIVE.md), paste it into your chat along with the book. The model outputs a verbatim `Target Dossier`.
     - **Open a Fresh Chat (Mandatory):** Copy the extracted Target Dossier text. **Open a new, clean chat session** *(mandatory to eliminate context contamination and prevent smoothing degradation)*.
     - **Stage 2 (Forensic Audit):** Paste [`templates/CRUCIBLE_WEB_PROMPT_EN.md`](templates/CRUCIBLE_WEB_PROMPT_EN.md) along with your extracted Target Dossier and execute the audit.
2. **Save Your Report:**  
   Copy the generated analytical output, paste it into a text editor, and save it locally as `cases/report.md`.
3. **Mandatory Linter Verification & Sealing (Deterministic Audit):**  
   Under the CRUCIBLE protocol, the linter is **not an optional suggestion; it is the external constitutional court.** An AI's self-affirmation ("I followed all rules") is strictly unverified. All 5 mandatory sections, the Layer 8 Claim-Source Matrix, and rhetorical hygiene must be verified programmatically:  
   ```bash
   pip install markdown
   python scripts/crucible_linter.py cases/report.md
   ```  
   The linter inspects the report line by line. If all constitutional criteria are met, it stamps **`[PASS]`** and automatically compiles the publication-ready `report.html` monograph. *(Reports that fail or skip linter verification remain uncertified drafts).*

---

### 📌 Core Epistemic Note: Parity Between Option A & Option B
> When executed strictly according to instructions, **Option A and Option B are 100% identical in epistemic depth, philosophical rigor, and analytical caliber.** Both pathways execute the exact same normative layers and must pass the exact same deterministic linter.  
> 
> The sole distinction lies in workflow automation: **In Option A**, the two-stage pipeline, cross-window text transfer, file persistence, and background linter verification are orchestrated autonomously by your AI agent (Antigravity, Cursor, VS Code). **In Option B**, you manage these window transitions and terminal commands manually.

---

## 🧠 Model Competence Threshold (Architectural Requirements)

CRUCIBLE is strictly model-agnostic and does not depend on any specific proprietary provider or transient model version. However, enforcing a 10-layer normative gauntlet, hermeneutic hygiene, and tabular source-criticism requires an underlying engine that satisfies **four structural competence criteria**:

1. **Anti-Smoothing Architecture:** High resistance to conversational politeness and diplomatic compression; capable of unyielding methodological friction rather than superficial summaries.
2. **Strict Tabular and Matrix Discipline:** Absolute fidelity in generating structured output, specifically the mandatory Layer 8 Claim-Source Matrix and Surgeon Cards, without syntactic deformation.
3. **Multi-Constraint Instruction Adherence:** Premier reasoning capacity capable of navigating complex epistemic triage without instruction decay or context degradation over long horizons.
4. **Substantial Context Capacity:** Sufficient context bandwidth to ingest primary source dossiers, extraction directives, and analytical constitutions simultaneously.

> ⚠️ **Lightweight Models Warning:** Distilled, lightweight, or conversational mini-models suffer rapid instruction decay under multi-layered normative constraints, invariably collapsing into journalistic summarization (*smoothing errors*).

---

## ⚠️ Three Rules You Must Follow

1. **Always use two stages.** Feeding a 400-page book directly into an AI with a single "analyze this" prompt triggers *smoothing error* — the AI compresses your audit into an 18 KB journalistic summary. Separate extraction from analysis.

2. **Match the language to the source.** If your source material is in English, run the audit in English. Forcing analysis of English scientific literature into a morphologically complex language (e.g., Turkish, Hungarian) costs ~50% of analytical depth due to tokenization overhead. Translate the sealed report afterward if needed. ([Evidence](docs/en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md))

3. **Cross-validate across models.** AI providers silently update model weights. A model that executes all 10 layers flawlessly today may degrade next week. Run critical audits on at least 2 different frontier models.

---

## How It Works: The 10-Layer Normative Gauntlet

CRUCIBLE does not activate all 10 layers on every text. A dynamic **Epistemic Triage Matrix** selects relevant layers based on the discipline of the source material:

| Layer | Function | Example Activation |
|:---:|:---|:---|
| **L1** | **Epistemic Virtue & Demarcation** — Eliminates emotional rhetoric, enforces intellectual humility | Always active |
| **L2** | **Steelmanning** — Rebuilds the thesis in its strongest possible academic form before any critique | Always active |
| **L3** | **Hermeneutics & Lexical Hygiene** — Detects semantic shifts, double meanings, concept creep | Philosophy, social science |
| **L4** | **Statistics & Bayesian Audit** — Audits sample sizes, effect sizes, p-hacking, prior distributions | Empirical sciences, medicine |
| **L5** | **Experimental Design & Causality** — Tests for confounders, reverse causation, collider bias via DAGs | Clinical trials, epidemiology |
| **L6** | **Evidence Hierarchies** — Applies AMSTAR-2, GRADE protocols; filters single-case anecdotes | Systematic reviews, meta-analyses |
| **L7** | **Decision Science & Risk (DMDU)** — Evaluates risk tradeoffs, fat-tail exposures, antifragility | Policy analysis, climate science |
| **L8** | **Historical Source Criticism** — Enforces primary source triangulation; requires Claim-Source Matrix | Historiography, archival research |
| **L9** | **Computational Model Audit** — Checks for overfitting, validation leakage, parameter tuning | Simulations, ML, agent-based models |
| **L10** | **Auto-Falsification & Surgeon Card** — AI confesses its own blind spots; provides 3-minute human verification checklist | Always active |

After analysis, the output is validated by a **deterministic Python linter** ([`crucible_linter.py`](scripts/crucible_linter.py)) that checks structural completeness, triage integrity, and rhetorical hygiene. Reports that fail are rejected and cannot be sealed.

---

## Showcase: 9 Validated Benchmark Cases

Every report below passed the deterministic linter and is available in both English and Turkish:

| # | Discipline | Audited Work | Key Vulnerability Found | Verdict |
|:---:|:---|:---|:---|:---:|
| 01 | Philosophy & Gender | **Judith Butler** — *Gender Trouble* (1990) | Semantic equivocation on "performativity"; proxy leap from epistemology to ontology | Major Revision |
| 02 | Psychoanalysis | **Jacques Lacan** — *Seminaire XX* (1975) | Pseudo-mathematical topology (mathemes) without formal validation | Major Revision |
| 03 | Clinical Epidemiology | **Hilary Cass** — *The Cass Review* (NHS, 2024) | Excessive RCT threshold applied to observational pediatric cohort data | Minor Revision |
| 04 | Historiography | **Cheikh Anta Diop** — *The African Origin* (1974) | Anachronistic racial categories; false linguistic cognates | Rejected |
| 05 | Classical Philology | **Frank M. Snowden Jr.** — *Blacks in Antiquity* (1970) | Minimization of Greco-Roman physiognomic prejudice | Minor Revision |
| 06 | Bibliometrics | **Cook et al. vs. Tol** — *97% Climate Consensus* (2013) | Denominator manipulation (66.4% neutral abstracts excluded) | Major Revision |
| 07 | Climate Science | **Judith Curry** — *Climate Uncertainty* (2023) | Internal ocean oscillation claims vs. observed net energy imbalance | Major Revision |
| 08 | Psychiatry & EBM | **Joanna Moncrieff et al.** — *Serotonin Theory* (2022) | Aspirin Fallacy: conflating etiological irrelevance with clinical inefficacy | Major Revision |
| 09 | Evolutionary Psychology | **Simon Baron-Cohen** — *The Essential Difference* (2003) | Failed neonate replication (Connellan 2000); 80% sex overlap ignored | Major Revision |

📂 Full reports: [`showcase/en/`](showcase/en/) (English) | [`showcase/tr/`](showcase/tr/) (Turkish)  
📊 Quantitative metrics: [`docs/BENCHMARKS.md`](docs/BENCHMARKS.md)  
🔬 Controlled Vanilla Baseline: [`benchmarks/vanilla_baselines/`](benchmarks/vanilla_baselines/) (N=3 Multi-Model Factorial Study)

---

## Documentation Map

| Document | What It Contains |
|:---|:---|
| [**Whitepaper**](docs/CRUCIBLE_v6_Whitepaper.md) | Full technical specification, SOTA comparison, architecture details |
| [**Benchmarks**](docs/BENCHMARKS.md) | Quantitative metrics (M1–M8) for all 9 cases, cross-model consistency data |
| [**Vanilla Baselines**](benchmarks/vanilla_baselines/COMPARATIVE_FACTORIAL_ANALYSIS.md) | Same-day N=3 factorial benchmark: CRUCIBLE vs unconstrained LLMs on an elite doctoral prompt |
| [**Limitations**](docs/LIMITATIONS.md) | Failure modes, hard boundaries, and what CRUCIBLE cannot do |
| [**Benchmark Protocol**](benchmarks/methodology/BENCHMARK_PROTOCOL.md) | How benchmarks were designed, executed, and measured |
| [**Blind Test Protocol**](benchmarks/methodology/BLIND_TEST_PROTOCOL.md) | Protocol for testing CRUCIBLE on literature it has never seen |
| [**Contributing Guide**](CONTRIBUTING.md) | How to contribute reports, critique methodology, or improve the linter |
| [**Changelog**](CHANGELOG.md) | Version history |

---

## Known Limitations

CRUCIBLE is transparent about what it **cannot** do:

- **Not a theorem prover.** Pure symbolic mathematics (topology, number theory) requires formal proof checkers (Lean, Coq), not LLMs.
- **Not autonomous.** Human-in-the-loop is mandatory. The 3-phase interactive pause system prevents black-box output dumps.
- **Input volume ceiling.** Target dossiers exceeding ~20 pages / ~15 KB risk context dilution. Segment longer works.
- **Model drift.** AI provider weight updates can silently alter CRUCIBLE performance. The deterministic linter catches structural degradation, but not semantic regression.

Full autopsy: [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md)

---

## Contributing

CRUCIBLE must withstand its own audit. **Methodological critiques are the most valuable contributions.** See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.

---

## License & Citation

Distributed under the [**MIT License**](LICENSE).

```bibtex
@software{crucible2026,
  author  = {CRUCIBLE Open-Source Contributors},
  title   = {CRUCIBLE: An Open-Source Framework for Epistemic Auditing and Dialectical Stress-Testing},
  year    = {2026},
  url     = {https://github.com/efegok73/crucible},
  note    = {Originally conceived as May{\i}n Tarlas{\i} (Epistemic Minefield) Protocol}
}
```
