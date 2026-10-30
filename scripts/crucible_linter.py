#!/usr/bin/env python3
"""
CRUCIBLE v7.0 — Grounded Deterministic Epistemic Audit Linter
=============================================================
Parses AI-generated CRUCIBLE analysis reports and enforces
constitutional compliance through structural, rhetorical,
layer-specific, and source-grounded validation.

Fixes addressed:
- Z1-Z10 (v6.0: hollow sections, triage group capture, scope leak,
  narrow terms, Turkish word boundaries, lang detection, verification
  seal, testability, sys.exit, MathJax/regex ordering).
- v7.0 Zero-Vulnerability Grounding:
  * Primary source cross-checking via --source (docx/txt/md).
  * Claim-Source Matrix artifact grounding (blocks phantom references like Selme/PERF 558).
  * Bracketed paragraph citation and quote verification ([P:xxxx]).
  * Segregated external comparison tagging ([DIŞ KAYNAK] / [EXTERNAL]).

Usage:
  python crucible_linter.py report.md
  python crucible_linter.py report.md --source document.docx
  python crucible_linter.py report.md --source document.docx --strict
  python crucible_linter.py report.md --json
  python crucible_linter.py report.md --source document.docx --json -o results.json
"""

import os
import sys
import re
import json
import hashlib
import argparse
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Set

try:
    import markdown
except ImportError:
    markdown = None

try:
    import docx
except ImportError:
    docx = None

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# ═══════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════

MIN_SECTION_WORDS = 15        # Z1: Minimum words for a non-hollow section
MIN_PAYLOAD_LINES = 30        # Minimum report length (lines)
MIN_PAYLOAD_CHARS = 1500      # Minimum report length (characters)

# Z5: Turkish-aware word boundary (replaces fragile \b)
_TR_ALPHA = r'a-zA-ZçÇğĞıİöÖşŞüÜâÂîÎûÛ'
_WB_L = rf'(?<![{_TR_ALPHA}])'   # left boundary
_WB_R = rf'(?![{_TR_ALPHA}])'    # right boundary

# ═══════════════════════════════════════════════════════════════════
# CORE SECTION DEFINITIONS (TR / EN canonical names)
# ═══════════════════════════════════════════════════════════════════

CORE_SECTIONS = [
    {
        'id': 'triage',
        'name_tr': 'EPİSTEMOLOJİK TRİYAJ',
        'name_en': 'EPISTEMIC TRIAGE',
        'pattern': r'\[?\s*(?:EP[İI]STEMOLOJ[İI]K\s+TR[İI]YAJ|EPISTEMIC\s+TRIAGE)\s*\]?',
        'min_words': 20,
    },
    {
        'id': 'steelman',
        'name_tr': 'ÇELİK ADAM',
        'name_en': 'STEELMANNING',
        'pattern': r'(?:ÇEL[İI]K\s+ADAM|STEELMAN(?:NING|NED|S)?)',
        'min_words': 30,
    },
    {
        'id': 'falsification',
        'name_tr': 'OTO-FALSİFİKASYON',
        'name_en': 'AUTO-FALSIFICATION',
        'pattern': r'(?:OTO-FALS[İI]F[İI]KASYON|B[İI]L[İI][ŞS]SEL\s+ÖZ-DENET[İI]M|AUTO-FALSIFICATION|EPISTEMIC\s+SELF-AUDIT|FALSIFIAB(?:LE|ILITY))',
        'min_words': 20,
    },
    {
        'id': 'damage',
        'name_tr': 'HASAR RAPORU',
        'name_en': 'DAMAGE REPORT',
        'pattern': r'(?:HASAR\s+RAPORU|ASGAR[İI]\s+EP[İI]STEM[İI]K\s+BEDEL|DAMAGE\s+REPORT|EPISTEMIC\s+TOLL|MINIMAL\s+EPISTEMIC\s+COST)',
        'min_words': 15,
    },
    {
        'id': 'surgeon',
        'name_tr': 'CERRAH DENETİM KARTI',
        'name_en': 'SURGEON CHECKLIST',
        'pattern': r'(?:CERRAH\s+(?:DENET[İI]M\s+)?KART|SURGEON(?:\'S)?\s+(?:AUDIT\s+)?(?:CARD|CHECKLIST))',
        'min_words': 10,
    },
]

# ═══════════════════════════════════════════════════════════════════
# Z4: EXPANDED FORBIDDEN TERMS (multilingual)
# ═══════════════════════════════════════════════════════════════════

FORBIDDEN_TERMS: Dict[str, list] = {
    'tr': [
        ('şüphesiz*',                    rf'{_WB_L}[şs]üphesiz\w*'),
        ('tartışmasız*',                 rf'{_WB_L}tart[ıi][şs]mas[ıi]z\w*'),
        ('kesinlikle kanıtlanmıştır',    r'kesinlikle\s+kan[ıi]tlanm[ıi][şs]t[ıi]r'),
        ('kesinlikle ispatlanmıştır',    r'kesinlikle\s+ispatlanm[ıi][şs]t[ıi]r'),
        ('entelektüel sahtekarlık',      r'entelektüel\s+sahtekarl[ıi]k'),
        ('infaz',                        rf'{_WB_L}[iıİI]nfaz{_WB_R}'),
        ('hiçbir şüpheye yer bırakmaz', r'hi[çc]bir\s+[şs]üpheye\s+yer\s+b[ıi]rakm'),
        ('bilimsel gerçektir',           r'bilimsel\s+ger[çc]ektir'),
        ('tartışma götürmez',            r'tart[ıi][şs]ma\s+götürmez'),
        ('reddedilemez*',                rf'{_WB_L}reddedilemez\w*'),
    ],
    'en': [
        ('undoubtedly',                   r'\bundoubtedly\b'),
        ('indisputable/indisputably',     r'\bindisputabl[ey]\b'),
        ('absolutely proven',             r'\babsolutely\s+proven\b'),
        ('beyond doubt',                  r'\bbeyond\s+(?:any\s+|all\s+)?doubt\b'),
        ('unquestionable/unquestionably', r'\bunquestionabl[ey]\b'),
        ('irrefutable/irrefutably',       r'\birrefutabl[ey]\b'),
        ('incontrovertible',              r'\bincontrovertibl[ey]\b'),
        ('proves conclusively',           r'\bproves?\s+conclusively\b'),
        ('undeniable/undeniably',         r'\bundeniab(?:le|ly)\b'),
        ('definitively establishes',      r'\bdefinitively\s+establish(?:es|ed)?\b'),
        ('it is certain that',            r'\bit\s+is\s+certain\s+that\b'),
    ],
    'de': [
        ('zweifellos',     r'\bzweifellos\b'),
        ('unbestreitbar',  r'\bunbestreitbar\w*\b'),
        ('unwiderlegbar',  r'\bunwiderlegbar\w*\b'),
        ('steht fest',     r'\bsteht\s+fest\b'),
    ],
    'fr': [
        ('sans aucun doute', r'\bsans\s+aucun\s+doute\b'),
        ('incontestable',    r'\bincontestabl[e]\w*\b'),
        ('irréfutable',      r'\birr[ée]futabl[e]\w*\b'),
    ],
    'es': [
        ('indudablemente', r'\bindudablemente\b'),
        ('irrefutable',    r'\birrefutablemente?\b'),
        ('incuestionable', r'\bincuestionable(?:mente)?\b'),
    ],
}

