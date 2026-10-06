# CRUCIBLE v6.0 — BENCHMARK PROTOCOL
**Document ID:** `BENCHMARK_PROTOCOL.md`  
**Version:** 1.0  
**Date:** 2026-10-06  
**Status:** Active  
**Purpose:** This document defines the reproducible methodology for quantitatively evaluating CRUCIBLE v6.0 epistemic audit reports.

---

## 1. DESIGN RATIONALE

### 1.1. Why Cross-Model Instead of Single-Model Baseline?

The original benchmark plan prescribed generating a "vanilla baseline" by prompting GPT-4o with a generic critical analysis instruction, then comparing the output against a CRUCIBLE-prompted output from the same model. This approach was abandoned for three reasons:

1. **API Dependency:** Requiring paid API access to a specific model snapshot creates a reproducibility barrier for external researchers.
2. **Stronger Evidence Available:** CRUCIBLE has already been executed across **4 distinct frontier LLMs** (Claude Opus 4.6 Thinking, Claude Sonnet 4.6 Thinking, Gemini 2.5 Pro High, Gemini 2.5 Flash High) on the **same target dossiers**. This cross-model design provides more robust evidence than a single-model baseline vs. treatment comparison.
3. **Model-Invariance Hypothesis:** If CRUCIBLE produces structurally consistent, high-quality epistemic audits regardless of which frontier model executes the protocol, this demonstrates that the methodology — not the model — is the primary driver of analytical quality. This is a stronger claim than "CRUCIBLE beats vanilla prompting on one model."

### 1.2. Benchmark Architecture

```
           Same Target Dossier (benchmarks/en/XX_*.md)
                      │
        ┌─────────────┼─────────────┐
        │             │             │
   Claude Opus   Gemini Flash   Gemini Pro
   4.6 Thinking   2.5 High      2.5 High
        │             │             │
        ▼             ▼             ▼
    CRUCIBLE       CRUCIBLE       CRUCIBLE
    v6.0 Output    v6.0 Output    v6.0 Output
        │             │             │
        └─────────────┼─────────────┘
                      │
           QUANTITATIVE METRIC TABLE
       (Layer coverage, fallacy count,
        auto-falsification depth,
        linter result, byte volume,
        source matrix presence)
```

### 1.3. Supplementary Evidence Layers

In addition to the core 9 showcase cases, the following data supplements the benchmark:

| Evidence Layer | Description | Location |
|:---|:---|:---|
| **V5→V6 Evolution Test** | Same case (Evolution Methodology) analyzed by 4 different models under V5.0 protocol | `CALISMALARIM/V5TEST/` |
| **V6 Cross-Validation** | Opus and Gemini Pro independently generate V6 improvement proposals; convergence analysis performed | `CALISMALARIM/V5TEST/OPUS_V6_Capraz_Dogrulama.md`, `3.1Pro_V6_Capraz_Dogrulama.md` |
| **V6 Meta Stress Test** | 4-discipline V6 stress test (Gender, Climate, History, Psychiatry) | `CALISMALARIM/V6TEST/V6_META_TEST_RAPORU.md` |
| **Linguistic Asymmetry Reports** | EN vs TR output comparison on identical inputs | `CALISMALARIM/UC_VAKA_KARSILASTIRMALI_DIL_DENETIMI.md`, `CALISMALARIM/DILSEL_SUBSTRAT_ASIMETRISI_*.md` |
| **Model Comparison Report** | Flash vs Pro: model and language impact analysis | `CALISMALARIM/CRUCIBLE_Model_ve_Dil_Karsilastirma_Raporu.md` |

---

## 2. MEASUREMENT FRAMEWORK

### 2.1. Primary Metrics (Programmatically Extractable)

These metrics can be derived from the report markdown files without human annotation:

