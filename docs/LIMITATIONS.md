# CRUCIBLE v7.1 — SYSTEM LIMITATIONS, FAILURE MODES & GROUNDING ARCHITECTURE
**Document ID:** `LIMITATIONS.md`  
**Version:** 7.1  
**Date:** 2026-11-20  
**Status:** Canonical Reference  
**Applicability:** All CRUCIBLE Deployments, Audits, and Benchmark Reproductions  

---

## 1. PURPOSE AND SCOPE

This document provides a transparent, non-defensive epistemological autopsy of the architectural, computational, and linguistic boundaries of **CRUCIBLE v7.1**. 

Academic credibility requires that a critical evaluation framework disclose its points of catastrophic failure and boundary constraints with the same forensic detachment it applies to external literature. The failures, historical design flaws, and systemic limitations detailed herein are grounded in empirical stress-testing across multi-disciplinary corpora, frontier LLMs (Claude Opus 4.6, Claude Sonnet 4.6, Gemini Pro, Gemini Flash), and the lessons learned from the v6.0 $\rightarrow$ v7.1 architectural transition.

---

## 2. STRUCTURAL & COMPUTATIONAL BOUNDARIES

### 2.1. The "Atomization Fiasco" and the Deprecation of Lossy Chunking (v6 $\rightarrow$ v7 Epistemic Autopsy)
* **Historical Design Flaw (v6.0):** In earlier iterations (v5.0–v6.0), CRUCIBLE prescribed chunking treatises and monographs into discrete "Target Dossiers" of 15–20 pages (~15 KB), operating under an obsolete assumption that frontier LLMs suffered catastrophic context collapse when processing large texts.
* **The Resulting Fiasco:** Empirical evidence proved that **arbitrary atomization is fatal to epistemic auditing**. Splitting a philosophical or empirical monograph into isolated 20-page fragments:
  1. Destroys cross-chapter dialectic coherence, preventing the model from recognizing when an author's caveat in Chapter 1 resolves an objection raised in Chapter 6.
  2. Induces context-blind hallucinations and straw-man critiques ("pseudo-surgery").
  3. Re-introduces the very sycophancy and fragmentation CRUCIBLE was designed to eradicate.
* **The v7.1 Law of Ground-Truth Immutability:** Modern frontier LLMs (featuring 1M–2M+ token active context windows) do *not* require lossy pre-segmentation. In CRUCIBLE v7.1:
  * **Arbitrary chunking is strictly prohibited.**
  * Full primary sources (PDF, DOCX, TXT) must be ingested as **unaltered ground truth**.
  * Structural precision is maintained not by cutting the text, but by deterministic paragraph indexing (`scripts/index_source.py`), assigning immutable `[P:xxxx]` coordinates to every paragraph across the entire monograph.

### 2.2. Formal Mathematical & Pure Deductive Derivation Limits
* **Failure Mode:** Auditing pure axiomatic mathematical proofs (e.g., differential topology, non-Euclidean geometry, pure algebraic number theory) without prose argumentation.
* **Observed Manifestation:** While CRUCIBLE successfully flags pseudo-mathematical rhetorical abuses and semantic posturing (e.g., Lacan’s topological mathemes in Case 02), LLMs lack an integrated formal proof checker (such as Lean, Coq, or Isabelle). Symbolic reasoning in token space can generate synthetic hallucinations or superficial verification of lemma chains.
* **Boundary Definition:** CRUCIBLE is an **epistemic, empirical, and rhetorical audit gauntlet**, *not* a formal automated theorem prover (ATP). Claims resting solely on symbolic math must be evaluated by specialized ATP engines.

### 2.3. Model Weight Drift & Black-Box Instability
* **Failure Mode:** Frontier commercial LLM APIs undergo continuous silent retraining, safety alignment updates, and quantization adjustments without semantic versioning.
* **Observed Manifestation:** A prompt configuration passing the deterministic linter (`crucible_linter.py`) on version $t_0$ may experience structural degradation (loss of tables, tone softening, sycophantic regression) on version $t_1$.
* **Mitigation:** Output compliance is enforced externally and deterministically via `crucible_linter.py` in CI/CD pipelines. Any output failing the linter is discarded, regardless of the underlying LLM's claim of completion. Verification seals are awarded **only** when grounded source verification is programmatically confirmed (`--source`).

---

## 3. LINGUISTIC SUBSTRATE ASYMMETRY (THE ANGLOCENTRIC CEILING)

Empirical testing documented in [`03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md`](en/03_SUBSTRATE_PARITY_AND_LINGUISTIC_ASYMMETRY.md) and [`04_THREE_CASE_LINGUISTIC_AUDIT.md`](en/04_THREE_CASE_LINGUISTIC_AUDIT.md) establishes an inescapable linguistic performance delta:

```
[Target Literature in English]
              │
    ┌─────────┴─────────┐
    ▼                   ▼
Prompt in English   Prompt in Agglutinative Language (e.g., Turkish)
    │                   │
    ▼                   ▼
Deep Forensic Surgery   The ~20 KB Smoothing Plateau
(35–50 KB / 340+ lines) (18–21 KB / ~175 lines)
+99.2% Payload Delta    Loss of Sub-scale Granularity
```