# ═══════════════════════════════════════════════════════════════════
# LAYER-SPECIFIC ARTIFACT SIGNATURES (V6 Alignment)
# ═══════════════════════════════════════════════════════════════════

LAYER_TRIGGERS: Dict[str, list] = {
    'K1':  [r'K1\b', r'Katman\s*1\b', r'Layer\s*1\b', r'Persona', r'Formel\s+Mant[ıi]k', r'Formal\s+Logic'],
    'K2':  [r'K2\b', r'Katman\s*2\b', r'Layer\s*2\b', r'Yöntem\s+[İI]lkeleri', r'Felsefi\s+Metot', r'Philosophical\s+Method', r'Steelman', r'Falsification'],
    'K3':  [r'K3\b', r'Katman\s*3\b', r'Layer\s*3\b', r'Yap[ıi]sal\s+Güvence', r'Hermeneutic', r'Tutarl[ıi]l[ıi]k', r'Consistency'],
    'K4':  [r'K4\b', r'Katman\s*4\b', r'Layer\s*4\b', r'Nicel', r'Quantitative', r'Bayes', r'Statist'],
    'K5':  [r'K5\b', r'Katman\s*5\b', r'Layer\s*5\b', r'Deneysel', r'Experimental', r'Nedensellik', r'Causal'],
    'K6':  [r'K6\b', r'Katman\s*6\b', r'Layer\s*6\b', r'Sistematik\s+Derleme', r'Systematic\s+Review', r'Retorik', r'Rhetoric'],
    'K7':  [r'K7\b', r'Katman\s*7\b', r'Layer\s*7\b', r'A[çc][ıi]k\s+Bilim', r'Open\s+Science', r'Tekrar(?:lanabilirlik)?', r'Replicat'],
    'K8':  [r'K8\b', r'Katman\s*8\b', r'Layer\s*8\b', r'Tarihsel', r'Historical', r'Disciplinary\s+Matrix', r'Kaynak\s+Tenkit', r'Source\s+Criticism'],
    'K9':  [r'K9\b', r'Katman\s*9\b', r'Layer\s*9\b', r'Hesaplamal[ıi]', r'Computational', r'\bAI\b'],
    'K10': [r'K10\b', r'Katman\s*10\b', r'Layer\s*10\b', r'Karma[şs][ıi]kl[ıi]k', r'Complexity', r'Geni[şs]letilmi[şs]\s+Etik', r'Post-Mortem', r'Reporting'],
}

LAYER_ARTIFACTS: Dict[str, dict] = {
    'K1': {
        'name': 'Formal Logic / Persona',
        'markers': [r'(?:P[1-9]|Öncül|Premise|Sonuç|Conclusion|modus\s+ponens|modus\s+tollens|syllogism|k[ıi]yas|Persona)'],
        'desc': 'formal logic / persona markers',
    },
    'K4': {
        'name': 'Bayesian / Quantitative Statistics',
        'markers': [r'(?:P\s*\(|Bayes|posterior|prior|olasılık|probability|güven\s+aralığı|confidence\s+interval|p[\s-]?değer|p[\s-]?value|etki\s+büyüklüğü|effect\s+size)'],
        'desc': 'statistical/Bayesian markers (P(), confidence intervals, effect sizes)',
    },
    'K5': {
        'name': 'Causality & Experimental Design',
        'markers': [r'(?:nedensellik|causal|Bradford\s+Hill|DAG|confounder|karıştırıcı|mekanizma|mechanism|korelasyon.*nedensellik|correlation.*causation)'],
        'desc': 'causal analysis markers (Bradford Hill, DAG, confounders)',
    },
    'K8': {
        'name': 'Disciplinary Matrix & Source Criticism',
        'markers': [r'(?:KAYNAK\s+TENK[İI]T|SOURCE\s+CRITICISM|DI[ŞS]\s+TENK[İI]T|[İI][ÇC]\s+TENK[İI]T|CLAIMS?-SOURCE|D[İI]S[İI]PL[İI]NER\s+MATR[İI]S|DISCIPLINARY\s+MATRIX)'],
        'desc': 'source criticism section / disciplinary matrix',
        'requires_table': True,
        'table_patterns': [
            r'\|\s*.*?(?:Tez|İddia|Thesis|Claim|Evidence|Kanıt).*?\|.*?Source|Kaynak.*?\|',
            r'\|\s*.*?(?:Kaynak\s+Durumu|Source\s+Status|Data\s+Type|Epistemic\s+Weight).*?\|',
            r'\|\s*.*?(?:Metodolojik\s+Hüküm|Methodological\s+Verdict|Assessment).*?\|',
        ],
    },
}

