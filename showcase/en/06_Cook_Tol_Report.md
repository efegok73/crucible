# CRUCIBLE v7.3 — Grounded Epistemic Audit Report (Case 06)

**Target Work:** John Cook, Dana Nuccitelli, Sarah A. Green, Mark Richardson, Bärbel Winkler, Rob Painting, Robert Way, Peter Jacobs & Andrew Skuce (2013) — *"Quantifying the consensus on anthropogenic global warming in the scientific literature"*, *Environmental Research Letters* 8:024024 (`doi:10.1088/1748-9326/8/2/024024`) `[P:0003]`  
**Audited By (AI Model):** Gemini 4 Hydrogen Extra High  
**Primary Source Document:** `Cook_2013_Environ._Res._Lett._8_024024.pdf` (`Cook_Indexed_Source.txt`, 9 Indexed Paragraphs `[P:0001]`–`[P:0009]`)  
**Analytical Standard:** CRUCIBLE v7.3 Primary-Grounded Epistemic Architecture (`L1–L5`, $L_{source} \equiv L_{audit}$: English Native Audit)  
**Operational Status:** Stage 1 Primary Audit (Single-Document Scope; External Supplementary Tables `S1`/Sections & Post-2013 Critiques Excluded from Verdict Engine per `L5`)

> **Audit Cockpit (`L5` Navigation Index — Grounded `[P:xxxx]` Pointers):**
> - **Verdict Summary:** Negligible peer-reviewed AGW rejection (`78 / 11,944 = 0.7%`) **Survives (Strong)** (`[P:0003]`, `[P:0006]`); equivalence of the headline `97.1%` rate to `>50%` primary human causation requires **Major Revision** (`[P:0004]`–`[P:0007]`).
> - **Key Quantitative Anchors:** `11,944` abstracts (`1991–2011`); Endorse `32.6% (3,896)` / `97.1%` position; No position `66.4% (7,930)`; Reject `0.7% (78)`; Uncertain `0.3% (40)` `[P:0003]`, `[P:0006]`; Self-ratings `2,142` papers (`14%` author response rate on `8,547` emailed) -> Endorse `62.7% (1,342)` / `97.2%` position `[P:0006]`–`[P:0007]`.
> - **Top 3 Structural Fissures:** (1) Threshold folding of `Level 3 Implicit` into the headline `>50%` causation claim without cell counts `[P:0004]`–`[P:0006]`; (2) `27%`/`33%` -> `11%`/`16%` rater disagreement lacking $\kappa$/$\alpha$ and unadjusted `14%` self-rating attrition (`12 -> 39` Reject jump in Table 5) `[P:0005]`–`[P:0007]`; (3) Search-query corpus truncation (`11,944` vs `43,548` vs `128,440`) and Oreskes `75%` vs `28%` sensitivity `[P:0008]`.
> - **Single-Document Boundary (`L5`):** Unverified external primary splits or econometrics (`[EXTERNAL VERIFICATION CANDIDATE]`) are banned from Surgery/K8 and routed solely to `## 5. SURGEON CHECKLIST`.

---

## 1. EPISTEMIC TRIAGE

Layer activation follows strictly from the empirical tasks inside this 7-page primary paper (bibliometric database filtering, multi-rater ordinal content coding, linear trend regression, and author self-rating survey methods):

