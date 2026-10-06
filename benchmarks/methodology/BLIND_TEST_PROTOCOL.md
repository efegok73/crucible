# CRUCIBLE v6.0 — BLIND TEST PROTOCOL
**Document ID:** `BLIND_TEST_PROTOCOL.md`  
**Version:** 1.0  
**Date:** 2026-10-06  
**Status:** Active  
**Purpose:** Standardized procedure for independently evaluating CRUCIBLE v6.0 on previously unseen academic texts.

---

## 1. OBJECTIVE

This protocol enables any external researcher to test CRUCIBLE v6.0 on a text that was **not part of the original 9-case showcase** and has **never been seen** by the CRUCIBLE developer. The goal is to demonstrate that CRUCIBLE's epistemic auditing capabilities generalize beyond cherry-picked demonstration cases.

---

## 2. ROLES

| Role | Description | Constraint |
|:---|:---|:---|
| **Test Designer** | Selects the target text and prepares the gold-standard annotation | Must NOT be a CRUCIBLE developer or contributor |
| **CRUCIBLE Operator** | Runs CRUCIBLE on the target text | Receives the target dossier only — no access to the gold-standard annotation until comparison |
| **Evaluator** | Compares CRUCIBLE output against the gold-standard annotation | Can be the Test Designer or a third party |

> **Minimal Viable Test:** In early-stage testing, a single external researcher may fill all three roles. This is acceptable as long as Step 3.2 (annotation) is completed **before** Step 3.3 (CRUCIBLE execution).

---

## 3. PROCEDURE

### Step 3.1: Target Text Selection

**Criteria:**
- The text must be a published academic work (journal article, book chapter, thesis, or policy report).
- The text must make explicit or implicit claims that can be evaluated for logical validity, source fidelity, and methodological rigor.
- The text must NOT be one of the 9 cases already in the CRUCIBLE showcase (`showcase/en/`).
- The text should be available in English or in a language with strong LLM training coverage.

**Recommended text types (descending suitability):**
1. Interdisciplinary works that cross domain boundaries (e.g., a neuroscientist making philosophical claims, a social scientist citing biological data)
2. Meta-analyses or systematic reviews with quantitative claims
3. Controversial or contested works with known methodological debates
4. Single-discipline theoretical works

**Output:** A target text (PDF, book chapter, or structured markdown).

---

### Step 3.2: Human Gold-Standard Annotation

**Before running CRUCIBLE**, the Test Designer independently annotates the target text:

| Annotation Category | Instructions |
|:---|:---|
| **Logical Fallacies** | Identify and name every logical fallacy, informal fallacy, or reasoning error in the text. Use standard taxonomy (Non Sequitur, Ad Hominem, Genetic Fallacy, Circular Reasoning, etc.). Record the page/paragraph number and the specific passage. |
| **Methodological Weaknesses** | Identify methodological problems: sampling bias, confounders, lack of controls, inappropriate statistical tests, p-hacking indicators, etc. |
| **Source/Citation Problems** | Identify misquotations, citation errors, appeal to non-peer-reviewed sources as if they were authoritative, disciplinary boundary violations (using a source outside its competence domain). |
| **Unfounded Claims** | Identify claims that lack empirical support or exceed the evidence presented. |
| **Strengths** | Identify genuine strengths and well-supported arguments (to test for sycophancy — a good auditor should acknowledge strengths too). |

**Output:** `blind_test/[test_id]/gold_standard_annotation.md`

**Critical Rule:** The gold-standard annotation must be completed and sealed (timestamped) BEFORE CRUCIBLE is executed. This prevents retrospective adjustment.

---

### Step 3.3: Target Dossier Preparation

The target text is converted into a CRUCIBLE-compatible target dossier format:

1. Extract the author's key theses / claims as verbatim passages.
2. Document the author's credentials and the work's publication context.
3. Identify the primary sources and evidentiary foundation the author relies upon.
4. Structure as a markdown document following the template in `templates/`.

**Output:** `blind_test/[test_id]/target_dossier.md`

---

### Step 3.4: CRUCIBLE Execution

1. **System Prompt:** Use the standard CRUCIBLE v6.0 web prompt (`templates/CRUCIBLE_WEB_PROMPT_EN.md`).
2. **Model:** Any frontier LLM. Record model name and version in the report header.
3. **Input:** The target dossier from Step 3.3.
4. **Run the protocol** and capture the full output.
5. **Validate:** Run `python scripts/crucible_linter.py <output.md>` — must return `[PASS]`.