PASSIVE_MARKERS = re.compile(
    r'(?:PAS[İI]F|DEAKT[İI]F|EXCLUDED|INACTIVE|D[IİI][ŞS]LANDI|hari[çc]|kapsam\s+d[ıi][şs][ıi]|⛔|❌)',
    re.IGNORECASE
)
ACTIVE_MARKERS = re.compile(
    r'(?:AKT[İI]F|ACTIVE|D[AÂ]H[İI]L|✅|☑)',
    re.IGNORECASE
)


# ═══════════════════════════════════════════════════════════════════
# DATA CLASSES
# ═══════════════════════════════════════════════════════════════════

@dataclass
class LintResult:
    """Structured validation result."""
    path: str
    lines: int
    chars: int
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
    detected_language: str = 'unknown'
    active_layers: List[str] = field(default_factory=list)
    passed: bool = False
    source_path: Optional[str] = None
    source_paragraphs: int = 0
    grounded: bool = False
    grounding_errors: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            'path': self.path,
            'filename': os.path.basename(self.path),
            'lines': self.lines,
            'chars': self.chars,
            'errors': self.errors,
            'warnings': self.warnings,
            'info': self.info,
            'detected_language': self.detected_language,
            'active_layers': self.active_layers,
            'passed': self.passed,
            'source_path': self.source_path,
            'source_paragraphs': self.source_paragraphs,
            'grounded': self.grounded,
            'error_count': len(self.errors),
            'warning_count': len(self.warnings),
            'timestamp': datetime.now(timezone.utc).isoformat(),
        }


@dataclass
class ParsedSection:
    """A markdown heading and its body content."""
    level: int
    title: str
    body: str
    line: int
    word_count: int


# ═══════════════════════════════════════════════════════════════════
# LINTER ENGINE
# ═══════════════════════════════════════════════════════════════════

class CrucibleLintError(Exception):
    """Raised for unrecoverable linter errors."""