| Layer | Status | Methodological Justification for Inclusion / Exclusion |
| :--- | :---: | :--- |
| **K1: Epistemic Virtue & Anti-Sycophancy** | ✅ ACTIVE | Mandatory baseline. Enforces neutrality against both climate-denialist dismissal of physics and activist treating of `"97%"` as immune to measurement audit, given authors' citizen-science origin at *Skeptical Science* (`[P:0004]`, `[P:0008]`). |
| **K2: Philosophical Method (Steelmanning & Falsification)** | ✅ ACTIVE | Mandatory baseline. Evaluates whether excluding `"no position"` abstracts measures mature paradigm normality versus inflating consensus boundaries (`[P:0007]`, `[P:0008]`). |
| **K3: Hermeneutics, Conceptual Hygiene & Structural Safeguards** | ✅ ACTIVE | Critical layer. Audits semantic drift between Table 2 Level 1 (`>50%` human causation), Level 3 (`assumes greenhouse gas emissions cause warming`), and consolidated `Endorse AGW` headlines (`[P:0004]`–`[P:0006]`). |
| **K4: Quantitative Methodology & Bayesian Statistics** | ✅ ACTIVE | Triggered by denominator definitions (`11,944` vs `4,014`), regression trends (`R2`, `p`-values), `2,142` self-rating proportions, `14%` survey response attrition, and author-per-paper differences (`[P:0005]`–`[P:0007]`). |
| **K5: Experimental Design & Causality** | ❌ EXCLUDED | Strictly observational bibliometric content analysis and voluntary author questionnaire; no randomized interventions or causal physical experiments exist in the study. |
| **K6: Evidence Hierarchy & Systematic Review** | ✅ ACTIVE | Triggered by Web of Science systematic literature screening rules, elimination criteria (`12,465 -> 11,944`), inter-rater arbitration protocol, and comparison against Oreskes (2004) / Schulte (2008) (`[P:0004]`–`[P:0008]`). |
| **K7: Decision Science & Open Science** | ✅ ACTIVE | Triggered by the study's explicit policy-communication rationale (`Ding et al 2011`, `Lewandowsky et al 2012` `[P:0003]`, `[P:0008]`) and omission of per-level raw counts from the published tables (`[P:0006]`). |
| **K8: Disciplinary Matrix & Reference Audit** | ✅ ACTIVE | Evaluates bibliometrics, content-analysis reliability standards, and survey methodology solely against citations present inside `[P:0001]`–`[P:0009]`. |
| **K9: Computational Models & Simulation** | ❌ EXCLUDED | Zero machine learning classifiers or climate GCM simulations are run; all ratings were coded manually via web interface (`[P:0004]`). |
| **K10: Complexity, Extended Ethics & Epistemic Autopsy** | ✅ ACTIVE | Mandatory baseline. Synthesizes epistemic casualties, surviving core findings, dual-use science communication ethics, and external verification directives. |

---

## 2. STEELMANNING

Reconstructed in its strongest and most coherent scientific formulation, Cook et al. (2013) set out to test an empirical sociology-of-science claim: **whether peer-reviewed climate research contains a growing or substantial body of scientific rejection of anthropogenic global warming (AGW)**, as public polls (`57%–60%` US disagreement perception `[P:0004]`, `[P:0008]`) and dissenting commentaries (`Oddie 2012`, `Allègre et al 2012` `[P:0008]`) asserted.

1. **Demonstrating the Virtual Absence of Peer-Reviewed Rejection (`[P:0003]`, `[P:0006]`):**  
   Examining `11,944` Web of Science articles (`1991–2011`, `29,083` authors across `1,980` journals) matching `'global climate change'` or `'global warming'`, blinded raters classified only `78` abstracts (`0.7%` of all abstracts; `1.9%` of position-taking abstracts; `124` authors = `0.4%`) as implicitly or explicitly rejecting AGW (`[P:0005]`, `[P:0006]`). Furthermore, across `21` years, rejection self-ratings showed a statistically significant negative linear trend (`−0.25% ± 0.18% yr⁻¹`, `R² = 0.28, p = 0.01`) `[P:0007]`, directly falsifying claims that dissenting literature is expanding (`[P:0008]`).

2. **Sociology-of-Science Justification for Excluding Silent Abstracts (`[P:0007]`, `[P:0008]`):**  
   Finding `66.4% (7,930)` abstracts with `"No position"` does not imply agnosticism on greenhouse physics; under Kuhnian normal science cited via Oreskes (`2007`) and Shwed & Bearman (`2010`), mature disciplines stop restating settled premises inside concise article abstracts `[P:0007]`. Cook et al. empirically tested this hypothesis in Phase 2 rather than merely assuming it: among papers whose abstracts expressed no position, authors reading their own full papers rated `"53.8% were self-rated as endorsing the consensus"` `[P:0006]`, reducing `"No position"` from `62.5%` (abstract rating) to `35.5%` (self-rating) on the exact same `2,142` paper subset (`Table 5` `[P:0007]`), while converging on a nearly identical conditional consensus ratio (`97.1%` abstracts vs. `97.2%` self-ratings `[P:0003]`).

