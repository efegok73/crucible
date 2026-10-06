# CRUCIBLE v6.0 — SYSTEM LIMITATIONS & FAILURE MODES
**Document ID:** `LIMITATIONS.md`  
**Version:** 1.0  
**Date:** 2026-10-06  
**Status:** Canonical Reference  
**Applicability:** All CRUCIBLE v6.0 Deployments, Audits, and Benchmark Reproductions  

---

## 1. PURPOSE AND SCOPE

This document provides a transparent, non-defensive epistemological autopsy of the architectural, computational, and linguistic boundaries of **CRUCIBLE v6.0**. 

Academic credibility requires that a critical evaluation framework disclose its points of catastrophic failure and boundary constraints with the same forensic detachment it applies to external literature. The failures and limitations detailed herein are grounded in empirical testing across 9 benchmark dossiers, cross-model stress tests (Claude Opus 4.6, Claude Sonnet 4.6, Gemini 3.1 Pro, Gemini 3.8 Flash), and multilingual corpus comparisons.

---

## 2. STRUCTURAL & COMPUTATIONAL BOUNDARIES

### 2.1. The Monolithic Context Collapse (400+ Page Ingestion Boundary)
* **Failure Mode:** Attempting to ingest unsegmented treatises, multi-volume books, or monograph-length dossiers (>400 pages / >100,000 words) in a single analytical prompt causes **catastrophic context dilution**.
* **Observed Manifestation:** The LLM's self-attention mechanism disproportionately privileges the opening thesis and closing bibliography ("lost in the middle" phenomenon), skipping methodological annexes, technical footnotes, and statistical appendices.
* **Prescribed Mitigation:** Monograph segmentation into discrete target dossiers (max 15–20 pages / ~15 KB per audited module), executed via the two-stage pipeline defined in [`05_TWO_STAGE_PIPELINE_AND_SUBSTRATE_DYNAMICS.md`](en/05_TWO_STAGE_PIPELINE_AND_SUBSTRATE_DYNAMICS.md).

### 2.2. Formal Mathematical & Pure Deductive Derivation Limits
* **Failure Mode:** Auditing pure axiomatic mathematical proofs (e.g., topology, non-Euclidean differential geometry, pure algebraic number theory) without prose argumentation.
* **Observed Manifestation:** While CRUCIBLE successfully flags pseudo-mathematical rhetorical abuses (e.g., Lacan’s topological mathemes in Case 02), LLMs lack an integrated formal proof checker (such as Lean, Coq, or Isabelle). Symbolic reasoning in token space can generate synthetic hallucinations or superficial verification of lemma chains.
* **Boundary Definition:** CRUCIBLE is an **epistemic, empirical, and rhetorical audit gauntlet**, *not* a formal automated theorem prover (ATP). Claims resting solely on symbolic math must be evaluated by specialized ATP engines.

### 2.3. Model Weight Drift & Black-Box Instability
* **Failure Mode:** Frontier commercial LLM APIs undergo continuous silent retraining, safety alignment updates, and quantization adjustments without semantic versioning.
* **Observed Manifestation:** A prompt configuration passing the deterministic linter (`crucible_linter.py`) on version $t_0$ may experience structural degradation (loss of tables, tone softening, sycophantic regression) on version $t_1$.
* **Mitigation:** Output compliance is enforced externally and deterministically via `crucible_linter.py` in CI/CD pipelines. Any output failing the linter is discarded, regardless of the underlying LLM's claim of completion.

---

## 3. LINGUISTIC SUBSTRATE ASYMMETRY (THE ANGLOCENTRIC CEILING)

Empirical testing documented in [`03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md`](en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md) and [`04_THREE_CASE_LINGUISTIC_AUDIT.md`](en/04_THREE_CASE_LINGUISTIC_AUDIT.md) establishes an inescapable linguistic performance delta:

```
[Target Literature in English]
              │
    ┌─────────┴─────────┐
    ▼                   ▼
Prompt in English   Prompt in Turkish (Agglutinative)
    │                   │
    ▼                   ▼
Deep Forensic Surgery   The ~20 KB Smoothing Plateau
(35–50 KB / 340+ lines) (18–21 KB / ~175 lines)
+99.2% Payload Delta    Loss of Sub-scale Granularity
```