**Output:** `blind_test/[test_id]/crucible_report.md`

---

### Step 3.5: Blind Comparison

The Evaluator compares the CRUCIBLE report against the gold-standard annotation:

| Comparison Metric | Definition | How to Compute |
|:---|:---|:---|
| **True Positives (TP)** | Fallacies/weaknesses identified by BOTH the human annotator AND CRUCIBLE | Count items present in both lists |
| **False Negatives (FN)** | Fallacies/weaknesses identified by the human annotator but MISSED by CRUCIBLE | Count items in gold standard but absent from CRUCIBLE report |
| **False Positives (FP)** | Issues flagged by CRUCIBLE that the human annotator considers invalid or non-existent | Count CRUCIBLE findings rejected by human evaluation |
| **Novel Discoveries (ND)** | Issues CRUCIBLE identified that the human annotator missed but, upon reflection, agrees are valid | Count items not in gold standard that the evaluator retroactively accepts |
| **Recall** | TP / (TP + FN) | Proportion of actual issues that CRUCIBLE detected |
| **Precision** | TP / (TP + FP) | Proportion of CRUCIBLE's findings that are valid |

**Output:** `blind_test/[test_id]/comparison_results.md`

---

### Step 3.6: Results Documentation

The final blind test report includes:

1. **Test Metadata:** Date, Test Designer identity, model used, target text citation.
2. **Gold-Standard Summary:** Number and types of annotated fallacies/weaknesses.
3. **CRUCIBLE Performance Summary:** TP, FN, FP, ND, Recall, Precision.
4. **Qualitative Analysis:** 
   - Where did CRUCIBLE excel? (e.g., finding cross-disciplinary boundary violations)
   - Where did CRUCIBLE fail? (e.g., missing domain-specific statistical errors)
   - Did CRUCIBLE find anything the human missed?
5. **Limitations and Caveats.**

**Output:** `blind_test/[test_id]/blind_test_report.md`

---

## 4. DIRECTORY STRUCTURE

```
blind_test/
└── [test_id]/                          # e.g., "BT001_Pinker_Better_Angels"
    ├── gold_standard_annotation.md     # Human annotation (sealed before execution)
    ├── target_dossier.md               # CRUCIBLE input
    ├── crucible_report.md              # CRUCIBLE output
    ├── comparison_results.md           # TP/FN/FP/ND analysis
    └── blind_test_report.md            # Final summary report
```

---

## 5. INTERPRETATION GUIDELINES

| Recall | Interpretation |
|:---|:---|
| ≥ 80% | Strong: CRUCIBLE detects the vast majority of human-identified issues |
| 60–80% | Moderate: Useful as a first-pass auditor, but human review still essential |
| < 60% | Weak: Significant gaps — investigate which categories are missed |

| Precision | Interpretation |
|:---|:---|
| ≥ 80% | High: CRUCIBLE's findings are overwhelmingly valid |
| 60–80% | Moderate: Some noise, but majority of findings are actionable |
| < 60% | Low: Too many false positives — CRUCIBLE is over-flagging |

| Novel Discovery Rate | Interpretation |
|:---|:---|
| ND > 0 | Positive signal: CRUCIBLE found valid issues the human missed — demonstrates complementary analytical value |
| ND = 0 | Neutral: CRUCIBLE matched but did not exceed human capability |

> **Expected Profile:** Based on the 9 showcase cases, CRUCIBLE's expected strength is in cross-disciplinary boundary violations (Layer 8), implicit proxy errors, and structural fallacy detection. Its expected weakness is in domain-specific quantitative errors requiring specialized expertise (e.g., specific statistical test misapplication in niche fields).

---

## 6. KNOWN LIMITATIONS OF THIS PROTOCOL

1. **Single-annotator vulnerability:** Until external annotators participate, gold standards reflect one researcher's judgment.
2. **Annotator competence ceiling:** The gold standard is limited by the annotator's domain expertise. A biologist may catch errors a philosopher misses, and vice versa.
3. **Subjectivity in FP/ND classification:** Whether a CRUCIBLE finding is a "false positive" or a "novel discovery" requires judgment.
4. **No blinding of CRUCIBLE to text context:** CRUCIBLE receives the full target dossier including metadata. True double-blind testing is not feasible with current LLM architecture.

---

## 7. REVISION HISTORY

| Version | Date | Change |
|:---|:---|:---|
| 1.0 | 2026-10-06 | Initial blind test protocol definition. |