3. **Authorial Caveats & Scope Boundaries Honored (`Devil's Advocate Record`):**  
   To avoid Straw Man distortion, all major methodological cautions disclosed inside Cook et al.'s text must be credited upfront:
   - **Corpus Representativeness Limit:** Authors explicitly warn that `"11 944 papers is only a fraction of the climate literature"`, contrasting `'climate change'` (`43,548` papers) and `'climate'` (`128,440` papers) (`[P:0007]`–`[P:0008]`).
   - **Abstract Brevity & Ambiguity:** They acknowledge short abstracts omit full-paper context and ambiguous wording hindered classification (`[P:0008]`).
   - **Disclosed Ideological Alignment & Protocol Drift:** They openly report the project's *Skeptical Science* origin (`[P:0004]`), admit that `"clarifications and amendments were required as specific situations presented themselves"`, and explicitly flag potential bias: `"Two sources of rating bias can be cited: ﬁrst, given that the raters themselves endorsed the scientiﬁc consensus on AGW, they may have been more likely to classify papers as sharing that endorsement."` (`[P:0008]`), alongside opposite `'erring on the side of least drama'` (ESLD) undercounting (`mean difference 0.6 in units of endorsement level` `[P:0008]`).

   **Strongest Steelman Core:** Even without relying on subtle Level 1–3 gradations, Cook et al. solidly substantiate that active peer-reviewed rejection of AGW in `'global warming'` / `'global climate change'` abstracts (`0.7%`) and responding authors (`1.8%`) constitutes a vanishingly small minority (`[P:0006]`–`[P:0007]`).

---

## REAL METHODOLOGICAL SURGERY

Filtering out every caveat Cook et al. proactively acknowledged leaves **three genuine, unmitigated structural fissures** strictly observable inside `[P:0001]`–`[P:0009]`:

### Fissure 1: Seven-to-Three Bucket Consolidation Hides the Primary Threshold (`Level 1` `>50%` vs `Level 3` Implicit) (`K3`, `K4`, `K7`)
Section 1 and Methodology explicitly anchor the scientific consensus definition to human causation exceeding half of modern warming: `"in order to determine the level of scientific consensus that human activity is very likely causing most of the current GW (anthropogenic global warming, or AGW)"` (`[P:0004]`, echoing the `2007 IPCC` criterion `"humans are contributing more than 50% of global warming"` `[P:0004]`).

Table 2 then operationalizes **seven distinct ordinal categories**, including:
- **Level (1) Explicit endorsement with quantification:** `"Explicitly states that humans are the primary cause of recent global warming"` `[P:0005]`
- **Level (2) Explicit endorsement without quantification:** `"Explicitly states humans are causing global warming or refers to anthropogenic global warming/climate change as a known fact"` `[P:0005]`
- **Level (3) Implicit endorsement:** `"research assumes greenhouse gas emissions cause warming without explicitly stating humans are the cause"` (Example: `". . . carbon sequestration in soil is important for mitigating global climate change"`) `[P:0005]`

Yet immediately after defining this 7-tier hierarchy, Section 3 collapses all boundaries:
> `"To simplify the analysis, ratings were consolidated into three groups: endorsements (including implicit and explicit; categories 1–3 in table 2), no position (category 4) and rejections (including implicit and explicit; categories 5–7)."` `[P:0005]`

1. **Non-Disclosure of Level 1–3 & 5–7 Marginal Counts:** Neither `Table 3` (`[P:0006]`) nor any paragraph in the 7-page published paper reports how many of the `3,896` endorsed abstracts fell into **Level 1 (`>50%` primary cause)** versus **Level 3 (`implicit`)**! Notice also `Table 4` Footnotes `a–c`: `"Self-rated papers that endorse AGW have an average endorsement rating less than 4 (1 = explicit endorsement with quantification, 7 = explicit rejection with quantification)."` (`[P:0007]`). Thus a mitigation abstract assuming greenhouse warming (`Level 3`) and a borderline `3.5` average score carry identical weight in the `97.1%` / `97.2%` headline ratio as a quantitative attribution paper demonstrating `>50%` anthropogenic warming (`Level 1`).
2. **Conceptual Hypertrophy (`K3` Semantic Equivalence Collapse):** Comparing `Cook`'s Oreskes replication in `[P:0008]` reveals how decisive implicit-endorsement classification rules are: `"Oreskes determined that 75% of papers endorsed the consensus, based on the assumption that mitigation and impact papers implicitly endorse the consensus."` `[P:0008]` versus Cook's own coding (`28%` endorsement and `72%` no position `[P:0008]`). Cook et al. recognize that Oreskes' `75%` vs their `28%` gap stemmed directly from `"implicit"` rules—yet still pool Level 3 mitigation/impact abstracts inside their own `32.6%` / `97.1%` consensus headline while withholding per-level counts.
- **One Concept, One Concrete Example (The Severity Bracket Folding):** A hospital reporting *"97.1% of symptomatic patients required cardiac intervention"* while internally merging Category 1 *(major bypass surgery)*, Category 2 *(oral statin prescription)*, and Category 3 *(routine blood-pressure monitoring without cardiac diagnosis)* into a single undisclosed bucket—while withholding separate Category 1 counts—creates a headline impression of surgical prevalence unverified by its published tables.