| # | Metric | Definition | Extraction Method | Unit |
|:---|:---|:---|:---|:---|
| M1 | **Active Layer Count** | Number of CRUCIBLE normative layers activated in triage | Regex extraction from `[EPISTEMIC TRIAGE]` section: count layers marked "Activated" or "AKTİF" | Integer (0–10) |
| M2 | **Report Volume** | Total file size of the completed audit report | File system `stat()` | Bytes (KB) |
| M3 | **Structural Integrity** | Whether the report passes the CRUCIBLE deterministic linter | Execute `crucible_linter.py` → `[PASS]` / `[FAIL]` | Binary |
| M4 | **Fallacy Detection Count** | Number of distinct logical fallacies explicitly identified and named in the report | Regex / manual count of named fallacies (e.g., "Non Sequitur", "Petitio Principii", "Proxy Leap", etc.) | Integer |
| M5 | **Auto-Falsification Depth** | Number of distinct self-identified weaknesses in the auto-falsification section | Count of enumerated items under `[AUTO-FALSIFICATION]` or `[OTO-FALSİFİKASYON]` | Integer |
| M6 | **Claims-Source Matrix Presence** | Whether a structured Thesis/Claim ↔ Source table exists (required when Layer 8 is active) | Regex detection of `| Thesis / Claim |` or `| Tez / İddia |` table pattern | Binary |
| M7 | **Surgeon Checklist Presence** | Whether the report concludes with a structured Surgeon Audit Card | Regex detection of `CERRAH` or `SURGEON` card section | Binary |
| M8 | **Linguistic Asymmetry Ratio** | Byte ratio between EN and TR versions of the same case report | `size(EN) / size(TR)` | Float |

### 2.2. Secondary Metrics (Require Human Annotation)

These metrics require a trained human annotator and are included for completeness. They will be populated as external collaborators become available:

| # | Metric | Definition | Ground Truth |
|:---|:---|:---|:---|
| M9 | **Fallacy Detection Rate** | Proportion of actual fallacies in the source text that the report identifies | Pre-annotated gold-standard fallacy inventory (min. 2 independent annotators, Cohen's κ ≥ 0.7) |
| M10 | **Hallucination Rate** | Proportion of factual claims in the report that are unverifiable or false | Source document (target dossier) cross-check |
| M11 | **Source Fidelity** | Whether citations in the report actually exist in the source material | Citation-by-citation verification |
| M12 | **Sycophancy Score** | Degree to which the model approves vs. critiques the author | Sentence-level stance annotation (approve / critique / neutral) |

> **Transparency Note:** As of v1.0 of this protocol, only M1–M8 are computed. M9–M12 require external annotators and will be populated in future iterations. This limitation is explicitly documented rather than concealed.

---

## 3. DATA INVENTORY

### 3.1. Core Benchmark Dataset: 9 Showcase Cases

Each case consists of:
- **Input:** Target Dossier (`benchmarks/en/XX_*.md`) — structured source material
- **Output (EN):** CRUCIBLE audit report (`showcase/en/XX_*_Report.md`)
- **Output (TR):** CRUCIBLE audit report (`showcase/tr/XX_*_Report.md`)

| # | Case | Discipline | Target Dossier (KB) | EN Report (KB) | TR Report (KB) |
|:---|:---|:---|:---|:---|:---|
| 01 | Judith Butler – Gender Trouble | Post-Structuralist Philosophy / Gender Studies | 9.0 | 25.0 | 18.0 |
| 02 | Jacques Lacan – Encore | Psychoanalysis / Semiotics | 11.3 | 35.2 | 18.0 |
| 03 | Cass Review – Gender Medicine | Clinical Medicine / Evidence Synthesis | 15.3 | 37.7 | 20.2 |
| 04 | Cheikh Anta Diop – African Origin | Historiography / Archaeology | 13.0 | 36.1 | 18.6 |
| 05 | Frank Snowden – Blacks in Antiquity | Classics / Ancient History | 13.9 | 34.8 | 18.3 |
| 06 | Cook et al. vs Tol – Climate Consensus | Bibliometrics / Climate Science | 11.3 | 45.5 | 20.5 |
| 07 | Judith Curry – Climate Uncertainty | Climate Science / Decision Theory | 12.7 | 42.5 | 19.8 |
| 08 | Joanna Moncrieff – Serotonin Theory | Psychiatry / Pharmacology | 14.1 | 41.8 | 20.3 |
| 09 | Simon Baron-Cohen – Essential Difference | Cognitive Neuroscience / Psychometrics | 12.3 | 49.0 | 20.0 |

### 3.2. Cross-Model Evidence: V5 Evolution Test

Same case (Evolution Theory Methodological Stress Test) analyzed by 4 frontier models under V5.0 protocol:

| Model | File | Size (KB) |
|:---|:---|:---|
| Claude Opus 4.6 (Thinking) | `V5TEST/Analiz_Opus4.6Thingking.md` | 32.8 |
| Claude Sonnet 4.6 (Thinking) | `V5TEST/Analiz_Sonnet4.6(Thinking).md` | 21.4 |
| Gemini 2.5 Pro (High) | `V5TEST/Analiz_Gemini3.1ProHigh.md` | 7.0 |
| Gemini 2.5 Flash (High) | `V5TEST/Analiz_Gemini3.8FlashHigh.md` | 11.5 |

### 3.3. Cross-Validation Evidence: V6 Improvement Proposals

Two models independently generated V6 methodology improvement proposals, then convergence was analyzed:

| Document | Description |
|:---|:---|
| `V5TEST/OPUS_V6_Capraz_Dogrulama.md` | Convergence analysis of Opus vs Gemini Pro V6 proposals (5 convergence points, 3 divergence points identified) |
| `V5TEST/3.1Pro_V6_Capraz_Dogrulama.md` | Gemini Pro's independent V6 cross-validation |

---

## 4. EXECUTION PROTOCOL

### 4.1. For 9 Showcase Cases (Already Completed)

1. **Input Preparation:** Target dossier sourced from `benchmarks/en/XX_*.md`.
2. **System Prompt:** CRUCIBLE v6.0 full methodology (`templates/CRUCIBLE_WEB_PROMPT_EN.md`).
3. **Model:** Frontier LLM (model identity recorded in report header).
4. **Temperature:** Model default (not API-controlled in Antigravity IDE environment).
5. **Output:** Report generated in both EN and TR.
6. **Validation:** Every report passed through `scripts/crucible_linter.py` — only `[PASS]` reports are included in the showcase.

### 4.2. For Cross-Model Tests (Already Completed)

1. **Same Input:** `CALISMALARIM/EVRIM_METODOLOJIK_SINAMA.md` served as the common target.
2. **Same Protocol:** V5.0 methodology (the immediate predecessor to V6.0).
3. **Different Models:** Opus 4.6, Sonnet 4.6, Gemini Pro, Gemini Flash.
4. **Each model produced one report independently.** No model saw another model's output.

### 4.3. Reproducibility Instructions for External Researchers

To independently reproduce CRUCIBLE benchmark results:

1. Clone the repository: `git clone <repo_url>`
2. Select a target dossier from `benchmarks/en/`.
3. Use the system prompt from `templates/CRUCIBLE_WEB_PROMPT_EN.md`.
4. Run with any frontier LLM (GPT-4o, Claude Opus/Sonnet, Gemini Pro, etc.).
5. Validate output with: `python scripts/crucible_linter.py <your_report.md>`
6. Compare your metrics against the published `BENCHMARKS.md` table.

> **Important:** Model behavior varies across API snapshots and weight updates. Benchmark results should be interpreted with awareness of this variance. The CRUCIBLE methodology aims for structural consistency across models, not numerical identity.

---

## 5. KNOWN LIMITATIONS OF THIS PROTOCOL

| # | Limitation | Impact | Mitigation |
|:---|:---|:---|:---|
| L1 | No controlled "vanilla baseline" comparison | Cannot directly quantify "how much better CRUCIBLE is than a generic prompt" | Cross-model consistency serves as a proxy: if the methodology produces consistent output across different models, the protocol — not the model — drives quality |
| L2 | Single annotator for M1–M8 (project founder) | Potential confirmation bias in metric extraction | Metrics M1–M7 are programmatically verifiable; M8 is arithmetic. Human annotation metrics (M9–M12) explicitly deferred |
| L3 | Reports generated in Antigravity IDE, not via API | Temperature, seed, and system prompt parameters are not API-locked | Model identity and reasoning mode are recorded in each report header |
| L4 | No variance control (single run per case per model in showcase) | Cannot compute standard deviation across runs | V5TEST cross-model data partially compensates: same case × 4 models shows structural variance |
| L5 | TR/EN linguistic asymmetry conflates translation quality with analytical quality | Size difference may reflect language efficiency, not analytical depth | Separate linguistic asymmetry reports (`docs/en/03_*`, `04_*`, `05_*`) provide dedicated analysis of this variable |

---

## 6. REVISION HISTORY

| Version | Date | Change |
|:---|:---|:---|
| 1.0 | 2026-10-06 | Initial protocol definition. Cross-model methodology adopted; API baseline approach deprecated. |