### 3.1. Sub-Word Tokenisation Penalty (BPE/WordPiece)
Morphologically complex and agglutinative languages (e.g., Turkish, Hungarian, Finnish) decompose into 2–3× more tokens per lexical unit than English. This consumes the LLM's finite attention span on morphological reconstruction rather than epistemic reasoning.

### 3.2. Premature Synthesis ("Smoothing Error")
When forced to analyze English scientific literature in a non-native language, the model exhibits early plateauing:
1. Replaces granular psychometric / biostatistical terminology (e.g., *attrition bias*, *diagnostic overshadowing*, *Krippendorff’s $\alpha$*) with colloquial abstractions.
2. Compresses multi-layered analytical matrices into flat bullet points.
3. Prematurely terminates auto-falsification (averaging 2 self-critique items in Turkish vs. 4+ in English).

---

## 4. CROSS-MODEL EXECUTION VARIANCE

Cross-validation experiments between Claude Opus 4.6, Claude Sonnet 4.6, Gemini 3.1 Pro, and Gemini 3.8 Flash revealed model-dependent failure patterns:

| Model | Primary Vulnerability | Observed Risk |
|:---|:---|:---|
| **Claude Opus 4.6 (Thinking)** | Quota exhaustion; tendency toward excessive rhetorical elaboration | High cost; execution cutoffs mid-turn if token limits are exceeded |
| **Claude Sonnet 4.6 (Thinking)** | Moderate compression on complex historical source criticism | Occasional omission of multi-source provenance triangulation |
| **Gemini 3.1 Pro (High)** | **Structural Format Collapse**; compresses tabular gauntlet into bullet points | Fails linter regex validation; loses forensic granularity |
| **Gemini 3.8 Flash (High)** | High speed and adherence, but requires explicit constraints to avoid surface-level speed bias | Requires rigid template grounding to match Opus analytical depth |

---

## 5. BENCHMARKING & EVALUATION LIMITATIONS

As codified in [`BENCHMARK_PROTOCOL.md`](../benchmarks/methodology/BENCHMARK_PROTOCOL.md):

1. **Absence of Direct Vanilla Baseline API Control:** The 9 showcase evaluations were generated without an automated side-by-side run of a vanilla system prompt under locked temperature ($T=0$) API calls. Current cross-model comparisons rely on empirical human-in-the-loop sessions.
2. **Single-Run Determinism vs. Stochastic Variance:** Benchmark metrics (M1–M8) represent validated reference outputs rather than multi-run Monte Carlo samples ($N=30$).
3. **Gold-Standard Annotation Dependency:** Programmatic metrics (M1–M7) are deterministic; qualitative metrics (M9–M12, such as Fallacy Detection Precision/Recall and Sycophancy Index) await formal multi-annotator inter-rater scoring (Cohen's $\kappa \ge 0.70$).
4. **Target Selection Bias:** The 9 benchmark cases were selected specifically for their high epistemic friction and contested status. Generalization to routine, uncontroversial scientific reporting has not been formally measured.

---

## 6. HUMAN-IN-THE-LOOP DEPENDENCY (THE EPISTEMIC SHIELD)

CRUCIBLE is explicitly designed **not** to function as an autonomous black-box arbiter:
* **No Unilateral Verdicts:** The protocol enforces interactive pauses (Phase 1 → Phase 2 → Phase 3). If an automated pipeline bypasses human intervention, the risk of uncorrected analytical bias increases by an order of magnitude.
* **The External Will Requirement:** The final layer (Surgeon Checklist) demands human physical inspection of primary archives and source data. CRUCIBLE cannot replace the primary researcher's empirical verification; it functions solely as an abrasive analytical whetstone.

---

## 7. SUMMARY TABLE: LIMITATION MATRIX

| Dimension | Constraint | Severity | Hard Boundary or Mitigated? |
|:---|:---|:---:|:---|
| **Input Volume** | Max ~20 pages per dossier | HIGH | Mitigated by two-stage extraction pipeline |
| **Domain** | Pure symbolic mathematical proofs | CRITICAL | **Hard Boundary** (Requires ATP, not LLM) |
| **Language** | Non-English source analysis | HIGH | Mitigated by Substrate Parity Law |
| **Infrastructure** | Model API weight drift | MEDIUM | Mitigated by deterministic Python linter |
| **Automation** | Full autonomous execution without human | CRITICAL | **Forbidden by Constitution** (Phase gating mandatory) |