---

### Fissure 2: Inter-Rater Agreement Gaps, Advocacy Volunteer Skew & Asymmetric `Table 5` Attrition (`K1`, `K4`, `K6`)
Cook et al. state candidly that `"This letter was conceived as a ‘citizen science’ project by volunteers contributing to the Skeptical Science website (www.skepticalscience.com)."` `[P:0004]`, where `12` core volunteers performed `97.4% (23,061)` ratings (`2.6% = 607` by `12` others `[P:0004]`–`[P:0005]`). Examine the reliability and survey numbers reported verbatim `[P:0005]`–`[P:0007]`:

> `"Initially, 27% of category ratings and 33% of endorsement ratings disagreed."` `[P:0005]`
> `"Following this, 11% of category ratings and 16% of endorsement ratings disagreed; these were then resolved by a third party."` `[P:0005]`
> `"We emailed 8547 authors an invitation to rate their own papers and received 1200 responses (a 14% response rate)."` `[P:0006]`

1. **Absence of Chance-Corrected Reliability & Resolution Direction:** A one-third (`33%`) initial disagreement rate—remaining at `16%` across nearly `12,000` abstracts (~`1,911` disputed endorsements requiring third-party adjudication) *even after unblinded justification among pro-consensus volunteers*—is statistically substantial. The paper supplies raw percentage disagreement only, omitting chance-corrected reliability coefficients (`Krippendorff's alpha` or `Cohen's kappa`), individual rater-pair confusion matrices, and whether third-party arbitration broke ties symmetrically. Additionally, re-checking only `"a random sample of 1000 ‘No Position’ category abstracts"` (`[P:0005]`) leaves `6,930` uninspected abstracts unquantified (`40` Uncertain extrapolated from `1,000` `[P:0006]`).
2. **Unadjusted `14%` Author Survey Selection & Overlooked Rejection Multiplication in `Table 5`:** Authors emphasize that `"More than half of the abstracts that we rated as ‘No Position’ or ‘Undecided’ were rated ‘Endorse AGW’ by the paper’s authors."` (`[P:0007]`, `53.8%` `[P:0006]`), attributing the abstract shortfall strictly to `"scientific reticence"` and `"ESLD"` undercounting endorsements (`[P:0008]`). Yet `Table 5` `[P:0007]` reveals a striking overlooked symmetry:
   - Abstract `Endorse`: `791 (36.9%)` -> Self-rated `1,342 (62.7%)` (**1.70×** increase; note `791/2142 = 36.9%` vs `32.6%` overall indicates slightly higher response among already-endorsed papers).
   - Abstract `Reject`: `12 (0.6%)` -> Self-rated `39 (1.8%)` (**3.25×** proportional increase—and author-level rejection reached `2.8%` of position papers / `3.6%` of respondents in `Table 4` vs `1.9%` / `1.2%` in `Table 3`!).
   Thus, abstract-only coding suppressed *both* Endorsement and Rejection stances (`No Position` collapsed from `62.5%` to `35.5%`), yet Section 4.1 (`[P:0008]`) interprets that gap selectively as evidence only of endorsement undercounting, while leaving the `86%` non-response cohort unadjusted.
- **One Concept, One Concrete Example (Two-Way Compression Diagnosed as One-Way Error):** Comparing abbreviated telegrams against long letters and concluding that brief summaries always drop praise—when the full table shows critical disagreements (`12 -> 39`) multiplied by a higher ratio (`3.25×`) than endorsements (`791 -> 1,342`, `1.70×`)—highlights one tail of abstract ambiguity while masking two-way information loss.

---

### Fissure 3: Search-Frame Sensitivity & Gateway Policy-Communication Bridging (`K2`, `K3`, `K7`)
Track how sample boundaries interact with rhetorical conclusions between Sections 3 and 5:

1. **Corpus Slice Fragility (`11,944` vs `43,548` vs `128,440` `[P:0008]`):** Authors candidly report that restricting queries to `'global warming'` or `'global climate change'` captures `11,944` papers, whereas `"over the same period yields 43 548 papers, while a search for ‘climate’ yields 128 440 papers."` `[P:0008]` (`27.4%` and `9.3%` of broader candidate sets, respectively). Why non-inclusion of `~31,600` `'climate change'` articles omits no systematic bias—especially when testing a meta-claim about *the scientific climate literature* (`[P:0003]`, `[P:0004]`)—remains empirically untested. Meanwhile, the paper's `Schulte (2008)` reconciliation (`529` vs `539` papers; `0` vs `6` explicit rejections `[P:0008]`) concedes that `"the reason for this discrepancy is unclear as Schulte’s exact methodology is not provided."` (`[P:0008]`).
2. **Descriptive Bibliometrics Mapped to Instrumental Policy Action (`[P:0003]`, `[P:0008]`):** Section 1 and Section 5 open and close with the political proposition that `"An accurate perception of the degree of scientific consensus is an essential element to public support for climate policy"` (`[P:0003]`) and `"is a necessary element in public support for climate policy (Ding et al 2011)."` (`[P:0008]`). Elevating the conditional statistic (`97.1%` / `97.2%` among stance-taking papers) to anchor public policy messaging systematically encourages lay readers to drop two critical mathematical conditions: (i) `66.4%` (`7,930/11,944`) of abstracts expressed no AGW stance (`[P:0006]`), and (ii) Level 3 implicit assumptions are merged cleanly into `Endorse AGW` (`[P:0005]`).
- **One Concept, One Concrete Example (The Denominator Sticker Shock):** Printing *"97.1% Consensus Proven"* on policy flyers while keeping *"across the 33.6% of abstracts taking a position, including papers assuming greenhouse warming as background context"* in Section 2 prose turns a conditional bibliometric subset into an unconditional public statistic.

---

## FALLACY AUDIT

Isolating structural inference errors in the primary paper (`[P:0001]`–`[P:0009]`):

1. **Measurement Equivalence Collapse (`K3` / Operational Drift):** Equating `Level 3 Implicit endorsement` (`"assumes greenhouse gas emissions cause warming without explicitly stating humans are the cause"` `[P:0005]`) with the study's headline IPCC attribution thesis (`">50%"` primary human causation `[P:0004]`, `[P:0005]`) inside consolidated `"Endorse AGW"` totals without reporting per-level splits (`[P:0006]`).
2. **Conditional Denominator Ambiguity (`K4`):** Presenting `97.1%` (`[P:0003]`) in the Abstract and Conclusion (`[P:0008]`) alongside `"32.6% endorsed AGW"` (`[P:0003]`) yet centering public-communication framing (`Ding et al 2011`) on the conditional numerator/denominator ratio.
3. **Selective Interpretation of Abstract-to-Full-Text Divergence (`K1`, `K4`):** Treating Table 5's expansion (`791 -> 1,342` Endorse) as diagnostic proof of `ESLD` undercounting of consensus (`[P:0008]`), while omitting discussion of the steeper `3.25×` expansion in author self-rated Rejections (`12 -> 39`, `[P:0007]`).
4. **Unquantified Volunteer-Coder Reliability (`K1`, `K6`):** Reporting raw unresolved disagreement (`16%` endorsement discrepancy `[P:0005]`) among self-selected *Skeptical Science* volunteers (`[P:0004]`) without $\kappa$/$\alpha$ reliability metrics or neutral-group sensitivity bounds.
5. **Descriptive-to-Normative Policy Slippage (`K7`):** Framing bibliometric classification trends directly around correcting `"consensus gap"` campaigns to unlock `"public support for climate policy"` (`[P:0008]`), creating downstream amplification pressure.

---

## LAYER 8: CLAIMS-SOURCE AUDIT MATRIX

Evaluating each major claim strictly against primary-text grounding (`[P:0001]`–`[P:0009]`) under `L5` Single-Document Discipline:

| Claim / Thesis | Foundational Source Cited | Source Status & Type | Methodological Verdict |
| :--- | :--- | :--- | :--- |
| `97.1%` of position-taking abstracts endorse AGW consensus (`32.6%` of all `11,944` abstracts; `66.4%` no position) (`[P:0003]`, `[P:0006]`) | Cook et al. (`2013`), Section `3.1`, Table 2, Table 3 (`[P:0005]`–`[P:0006]`) | `[PRIMARY DATA]` — `11,944` Web of Science abstracts (`23,668` paired ratings) | **Arithmetically Consistent / Granularity Withheld:** `3,896 / (3,896 + 78 + 40) = 97.06%` holds arithmetically on consolidated groups, yet merging Level 3 (`implicit`) with Level 1 (`>50%`) without per-level counts (`[P:0005]`) prevents independent threshold auditing. |
| Active peer-reviewed AGW rejection is vanishingly small (`0.7%` abstracts / `1.8%` self-rated) (`[P:0003]`, `[P:0006]`, `[P:0007]`) | Cook et al. (`2013`), Table 3 (`78`), Table 4 (`39`), Figure 2 (`p = 0.01`) (`[P:0006]`–`[P:0007]`) | `[PRIMARY DATA]` — Blinded abstract corpus + author self-ratings | **Strongly Supported Core Finding:** Even allowing coding boundary sensitivity (`Schulte 2008` `6%` comparison `[P:0008]`), active rejection across queried climate abstracts remains rare (`<2%`). |
| Author self-ratings (`97.2%` of position papers) confirm that silent abstracts mostly assume AGW (`[P:0003]`, `[P:0006]`, `[P:0007]`) | Cook et al. (`2013`), Section `3.2`, Table 4, Table 5 (`53.8%` `[P:0006]`–`[P:0007]`) | `[SURVEY DATA]` — Voluntary email survey (`1,200 / 8,547 = 14%` response rate) | **Partially Supported / Unadjusted Attrition:** Proves abstracts omit explicit framing relative to full manuscripts, yet suffers unmodeled `86%` non-response bias and asymmetrical omission of Table 5's `12 -> 39` (`3.25×`) rejection jump. |
| Rater ideological alignment and scientific reticence balanced out via anonymous multi-rater design (`[P:0004]`, `[P:0005]`, `[P:0008]`) | Section 2; Section `4.1`; `Skeptical Science` (`[P:0004]`, `[P:0005]`, `[P:0008]`) | `[METHODOLOGY DISCLOSURE]` — Raw agreement rates (`33%` -> `16%` disagreement) | **Incompletely Substantiated (`K1`, `K6`):** Author transparency is high (`[P:0008]`), yet absence of $\kappa$/$\alpha$ statistics, third-party tie directions, and `6,930` un-resampled `'No Position'` abstracts weakens reliability claims. |
| Mature consensus explains why `66.4%` of abstracts omit stance and replicates `Oreskes (2004)` (`[P:0004]`, `[P:0007]`, `[P:0008]`) | Oreskes (`2004`, `2007`); Shwed and Bearman (`2010`); Schulte (`2008`) `[P:0004]`, `[P:0007]`–`[P:0008]` | `[COMPARATIVE LITERATURE]` + Internal `894`-paper overlap check `[P:0008]` | **Methodologically Revealing Comparison:** Confirms zero rejections in the `1993–2003` Oreskes subset (`0 / 894`), yet highlights `75%` vs `28%` sensitivity to implicit categorization rules (`[P:0008]`). |
| `'global warming'` + `'global climate change'` (`11,944`) tracks broader climate science (`[P:0004]`, `[P:0008]`) | Section `4.1` (`43 548` `'climate change'`, `128 440` `'climate'`) `[P:0008]` | `[BIBLIOMETRIC SEARCH BENCHMARK]` | **Scope Boundary Enforced:** Leaves `~73%` (`43,548`) to `~91%` (`128,440`) of broader climate-indexed Web of Science entries outside empirical inspection. |

---

## 3. AUTO-FALSIFICATION

Applying the mandatory 7-question Cognitive Self-Audit (`K2.9`) and `L5` Single-Document disclosure:

1. **Unquestioned Assumptions Scan:** This audit scrutinized measurement granularity (Level 1 vs. Level 3) and survey attrition (`14%`), which could leave the reader underestimating how rare explicit counter-consensus papers truly are (`78` in `11,944` `[P:0006]`). Methodological measurement fuzziness in coding thresholds does not flip `78 / 11,944` into a parity scientific dispute.
2. **Strawman Audit (`Steelman` Fairness Test):** Did we overstate the claim that Cook et al. conflated Level 3 with `>50%` primary causation? Fair defense: Cook et al. openly define Level 1–3 transparently in `Table 2` (`[P:0005]`), print `32.6%` right beside `97.1%` in the very first sentence of the Abstract (`[P:0003]`), and explicitly label Table 3's metric `"% among abstracts with AGW position"` (`[P:0006]`). The methodological critique targets the omission of Level 1–3 counts and the downstream rhetorical elevation of the `"97%"` figure (`[P:0008]`).
3. **Strongest Counter-Argument Against This Audit:** A rigorous bibliometrician can argue that *if* human causation of AGW were genuinely contested inside atmospheric physics, papers rejecting AGW would not represent `0.7%` of `11,944` articles nor average only `2.0` co-authors vs. `3.4–3.6` (`[P:0006]`), and even a harsh `3.25×` self-rating sensitivity still leaves rejection at `1.8% (39 / 2,142)` (`[P:0007]`). Thus the directional conclusion holds independently of Level 1 vs. Level 3 edge coding.
4. **Rhetoric vs. Evidence Separation:** Concrete analogies ("Severity Bracket Folding," "Two-Way Compression") merely illustrate structural patterns; removing every illustration leaves all numeric anomalies intact verbatim inside the paper (`11%`/`16%` disagreement `[P:0005]`, unstratified `3,896` sum `[P:0006]`, `14%` survey response `[P:0006]`, Table 5 `12 -> 39` jump `[P:0007]`, `43,548`/`128,440` search gap `[P:0008]`).
5. **Single-Document & Supplementary Boundary (`L5` Transparency Disclosure):** Under CRUCIBLE `L5` (`Alternatif 1`), this primary audit evaluated **strictly** the 7-page `Cook_2013` PDF (`[P:0001]`–`[P:0009]`) plus established `Class 1` psychometrics and survey statistics. External supplementary data files (`stacks.iop.org/ERL/8/024024/mmedia` referenced in `[P:0003]`, `[P:0005]`, `[P:0006]`, `[P:0008]`), external post-2013 econometric comments (e.g., *Tol*), and granular Level 1/2/3 primary-data breakdowns reside outside this single PDF and are routed solely to `## 5. SURGEON CHECKLIST` as `[EXTERNAL VERIFICATION CANDIDATE]`.
6. **Bayesian Belief Update (Directional Only — K4.2.1):**
   - *Thesis A ("Peer-reviewed literature contains negligible active rejection of AGW, <2%"):* Posterior confidence rises strongly (**↑↑**), corroborated by both abstract coding (`0.7%`) and responding author self-ratings (`1.8%`) (`[P:0006]`–`[P:0007]`).
   - *Thesis B ("97.1% of queried climate abstracts explicitly quantify `>50%` anthropogenic causation"):* Posterior confidence drops sharply (**↓↓**), unsupported because Level 1–3 counts are consolidated and `Level 3` counts implicit background assumptions (`[P:0005]`).
7. **Generalizability & Temporal Boundaries:** Strictly bounded to `1991–2011` Web of Science `'article'` records matching `'global warming'` / `'global climate change'` (`11,944` of `43,548` `'climate change'` / `128,440` `'climate'` `[P:0008]`), prior to obtaining external supplementary rating datasets.

---

## 4. DAMAGE REPORT

### Epistemic Damage Ledger & Minimal Epistemic Toll (`K1.5`, `K10`)

| Audited Component | Post-Audit Epistemic Status | Nature of Sustained Structural Damage |
| :--- | :---: | :--- |
| **1. Low Rejection Prevalence Core** *(Active AGW rejection is `<1%` abstracts / `<2%` self-ratings)* | **SURVIVES (STRONG)** | Supported across `11,944` abstracts (`78` rejections, `0.7%` `[P:0006]`) and `2,142` full-paper self-ratings (`39` rejections, `1.8%` `[P:0007]`). |
| **2. Consolidated `97.1%` / `97.2%` Metric Equivalence to `>50%` Attribution** | **DAMAGED (MAJOR REVISION)** | Consolidated categories `1–3` conceal exact Level 1 (`>50%` explicit) vs. Level 3 (`implicit assumption`) shares inside published tables (`[P:0005]`–`[P:0006]`), enabling public semantic overreach. |
| **3. Blinded Volunteer Coding Neutrality** | **PARTIALLY DAMAGED** | `16%` post-discussion endorsement disagreement resolved internally without $\kappa$/$\alpha$ reliability metrics (`[P:0005]`), volunteer alignment disclosed (`[P:0004]`, `[P:0008]`), and `6,930` neutral abstracts never re-checked beyond `1,000` sample (`[P:0005]`). |
| **4. Author Self-Rating Validation & Policy Framing** | **CONDITIONAL / FRAMING OVERREACH** | Confirms full papers endorse AGW more often than abstracts (`53.8%` shift `[P:0006]`), yet faces unadjusted `14%` attrition (`[P:0006]`), unaddressed `3.25×` rejection jump (`[P:0007]`), and normative `Gateway` messaging (`[P:0008]`). |