class CrucibleLinter:
    """CRUCIBLE v7.0 Grounded Deterministic Epistemic Audit Linter.

    Instantiate with a file path and optional primary source document path,
    call validate(), then optionally compile_html().
    """

    def __init__(self, md_path: str, source_path: Optional[str] = None, strict: bool = False):
        self.md_path = os.path.abspath(md_path)
        self.source_path = os.path.abspath(source_path) if source_path else None
        self.strict = strict

        if not os.path.exists(self.md_path):
            raise FileNotFoundError(f"Target file not found: {self.md_path}")

        with open(self.md_path, 'r', encoding='utf-8') as f:
            self.lines: List[str] = f.readlines()
        self.full_text: str = "".join(self.lines)

        self.result = LintResult(
            path=self.md_path,
            lines=len(self.lines),
            chars=len(self.full_text),
            source_path=self.source_path,
        )

        self.sections: List[ParsedSection] = []
        self.triage_body: Optional[str] = None
        self.active_layers: Set[str] = set()

        self.source_paragraphs: List[str] = []
        self.source_full_text: str = ""
        if self.source_path:
            self.load_source()

    def load_source(self):
        """Loads primary source document (.docx, .txt, .md) for grounding verification."""
        if not os.path.exists(self.source_path):
            raise FileNotFoundError(f"Primary source file not found: {self.source_path}")

        ext = os.path.splitext(self.source_path)[1].lower()
        if ext == '.docx':
            if docx is not None:
                try:
                    doc = docx.Document(self.source_path)
                    self.source_paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
                    self.source_full_text = "\n".join(self.source_paragraphs)
                except Exception as e:
                    self._error(f"Failed to load .docx source: {e}")
            else:
                # Zero-dependency XML fallback for .docx
                import zipfile
                import xml.etree.ElementTree as ET
                try:
                    with zipfile.ZipFile(self.source_path) as z:
                        tree = ET.fromstring(z.read('word/document.xml'))
                    paras = []
                    for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                        texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
                        if texts:
                            paras.append(''.join(texts))
                    self.source_paragraphs = [p for p in paras if p.strip()]
                    self.source_full_text = "\n".join(self.source_paragraphs)
                except Exception as e:
                    self._error(f"Failed to load .docx source via XML fallback: {e}")
        else:
            # Text / Markdown / Plain formats
            try:
                with open(self.source_path, 'r', encoding='utf-8', errors='ignore') as f:
                    self.source_paragraphs = [line.strip() for line in f if line.strip()]
                    self.source_full_text = "\n".join(self.source_paragraphs)
            except Exception as e:
                self._error(f"Failed to load source text: {e}")

        self.result.source_path = self.source_path
        self.result.source_paragraphs = len(self.source_paragraphs)
        self._info(f"Loaded primary source: {os.path.basename(self.source_path)} ({len(self.source_paragraphs)} paragraphs, {len(self.source_full_text):,} chars)")

    # ── helpers ──

    def _error(self, msg: str):
        self.result.errors.append(msg)

    def _warn(self, msg: str):
        self.result.warnings.append(msg)

    def _info(self, msg: str):
        self.result.info.append(msg)

    def _find_nearest_heading_above(self, line_num: int) -> Optional[str]:
        """Return the nearest markdown heading text above *line_num* (1-indexed)."""
        for i in range(line_num - 2, -1, -1):
            if 0 <= i < len(self.lines) and self.lines[i].strip().startswith('#'):
                return self.lines[i].strip()
        return None

    # ── Phase 0: Structural Parse ──

    def parse_sections(self):
        """Extract heading-body pairs from the markdown text with hierarchy preservation."""
        heading_re = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        matches = list(heading_re.finditer(self.full_text))

        for i, m in enumerate(matches):
            current_level = len(m.group(1))
            body_start = m.end()
            # Hierarchical boundary: body continues until next heading of level <= current_level
            body_end = len(self.full_text)
            for j in range(i + 1, len(matches)):
                next_level = len(matches[j].group(1))
                if next_level <= current_level:
                    body_end = matches[j].start()
                    break

            body = self.full_text[body_start:body_end].strip()
            # Strip markdown formatting artifacts for word count
            clean_body = re.sub(r'[|#*\-_>`~\[\]\(\)]', ' ', body)
            word_count = len(clean_body.split())
            line_num = self.full_text[:m.start()].count('\n') + 1

            self.sections.append(ParsedSection(
                level=current_level,
                title=m.group(2).strip(),
                body=body,
                line=line_num,
                word_count=word_count,
            ))

    def detect_language(self) -> str:
        """Z6 fix: Content-based heuristic language detection."""
        scores: Dict[str, int] = {
            'tr': len(re.findall(r'\b(?:ve|bir|bu|ile|için|olan|ise|olarak|ancak|çünkü|değil|kadar|gibi)\b', self.full_text, re.IGNORECASE)),
            'en': len(re.findall(r'\b(?:the|and|is|are|this|that|which|with|from|but|not|has|have|was|were)\b', self.full_text, re.IGNORECASE)),
            'de': len(re.findall(r'\b(?:und|der|die|das|ist|ein|eine|für|mit|auf|nicht|auch|sich)\b', self.full_text, re.IGNORECASE)),
            'fr': len(re.findall(r'\b(?:et|le|la|les|est|un|une|des|pour|dans|pas|qui|que|sont)\b', self.full_text, re.IGNORECASE)),
            'es': len(re.findall(r'\b(?:el|la|los|las|es|un|una|del|por|con|que|no|se|como)\b', self.full_text, re.IGNORECASE)),
        }

        detected = max(scores, key=scores.get)  # type: ignore[arg-type]
        if scores[detected] < 10:
            detected = 'en'

        self.result.detected_language = detected
        self._info(f"Detected language: {detected} (tr={scores['tr']}, en={scores['en']}, de={scores['de']}, fr={scores['fr']}, es={scores['es']})")
        return detected

    # ── Phase 1: Payload & Core Sections ──

    def validate_payload(self):
        """Minimum payload check."""
        if self.result.lines < MIN_PAYLOAD_LINES or self.result.chars < MIN_PAYLOAD_CHARS:
            self._error(
                f"Payload Too Small: {self.result.lines} lines / {self.result.chars:,} chars. "
                f"Minimum: {MIN_PAYLOAD_LINES} lines / {MIN_PAYLOAD_CHARS:,} chars."
            )

    def validate_core_sections(self):
        """Z1 fix: Verify 5 core sections exist AS HEADINGS with substantive body."""
        for sec_def in CORE_SECTIONS:
            pattern = sec_def['pattern']
            min_words = sec_def.get('min_words', MIN_SECTION_WORDS)

            # Search in parsed headings
            found_section: Optional[ParsedSection] = None
            for sec in self.sections:
                if re.search(pattern, sec.title, re.IGNORECASE):
                    found_section = sec
                    break

            if found_section is None:
                # Fallback: present anywhere in text but not as heading
                if re.search(pattern, self.full_text, re.IGNORECASE):
                    self._warn(
                        f"'{sec_def['name_en']}' found in body text but NOT as a Markdown heading. "
                        f"Use '## [{sec_def['name_en']}]' for reliable validation."
                    )
                    if self.strict:
                        self._error(f"Missing Core Section Heading: '{sec_def['name_tr']} / {sec_def['name_en']}'")
                else:
                    self._error(f"Missing Core Section: '{sec_def['name_tr']} / {sec_def['name_en']}'")
                continue

            # Z1: Verify substantive body (not hollow)
            if found_section.word_count < min_words:
                self._error(
                    f"Hollow Section: '{sec_def['name_en']}' contains only "
                    f"{found_section.word_count} words (minimum: {min_words}). "
                    f"A section title without substantive analysis is not a valid audit component."
                )

        # Surgeon Checklist: actionable items check
        surgeon_pattern = CORE_SECTIONS[4]['pattern']
        for sec in self.sections:
            if re.search(surgeon_pattern, sec.title, re.IGNORECASE):
                actionable_re = re.compile(
                    r'(?:\[[\s_xX✓✗]?\]|☐|☑|✅|❌|\|.*?(?:Check|Action|Verify|Doğrulama|Denetim|Kontrol).*?\|)',
                    re.IGNORECASE
                )
                if not actionable_re.search(sec.body):
                    self._error(
                        "Surgeon Checklist lacks actionable items "
                        "(expected: '☐', '[ ]', '✅', or structured action table)."
                    )
                break

    # ── Phase 2: Triage & Layer Detection ──

    def validate_triage(self):
        """Z2 fix: Parse triage BODY (not heading) for active layers with robust discrimination."""
        triage_heading_re = re.compile(
            r'(?:EP[İI]STEMOLOJ[İI]K\s+TR[İI]YAJ|EPISTEMIC\s+TRIAGE)',
            re.IGNORECASE
        )

        # Find triage section from parsed sections
        for sec in self.sections:
            if triage_heading_re.search(sec.title):
                self.triage_body = sec.body  # Z2: body, not title
                break

        if self.triage_body is None:
            return

        active_block = False
        passive_block = False

        for line in self.triage_body.split('\n'):
            line_stripped = line.strip()
            if not line_stripped:
                continue

            if re.search(r'(?:aktif|active|d[aâ]hil)\s+katman|active\s+layer', line_stripped, re.IGNORECASE):
                active_block = True
                passive_block = False
            elif re.search(r'(?:pasif|passive|excluded|d[ıi][şs]lanan)\s+katman|excluded\s+layer', line_stripped, re.IGNORECASE):
                active_block = False
                passive_block = True

            line_passive = bool(PASSIVE_MARKERS.search(line_stripped)) or passive_block
            line_active = bool(ACTIVE_MARKERS.search(line_stripped)) or active_block

            for layer_id, triggers in LAYER_TRIGGERS.items():
                if any(re.search(trigger, line_stripped, re.IGNORECASE) for trigger in triggers):
                    if line_passive and not bool(ACTIVE_MARKERS.search(line_stripped)):
                        if layer_id in self.active_layers:
                            self.active_layers.remove(layer_id)
                    elif line_active:
                        self.active_layers.add(layer_id)

        self.result.active_layers = sorted(self.active_layers)
        self._info(f"Active layers: {', '.join(self.result.active_layers) or 'none detected'}")

    def validate_layer_artifacts(self):
        """Z4 fix: For active layers with known requirements, verify artifacts."""
        for layer_id in self.active_layers:
            if layer_id not in LAYER_ARTIFACTS:
                continue

            layer_def = LAYER_ARTIFACTS[layer_id]
            marker_found = any(
                re.search(mp, self.full_text, re.IGNORECASE)
                for mp in layer_def['markers']
            )

            if not marker_found:
                msg = (
                    f"Layer {layer_id} ({layer_def['name']}) is active in triage "
                    f"but no {layer_def['desc']} found in report."
                )
                self._error(msg) if self.strict else self._warn(msg)

            # K8: require claim-source table
            if layer_def.get('requires_table'):
                table_found = any(
                    re.search(tp, self.full_text, re.IGNORECASE)
                    for tp in layer_def['table_patterns']
                )
                if not table_found:
                    self._error(
                        f"Layer {layer_id} is active but required Claim-Source Audit Matrix "
                        f"(table with Thesis/Claim | Primary Source columns) not found!"
                    )
                else:
                    table_rows = re.findall(r'^\|(.+)\|$', self.full_text, re.MULTILINE)
                    has_wide_table = any(
                        len([c for c in row.split('|') if c.strip()]) >= 3
                        for row in table_rows
                    )
                    if not has_wide_table:
                        self._warn(
                            "Claim-Source table found but has fewer than 3 data columns. "
                            "Expected: | Thesis/Claim | Primary Source | Source Status | Verdict |"
                        )

    # ── Phase 3: Rhetorical Hygiene ──

    def scan_rhetoric(self):
        """Z3/Z4/Z5 fix: Expanded, per-line rhetorical scanning with proper scope."""
        scan_langs = {'tr', 'en'}
        lang = self.result.detected_language
        if lang in FORBIDDEN_TERMS:
            scan_langs.add(lang)

        all_terms = []
        for sl in scan_langs:
            for term_name, pattern in FORBIDDEN_TERMS.get(sl, []):
                all_terms.append((term_name, pattern, sl))

        in_code_block = False

        for idx, line in enumerate(self.lines, 1):
            stripped = line.strip()

            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            # Z3 fix: Per-line didactic context check
            if "|" in line:
                nearest_heading = self._find_nearest_heading_above(idx)
                if nearest_heading and re.search(
                    r'(?:Yasak\s+[İI]fade|Safsata|Forbidden|Fallacy|Didaktik|Didactic|Örnek|Example|Tenkit|Criticism|Hüküm|Verdict)',
                    nearest_heading, re.IGNORECASE
                ):
                    continue

            for term_name, pattern, term_lang in all_terms:
                if re.search(pattern, line, re.IGNORECASE):
                    self._warn(
                        f"Line {idx} [{term_lang.upper()}]: Forbidden dogmatic term "
                        f"'{term_name}' (Snippet: {stripped[:70]})"
                    )

    # ── Phase 4: Grounded Source Verification (v7.0) ──

    def validate_source_grounding(self):
        """CRUCIBLE v7.0: Grounded Verification against primary source document.
        Ensures zero-hallucination of primary source artifacts and verifies quoted anchors."""
        if not self.source_path or not self.source_full_text:
            self._info("Source grounding check skipped (no --source provided; running in unanchored mode).")
            return

        source_lower = self.source_full_text.lower()
        source_name = os.path.basename(self.source_path)
        external_marker_re = re.compile(
            r'\[\s*(?:DIŞ\s+KAYNAK|EXTERNAL\s+SOURCE|DIŞ\s+L[İI]TERATÜR|EXTERNAL)\b',
            re.IGNORECASE
        )

        # 1. Parse and verify Claim-Source Audit Matrix (K8 table)
        table_rows = re.findall(r'^\|(.+)\|$', self.full_text, re.MULTILINE)
        in_matrix = False
        matrix_rows = []

        for row in table_rows:
            cols = [c.strip() for c in row.split('|')]
            if len(cols) < 3:
                continue
            # Header check
            if any(re.search(r'(?:Tez|İddia|Thesis|Claim)', c, re.IGNORECASE) for c in cols) and \
               any(re.search(r'(?:Kaynak|Source)', c, re.IGNORECASE) for c in cols):
                in_matrix = True
                continue
            if in_matrix:
                if re.match(r'^[\s:\-]+$', cols[0]):
                    continue
                if cols[0].startswith('#') or len(cols) < 2:
                    in_matrix = False
                    continue
                matrix_rows.append(cols)

        stop_words = {
            'yazıtı', 'yazıt', 'kitabesi', 'kitabe', 'grubu', 'parşömeni', 'fragmanı',
            'fragmanları', 'belgesi', 'belgeleri', 'mektubu', 'mektupları', 'arşivi',
            'serisi', 'parçası', 'parçaları', 'nüshası', 'yazması', 'mushafı', 'sikkeleri',
            'sikkesi', 'dinarı', 'dirhemi', 'yazısı', 'metni', 'metinleri', 'örneği',
            'ölçümü', 'tarihli', 'tarihi', 'bölümü', 'erken', 'dönem', 'hicri', 'miladi',
            've', 'ile', 'veya', 'and', 'with', 'from', 'group', 'dated',
            'inscription', 'manuscript', 'fragment', 'document', 'archive', 'series',
            'coin', 'coins', 'text', 'texts', 'codex', 'palimpsest', 'source', 'primary'
        }

        for cols in matrix_rows:
            source_col = cols[1] if len(cols) > 1 else ""
            if not source_col:
                continue

            # Check if explicitly exempted as external comparison
            if external_marker_re.search(source_col) or external_marker_re.search(cols[0]):
                self._info(f"External literature artifact exempted: '{source_col[:45]}'")
                continue

            clean_source = re.sub(r'\[P:\d+\]', '', source_col)
            clean_source = re.sub(r'[*_`]', '', clean_source)
            sub_artifacts = [s.strip() for s in re.split(r'[,;]|\bve\b|\band\b', clean_source) if s.strip()]

            for artifact in sub_artifacts:
                artifact_clean = re.sub(r'\(.*?\)', '', artifact).strip()
                tokens = [t.strip('().,;:"\'') for t in artifact_clean.split()]
                candidate_tokens = [
                    t for t in tokens
                    if len(t) >= 3 and t.lower() not in stop_words and not re.match(r'^[0-9\-/]+$', t)
                ]

                if not candidate_tokens:
                    continue

                found = False
                if len(artifact_clean) <= 40 and artifact_clean.lower() in source_lower:
                    found = True
                else:
                    for tok in candidate_tokens:
                        tok_re = rf'(?<![{_TR_ALPHA}]){re.escape(tok.lower())}(?![{_TR_ALPHA}])'
                        if re.search(tok_re, source_lower):
                            found = True
                            break

                if not found:
                    self._error(
                        f"[FAIL: UNGROUNDED ARTIFACT] Primary source artifact '{artifact}' "
                        f"(in matrix: '{source_col[:50]}') was NOT found in source document '{source_name}'. "
                        f"If this is an external comparison, prefix with '[DIŞ KAYNAK]' or '[EXTERNAL]'."
                    )

        # 2. Check Paragraph Citations [P:xxxx]
        citations = re.findall(r'\[P:(\d+)\]', self.full_text)
        max_para = len(self.source_paragraphs)

        for p_str in set(citations):
            p_idx = int(p_str)
            if max_para > 0 and p_idx >= max_para:
                self._warn(
                    f"Citation [P:{p_idx}] exceeds source paragraph count ({max_para}) of '{source_name}'."
                )

        # 3. Check Verbatim Quotes attached to [P:xxxx]
        quote_matches = re.finditer(
            r'\[P:(\d+)\]\s*(?:[:\-]\s*)?(?:[\*_]{1,2})?["“\']([^"”\']{20,150})["”\']',
            self.full_text
        )
        for qm in quote_matches:
            p_num = int(qm.group(1))
            quoted_str = qm.group(2).strip()
            norm_quote = re.sub(r'\s+', ' ', quoted_str).lower()

            if norm_quote not in source_lower:
                short_snippet = norm_quote[:35]
                if short_snippet not in source_lower:
                    self._error(
                        f"[FAIL: UNVERIFIED QUOTE] Quoted text attached to [P:{p_num}] not found in '{source_name}': "
                        f'"{quoted_str[:60]}..."'
                    )
                else:
                    self._info(f"Verified partial quote anchor for [P:{p_num}].")
            else:
                self._info(f"Verified verbatim quote anchor for [P:{p_num}].")

        if len(self.result.errors) == 0:
            self.result.grounded = True
            self._info("Source Grounding Verification: 100% PASS (Zero ungrounded artifacts).")

    # ── Orchestrator ──

    def validate(self) -> LintResult:
        """Run all validation phases and return the result."""
        self.parse_sections()
        self.detect_language()
        self.validate_payload()
        self.validate_core_sections()
        self.validate_triage()
        self.validate_layer_artifacts()
        self.scan_rhetoric()
        self.validate_source_grounding()

        self.result.passed = len(self.result.errors) == 0
        return self.result

    # ── HTML Compilation ──

    def compile_html(self) -> Optional[str]:
        """Compile verified markdown to styled HTML with verification seal."""
        if markdown is None:
            raise CrucibleLintError(
                "HTML compilation requires the 'markdown' package. "
                "Install: pip install markdown"
            )

        if not self.result.passed:
            return None

        render_text = self._convert_latex_to_unicode(self.full_text)
        html_body = markdown.markdown(render_text, extensions=['tables', 'fenced_code', 'nl2br'])

        content_hash = hashlib.sha256(self.full_text.encode('utf-8')).hexdigest()[:16]
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        lang_code = self.result.detected_language if self.result.detected_language in ('tr', 'en', 'de', 'fr', 'es') else 'en'

        seal_html = self._build_seal_html(content_hash, timestamp, lang_code)
        styled_html = self._build_full_html(lang_code, html_body, seal_html)

        html_output_path = os.path.splitext(self.md_path)[0] + ".html"
        with open(html_output_path, 'w', encoding='utf-8') as f:
            f.write(styled_html)

        return html_output_path

    # ── LaTeX to Unicode ──

    @staticmethod
    def _convert_latex_to_unicode(text: str) -> str:
        """Convert known LaTeX patterns to Unicode.
        Z10 fix: specific patterns first, catch-all only for non-LaTeX $...$."""
        subscripts = {str(i): chr(0x2080 + i) for i in range(10)}

        # Bayes (most complex first)
        text = re.sub(
            r'\$\s*P\s*\(\s*H_([0-9])\s*(?:\\?\|)\s*E\s*\)\s*=\s*(?:\\?%|%)?'
            r'\s*([0-9.,]+)%?\s*\$',
            lambda m: 'P(H' + subscripts.get(m.group(1), m.group(1)) + '|E) = %' + m.group(2),
            text)
        text = re.sub(
            r'\$\s*P\s*\(\s*H_([0-9])\s*(?:\\?\|)\s*E\s*\)\s*\$',
            lambda m: 'P(H' + subscripts.get(m.group(1), m.group(1)) + '|E)',
            text)

        # Arrows (compound before simple)
        for pat, repl in [
            (r'\$\s*\\Uparrow\s*\\Uparrow\s*/\s*\\Downarrow\s*\\Downarrow\s*\$', '⇑⇑ / ⇓⇓'),
            (r'\$\s*\\Uparrow\s*\\Uparrow\s*\$', '⇑⇑'),
            (r'\$\s*\\Downarrow\s*\\Downarrow\s*\$', '⇓⇓'),
            (r'\$\s*\\Uparrow\s*\$', '⇑'),
            (r'\$\s*\\Downarrow\s*\$', '⇓'),
            (r'\$\s*\\rightarrow\s*\$', '→'),
            (r'\$\s*\\leftarrow\s*\$', '←'),
            (r'\$\s*\\Rightarrow\s*\$', '⇒'),
        ]:
            text = re.sub(pat, repl, text)

        # Hypothesis subscripts
        text = re.sub(r'\$H_([0-9])\$',
                      lambda m: 'H' + subscripts.get(m.group(1), m.group(1)), text)

        # Math operators
        for pat, repl in [
            (r'\$\s*\\approx\s*([0-9.,]+)\s*\$', r'≈ \1'),
            (r'\$\s*\\neq\s*\$', '≠'),
            (r'\$\s*\\leq?\s*\$', '≤'),
            (r'\$\s*\\geq?\s*\$', '≥'),
            (r'\$\s*\\pm\s*\$', '±'),
        ]:
            text = re.sub(pat, repl, text)

        text = re.sub(r'\\approx', '≈', text)
        text = re.sub(r'\\neq', '≠', text)

        # Degrees
        text = re.sub(r'\$\s*([0-9]+)\s*\^\{?\\circ\}?\s*\$', r'\1°', text)

        # Greek letters
        for g_code, g_char in {'\\alpha': 'α', '\\beta': 'β', '\\gamma': 'γ', '\\delta': 'δ',
                                '\\theta': 'θ', '\\sigma': 'σ', '\\mu': 'μ', '\\lambda': 'λ',
                                '\\pi': 'π', '\\epsilon': 'ε', '\\omega': 'ω'}.items():
            text = re.sub(r'\$\s*([+-]?)\s*' + re.escape(g_code) + r'\s*\$',
                          r'\1' + g_char, text)

        # Z10: Catch-all — ONLY $simple_text$ with NO backslashes
        text = re.sub(r'\$([a-zA-Z0-9_ -]+)\$', r'<em>\1</em>', text)

        # Remaining bare commands
        for cmd, char in [('\\rightarrow', '→'), ('\\Downarrow', '⇓'), ('\\Uparrow', '⇑')]:
            text = text.replace(cmd, char)

        return text

    # ── HTML Templates ──

    def _build_seal_html(self, content_hash: str, timestamp: str, lang_code: str = 'en') -> str:
        wc = len(self.result.warnings)
        layers_text = ', '.join(self.result.active_layers) or ('Yok / Bulunamadı' if lang_code == 'tr' else 'N/A')
        src_name = os.path.basename(self.result.source_path) if self.result.source_path else None

        if lang_code == 'tr':
            w_text = "Temiz (0 terim)" if wc == 0 else f"{wc} uyarı"
            ground_box = f"<div><strong>Zemin Kaynak (Ground Truth):</strong> <code>{src_name}</code> ({self.result.source_paragraphs} paragraf)</div><div><strong>Zemin Doğrulama:</strong> Sıfır Hayalet Referans (Doğrulandı)</div>" if src_name else "<div><strong>Zemin Doğrulama:</strong> Çıpasız Mod (Kaynak belirtilmedi)</div>"
            return f"""
    <div style="background:#0f172a;color:#f8fafc;border:2px solid #10b981;border-radius:8px;padding:18px 24px;margin-bottom:35px;box-shadow:0 4px 6px -1px rgba(0,0,0,.12)">
        <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #334155;padding-bottom:10px;margin-bottom:12px;flex-wrap:wrap;gap:10px">
            <span style="font-weight:700;color:#34d399;font-size:1.1em;letter-spacing:.5px">🛡️ MAYIN TARLASI V7.0 — ZEMİN ÇIPALI DETERMINİSTİK DOĞRULAMA MÜHRÜ</span>
            <span style="background:#059669;color:#fff;padding:4px 12px;border-radius:4px;font-weight:700;font-size:.9em">[PASS] ANAYASAL UYUMLULUK ONAYLANDI (V7.0 ZEMİN ÇIPALI)</span>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;font-size:.9em;color:#cbd5e1">
            <div><strong>Doğrulayıcı:</strong> <code>crucible_linter.py v7.0</code></div>
            <div><strong>Yük (Payload):</strong> {self.result.lines} satır | {self.result.chars:,} karakter</div>
            <div><strong>Retorik Hijyen:</strong> {w_text}</div>
            <div><strong>Aktif Katmanlar:</strong> {layers_text}</div>
            {ground_box}
            <div><strong>İçerik Özeti (SHA-256):</strong> <code>sha256:{content_hash}</code></div>
            <div><strong>Doğrulama Zamanı:</strong> {timestamp}</div>
        </div>
        <div style="margin-top:10px;font-size:.82em;color:#94a3b8;border-top:1px dashed #334155;padding-top:8px">
            Deterministik Doğrulama Damgası (v7.0) — Başlık analizi, anayasal regex süzgeci ve zemin metin çapraz doğrulamasıyla onaylanmış Markdown metninden derlenmiştir. Doğrulanmamış taslaklar bu mührü taşıyamaz.
        </div>
    </div>"""

        w_text = "Clean (0 terms)" if wc == 0 else f"{wc} warning(s)"
        ground_box = f"<div><strong>Ground Truth Source:</strong> <code>{src_name}</code> ({self.result.source_paragraphs} paras)</div><div><strong>Artifact Grounding:</strong> Zero Phantom References (Verified)</div>" if src_name else "<div><strong>Artifact Grounding:</strong> Unanchored Mode (No source provided)</div>"
        return f"""
    <div style="background:#0f172a;color:#f8fafc;border:2px solid #10b981;border-radius:8px;padding:18px 24px;margin-bottom:35px;box-shadow:0 4px 6px -1px rgba(0,0,0,.12)">
        <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #334155;padding-bottom:10px;margin-bottom:12px;flex-wrap:wrap;gap:10px">
            <span style="font-weight:700;color:#34d399;font-size:1.1em;letter-spacing:.5px">🛡️ CRUCIBLE v7.0 — GROUNDED DETERMINISTIC VERIFICATION SEAL</span>
            <span style="background:#059669;color:#fff;padding:4px 12px;border-radius:4px;font-weight:700;font-size:.9em">[PASS] CONSTITUTIONAL COMPLIANCE (V7.0 GROUNDED)</span>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;font-size:.9em;color:#cbd5e1">
            <div><strong>Validator:</strong> <code>crucible_linter.py v7.0</code></div>
            <div><strong>Payload:</strong> {self.result.lines} lines | {self.result.chars:,} chars</div>
            <div><strong>Rhetorical Hygiene:</strong> {w_text}</div>
            <div><strong>Active Layers:</strong> {layers_text}</div>
            {ground_box}
            <div><strong>Content Hash:</strong> <code>sha256:{content_hash}</code></div>
            <div><strong>Verified:</strong> {timestamp}</div>
        </div>
        <div style="margin-top:10px;font-size:.82em;color:#94a3b8;border-top:1px dashed #334155;padding-top:8px">
            Deterministic Verification Stamp (v7.0) — compiled from verified Markdown via structural heading analysis, regex constraints, and primary source cross-checking. Unverified drafts lack this seal.
        </div>
    </div>"""

    def _build_full_html(self, lang_code: str, html_body: str, seal_html: str) -> str:
        title_prefix = "Mayın Tarlası V7.0" if lang_code == "tr" else "CRUCIBLE v7.0"
        return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="utf-8">
    <title>{title_prefix} — {os.path.basename(self.md_path)}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
               line-height: 1.8; max-width: 960px; margin: 40px auto; padding: 35px; color: #1e293b; background-color: #f8fafc; }}
        h1, h2, h3, h4 {{ color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 1.6em; }}
        h1 {{ text-align: center; font-size: 2.2em; border-bottom: 3px solid #cbd5e1; padding-bottom: 15px; color: #091e42; }}
        pre {{ background: #0f172a; color: #f8fafc; padding: 18px; border-radius: 8px; overflow-x: auto;
               font-family: 'Consolas', 'Courier New', monospace; font-size: 0.9em; }}
        pre code {{ background: transparent !important; color: inherit !important; padding: 0 !important;
                    border-radius: 0 !important; font-size: inherit !important; }}
        code {{ background: #e2e8f0; color: #0f172a; padding: 2px 6px; border-radius: 4px;
                font-family: 'Consolas', 'Courier New', monospace; font-size: 0.9em; }}
        table {{ border-collapse: collapse; width: 100%; margin: 25px 0; font-size: 0.92em; background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,.05); }}
        th, td {{ border: 1px solid #cbd5e1; padding: 12px 14px; text-align: left; }}
        th {{ background-color: #1e293b; color: #fff; font-weight: 600; }}
        tr:nth-child(even) {{ background-color: #f1f5f9; }}
        strong {{ color: #991b1b; }}
        hr {{ border: 0; height: 1px; background: #cbd5e1; margin: 35px 0; }}
        .surgeon-card, .cerrah-card {{ background-color: #f0fdf4; border-left: 5px solid #16a34a; padding: 20px; margin: 30px 0; border-radius: 4px; }}
    </style>
    <script>window.MathJax = {{ tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }} }};</script>
    <script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    {seal_html}
    {html_body}
</body>
</html>"""


# ═══════════════════════════════════════════════════════════════════
# TERMINAL REPORT
# ═══════════════════════════════════════════════════════════════════

def print_report(result: LintResult):
    """Print a formatted terminal report."""
    print("=" * 72)
    print("🔍 CRUCIBLE v7.0 — GROUNDED DETERMINISTIC AUDIT & LINTER PIPELINE")
    print(f"📄 Target: {os.path.basename(result.path)}")
    print(f"📊 Lines: {result.lines} | Characters: {result.chars:,}")
    print(f"🌐 Language: {result.detected_language.upper()}")
    if result.active_layers:
        print(f"🧬 Active Layers: {', '.join(result.active_layers)}")
    if result.source_path:
        print(f"⚓ Primary Source: {os.path.basename(result.source_path)} ({result.source_paragraphs} paragraphs)")
        print(f"🛡️ Grounding: {'✅ GROUNDED (Zero Phantom Artifacts)' if result.grounded else '❌ UNGROUNDED / UNVERIFIED'}")
    else:
        print("⚓ Primary Source: None (Unanchored Mode)")
    print("-" * 72)

    if result.errors:
        print(f"❌ [FAIL] {len(result.errors)} METHODOLOGICAL DEFICIENC{'Y' if len(result.errors) == 1 else 'IES'} DETECTED:")
        for err in result.errors:
            print(f"   • {err}")
    else:
        print("✅ [PASS] All Core Sections, Triage, and Layer Requirements Verified.")

    if result.warnings:
        print(f"\n⚠️  [WARNINGS] ({len(result.warnings)}):")
        for wrn in result.warnings:
            print(f"   • {wrn}")
    else:
        print("✅ [CLEAN RHETORIC] Zero dogmatic or polemical terms detected.")

    print("=" * 72)

    if not result.passed:
        print("⛔ HTML COMPILATION ABORTED. Resolve deficiencies above.")


# ═══════════════════════════════════════════════════════════════════
# CLI ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='CRUCIBLE v7.0 — Grounded Deterministic Epistemic Audit Linter',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python crucible_linter.py report.md
  python crucible_linter.py report.md --source document.docx
  python crucible_linter.py report.md --source document.docx --strict
  python crucible_linter.py report.md --json
  python crucible_linter.py report.md --source document.docx --json -o results.json
  python crucible_linter.py report.md --no-html
        """,
    )
    parser.add_argument('target', help='Path to the Markdown report to validate')
    parser.add_argument('--source', metavar='PATH', default=None,
                        help='Path to primary source document (.docx, .txt, .md) for ground-truth verification')
    parser.add_argument('--strict', action='store_true',
                        help='Treat layer-artifact warnings as hard errors')
    parser.add_argument('--json', action='store_true',
                        help='Output structured JSON results')
    parser.add_argument('-o', '--output', metavar='PATH',
                        help='Write JSON results to file (requires --json)')
    parser.add_argument('--no-html', action='store_true',
                        help='Skip HTML compilation even on PASS')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Suppress terminal report (use with --json)')

    args = parser.parse_args()

    try:
        linter = CrucibleLinter(args.target, source_path=args.source, strict=args.strict)
        result = linter.validate()
    except FileNotFoundError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

    if not args.quiet:
        print_report(result)

    if args.json:
        json_str = json.dumps(result.to_dict(), indent=2, ensure_ascii=False)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(json_str)
            if not args.quiet:
                print(f"\n📁 JSON results written to: {args.output}")
        elif args.quiet:
            print(json_str)

    if result.passed and not args.no_html:
        try:
            html_path = linter.compile_html()
            if html_path and not args.quiet:
                print(f"🎉 [SUCCESS] HTML Report Compiled: {os.path.basename(html_path)}")
        except CrucibleLintError as e:
            print(f"⚠️  {e}", file=sys.stderr)

    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