### 3.1. Sub-Word Tokenisation Penalty (BPE/WordPiece)
Morphologically complex and agglutinative languages decompose into 2–3× more tokens per lexical unit than English. This consumes the LLM's finite attention span on morphological reconstruction rather than epistemic reasoning.

### 3.2. Premature Synthesis ("Smoothing Error")
When forced to analyze English scientific literature in a non-native language, the model exhibits early plateauing:
1. Replaces granular psychometric / biostatistical terminology (e.g., *attrition bias*, *diagnostic overshadowing*, *Krippendorff’s $\alpha$*) with colloquial abstractions.
2. Compresses multi-layered analytical matrices into flat bullet points.
3. Prematurely terminates auto-falsification (averaging 2 self-critique items in non-English vs. 4+ in English).
* **v7.1 Mitigation:** The **Substrate Parity Law** dictates that primary audits must be conducted in the original language of the source text, with deterministic translation reserved for post-audit dissemination.

---

## 4. CROSS-MODEL EXECUTION VARIANCE

Empirical stress-testing across frontier model families reveals systematic model-dependent failure patterns:

| Model | Primary Vulnerability | Observed Risk | v7.1 Countermeasure |
|:---|:---|:---|:---|
| **Claude Opus (Thinking)** | Quota exhaustion; runaway rhetorical elaboration | High latency; execution cutoffs mid-turn | Rigid phase gating (Phase 1 $\rightarrow$ Phase 2 $\rightarrow$ Phase 3) |
| **Claude Sonnet (Thinking)** | Compression on multi-century historical source criticism | Occasional omission of multi-source provenance triangulation | Mandatory Layer 8 (Source Criticism) matrix validation |
| **Gemini Pro (Thinking / High)** | **Format Collapse Risk**; compresses tabular gauntlet into bullet points | Fails linter regex validation; loses forensic granularity | Linter rejects bullet summaries; requires explicit Markdown tables |
| **Gemini Flash (High)** | High speed and adherence, but superficial critical depth | Shallows the auto-falsification layer | Enforced 5-section constitutional structure and verbatim quote check |

---

## 5. BENCHMARKING & EVALUATION LIMITATIONS

As codified in [`BENCHMARK_PROTOCOL.md`](../benchmarks/methodology/BENCHMARK_PROTOCOL.md):

1. **Baseline Legacy Distinction:** The 18 historical showcase evaluations (`showcase/`) represent v6.0 Target Dossier baselines maintained strictly for backward regression testing. Genuine v7.1 benchmarks require full-text ground indexing (`index_source.py`).
2. **Single-Run Determinism vs. Stochastic Variance:** Benchmark metrics (M1–M8) represent validated reference outputs rather than multi-run Monte Carlo samples ($N=30$).
3. **Gold-Standard Annotation Dependency:** Programmatic metrics (M1–M7) are deterministic; qualitative metrics (M9–M12, such as Fallacy Detection Precision/Recall and Sycophancy Index) await formal multi-annotator inter-rater scoring (Cohen's $\kappa \ge 0.70$).
4. **Target Selection Bias:** The benchmark cases were selected specifically for their high epistemic friction and contested status. Generalization to routine, uncontroversial scientific reporting has not been formally measured.

---

## 6. HUMAN-IN-THE-LOOP DEPENDENCY (THE EPISTEMIC SHIELD)

CRUCIBLE is explicitly designed **not** to function as an autonomous black-box arbiter:
* **No Unilateral AI Verdicts:** The protocol enforces interactive pauses (Phase 1: Triage & Steel Man $\rightarrow$ Phase 2: Surgery & Fallacies $\rightarrow$ Phase 3: Auto-Falsification, Damage Report & Surgeon Card). If an automated pipeline bypasses human intervention, the risk of uncorrected analytical bias increases exponentially.
* **The External Will Requirement:** The final layer (Surgeon Checklist) demands human physical inspection of primary archives and source data. CRUCIBLE cannot replace the primary researcher's empirical verification; it functions solely as an abrasive analytical whetstone.

---

## 7. SUMMARY TABLE: LIMITATION MATRIX

| Dimension | Constraint | Severity | Hard Boundary or Mitigated? |
|:---|:---|:---:|:---|
| **Input Ingestion** | Monograph-length primary sources | HIGH | **Mitigated** via `index_source.py` full-text grounding (`[P:xxxx]`). Lossy chunking deprecated. |
| **Domain** | Pure symbolic mathematical proofs | CRITICAL | **Hard Boundary** (Requires Automated Theorem Provers, not LLMs) |
| **Language** | Non-native source analysis | HIGH | **Mitigated** by Substrate Parity Law (Audit in source language) |
| **Infrastructure** | Model API weight drift / formatting drift | MEDIUM | **Mitigated** by deterministic Python linter (`crucible_linter.py`) in CI/CD |
| **Verification** | Hallucinated quotes and phantom anchors | HIGH | **Mitigated** by strict linter ground-truth verification (`--source`) |
| **Automation** | Autonomous execution without human oversight | CRITICAL | **Forbidden by Constitution** (Phase gating and Surgeon Card mandatory) |