**Minimal Epistemic Toll Required for Scientific Survival:**
1. **Disaggregate Consolidated Categories Inside Primary Reporting:** Explicitly separate **Level 1 (`>50%` quantitative endorsement)**, **Level 2 (`unquantified explicit`)**, and **Level 3 (`implicit`)** counts in primary summary tables alongside `32.6%` unconditional and `97.1%` conditional proportions.
2. **Report Chance-Corrected Reliability & Non-Response Weighting:** Publish Cohen's $\kappa$ / Krippendorff's $\alpha$, tie-breaker distributions (`16%` unresolved slice `[P:0005]`), and propensity weights across the `86%` non-responding authors (`[P:0006]`) alongside symmetrical analysis of Table 5's `12 -> 39` rejection shift (`[P:0007]`).
3. **Restrict Headline Language:** Anchor policy headlines strictly to *"among abstracts taking a position matching `'global warming'` / `'global climate change'`, explicit or implicit endorsement stands at 97.1% vs. 1.9% rejection (`66.4%` unstated)"*.

**Surviving Minimal Claim Core:** Within `11,944` Web of Science abstracts (`1991–2011`) matching `'global warming'` or `'global climate change'`, papers rejecting anthropogenic global warming (`0.7%` of all abstracts; `1.8%` of `2,142` self-rated papers) represent a statistically minor fraction relative to papers explicitly or implicitly endorsing AGW (`32.6%` of abstracts; `62.7%` of self-rated papers), although the headline `97.1%` figure pools implicit assumptions (`Level 3`) with quantified primary-causation claims (`Level 1`).

---

## 5. SURGEON CHECKLIST

Actionable 3-minute verification protocol for the Human External Judge (`Dış İrade`):

- [ ] `[EXTERNAL VERIFICATION CANDIDATE]` **Retrieve Supplementary Dataset (`stacks.iop.org/ERL/8/024024/mmedia`):** Access the online supplementary rating spreadsheet referenced in `[P:0003]` and `[P:0005]` to extract exact separate primary-study counts for **Level 1 (`>50%` explicit)**, **Level 2 (`explicit unquantified`)**, **Level 3 (`implicit`)**, **Level 4a/4b**, and **Levels 5–7**, which were pooled into single buckets in Table 3 `[P:0006]`.
- [ ] `[EXTERNAL VERIFICATION CANDIDATE]` **Audit External Post-2013 Econometric & Coding Rebuttals (e.g., Tol 2016 ERL Comments & Cook et al. Replies):** Examine published external sensitivity re-analyses computing Krippendorff's $\alpha$, rater-drift across the `23,668` ratings (`[P:0004]`–`[P:0005]`), and denominator-sensitivity curves outside this 2013 source text.
- [ ] `[EXTERNAL VERIFICATION CANDIDATE]` **Verify Author Self-Rating Email Non-Response Bias (`Table S1` & Survey Instrument `[P:0005]`–`[P:0006]`):** Inspect the external survey questionnaire and geographic response distribution referenced in `[P:0005]` and `[P:0006]` (`91` countries) to test whether the `1,189` respondents systematically differed from the `7,358` non-respondents on institutional or geographical covariates.
- [ ] **Check `Table 5` (`[P:0007]`) Two-Sided Abstract Compression Arithmetic:** Verify on `[P:0007]` that while abstract-no-position papers shifted heavily toward `Endorse AGW` in author self-ratings (`53.8%`, `791 -> 1,342`, `1.70×`), self-rated `Reject AGW` also rose (`12 -> 39`, `3.25×`), confirming bidirectional information loss in short abstracts.
- [ ] **Check Query Corpus Boundaries (`[P:0008]`):** Verify the exact corpus ratios stated in Section 4.1 (`11,944` analyzed vs `43,548` for `'climate change'` vs `128,440` for `'climate'`) before extrapolating conclusions beyond `'global warming'` / `'global climate change'` subsets.
- [ ] **Apply the Fatal Falsification Test:** Ask: *"If you re-calculate consensus strictly on papers quantifying `>50%` primary anthropogenic attribution (Level 1 only) out of all `11,944` abstracts rather than pooling `Level 1–3` divided by stance-taking papers, does `97.1%` measure `>50%` physical attribution agreement or paradigm-background non-dissent?"*
