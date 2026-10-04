import os
import sys
import re
import markdown

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def validate_and_convert(md_path):
    if not os.path.exists(md_path):
        print(f"[ERROR] Target file not found: {md_path}")
        sys.exit(1)

    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    full_text = "".join(lines)

    errors = []
    warnings = []

    # 1. CORE SECTION INTEGRITY
    required_sections = [
        ("EPİSTEMOLOJİK TRİYAJ / EPISTEMIC TRIAGE", r"\[(EP[İI]STEMOLOJ[İI]K\s+TR[İI]YAJ|EPISTEMIC\s+TRIAGE)\]"),
        ("ÇELİK ADAM (STEELMANNING)", r"(ÇEL[İI]K\s+ADAM|STEELMANNING)"),
        ("OTO-FALSİFİKASYON / AUTO-FALSIFICATION", r"(OTO-FALS[İI]F[İI]KASYON|B[İI]L[İI][ŞS]SEL\s+ÖZ-DENET[İI]M|AUTO-FALSIFICATION)"),
        ("HASAR RAPORU / EPISTEMIC TOLL", r"(HASAR\s+RAPORU|ASGAR[İI]\s+EP[İI]STEM[İI]K\s+BEDEL|DAMAGE\s+REPORT|EPISTEMIC\s+TOLL)"),
        ("CERRAH DENETİM KARTI / SURGEON CHECKLIST", r"(CERRAH\s+(DENET[İI]M\s+)?KART|SURGEON('S)?\s+(AUDIT\s+)?(CARD|CHECKLIST))")
    ]

    for section_name, pattern in required_sections:
        if not re.search(pattern, full_text, re.IGNORECASE):
            errors.append(f"Missing Required Core Section: '{section_name}'")

    # 2. DYNAMIC TRIAGE VERIFICATION
    # If Historical Textual Criticism (Layer 8) is active, require evidentiary table
    triyaj_match = re.search(r"##\s*\[(EP[İI]STEMOLOJ[İI]K\s+TR[İI]YAJ|EPISTEMIC\s+TRIAGE)\](.*?)(?=(\n#[^#]|\Z))", full_text, re.DOTALL | re.IGNORECASE)
    if triyaj_match:
        triyaj_content = triyaj_match.group(1)
        if "K8" in triyaj_content or "Katman 8" in triyaj_content or "Layer 8" in triyaj_content or "Tarihsel" in triyaj_content or "Historical" in triyaj_content:
            if not re.search(r"(KAYNAK\s+TENK[İI]T|SOURCE\s+CRITICISM|DI[ŞS]\s+TENK[İI]T|[İI][ÇC]\s+TENK[İI]T)", full_text, re.IGNORECASE):
                errors.append("Layer 8 is active in triage, but 'Source Criticism' section is missing!")
            if not (re.search(r"\|\s*.*?Tez\s*/\s*İddia.*?\|\s*.*?Dayandığı\s+Temel\s+Kaynak.*?\|", full_text, re.IGNORECASE) or 
                    re.search(r"\|\s*.*?Thesis\s*/\s*Claim.*?\|\s*.*?Primary\s+Source.*?\|", full_text, re.IGNORECASE) or
                    re.search(r"\|\s*.*?Kaynak\s+Durumu.*?\|", full_text, re.IGNORECASE) or
                    re.search(r"\|\s*.*?Source\s+Status.*?\|", full_text, re.IGNORECASE)):
                errors.append("Layer 8 is active, but required Claim-Source Audit Matrix (Table) was not found under Section 2.1!")

    # 3. RHETORICAL HYGIENE (Forbidden Dogmatic & Sycophantic Terms)
    forbidden_terms = [
        ("şüphesiz", r"\b[şs]üphesiz\b"),
        ("tartışmasızdır", r"\btart[ıi][şs]mas[ıi]zd[ıi]r\b"),
        ("kesinlikle kanıtlanmıştır", r"\bkesinlikle\s+kan[ıi]tlanm[ıi][şs]t[ıi]r\b"),
        ("entelektüel sahtekarlık", r"\bentelektüel\s+sahtekarl[ıi]k\b"),
        ("infaz", r"\b[iıİI]nfaz\b"),
        ("undoubtedly", r"\bundoubtedly\b"),
        ("indisputable", r"\bindisputable\b"),
        ("absolutely proven", r"\babsolutely\s+proven\b")
    ]

    in_code_block = False
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        for term, pattern in forbidden_terms:
            if re.search(pattern, line, re.IGNORECASE):
                if "|" in line and ("Yasak İfade" in full_text or "Safsata" in full_text or "Forbidden" in full_text):
                    continue
                warnings.append(f"Line {idx}: Forbidden dogmatic/polemical term detected -> '{term}' (Snippet: {line.strip()[:60]}...)")

    # 4. PRINT REPORT
    print("=" * 72)
    print("🔍 CRUCIBLE v6.0 — AUDIT & LINTER PIPELINE")
    print(f"📄 Target: {os.path.basename(md_path)}")
    print(f"📊 Lines: {len(lines)} | Characters: {len(full_text)}")
    print("-" * 72)

    if errors:
        print("❌ [FAIL] METHODOLOGICAL DEFICIENCIES DETECTED:")
        for err in errors:
            print(f"   • {err}")
    else:
        print("✅ [PASS] All Universal Core & Triage Requirements Verified.")

    if warnings:
        print("\n⚠️ [RHETORICAL WARNINGS]:")
        for wrn in warnings:
            print(f"   • {wrn}")
    else:
        print("✅ [CLEAN RHETORIC] Zero dogmatic or polemical terms detected.")

    print("=" * 72)

    if errors:
        print("⛔ HTML COMPILATION ABORTED. Resolve the methodological deficiencies above.")
        sys.exit(1)

    # 5. HTML COMPILATION
    html_output_path = os.path.splitext(md_path)[0] + ".html"

    # LaTeX & Math/Logic Clean Unicode Conversions
    subscripts = {'0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'}
    render_text = full_text

    render_text = re.sub(r'\$\s*\\Uparrow\s*\\Uparrow\s*\$', '⇑⇑', render_text)
    render_text = re.sub(r'\$\s*\\Downarrow\s*\\Downarrow\s*\$', '⇓⇓', render_text)
    render_text = re.sub(r'\$\s*\\Uparrow\s*\\Uparrow\s*/\s*\\Downarrow\s*\\Downarrow\s*\$', '⇑⇑ / ⇓⇓', render_text)
    render_text = re.sub(r'\$\s*\\Uparrow\s*\$', '⇑', render_text)
    render_text = re.sub(r'\$\s*\\Downarrow\s*\$', '⇓', render_text)
    render_text = re.sub(r'\$\s*\\rightarrow\s*\$', '→', render_text)
    render_text = re.sub(r'\$\s*\\leftarrow\s*\$', '←', render_text)
    render_text = re.sub(r'\$\s*\\Rightarrow\s*\$', '⇒', render_text)

    render_text = re.sub(r'\$H_([0-9])\$', lambda m: 'H' + subscripts.get(m.group(1), m.group(1)), render_text)
    render_text = re.sub(r'\$\s*\\approx\s*([0-9.,]+)\s*\$', r'≈ \1', render_text)
    render_text = re.sub(r'\$\s*\\approx\s*', '≈ ', render_text)
    render_text = re.sub(r'\\approx', '≈', render_text)
    render_text = re.sub(r'\$\s*\\neq\s*\$', '≠', render_text)
    render_text = re.sub(r'\\neq', '≠', render_text)
    render_text = re.sub(r'\$\s*\\le(q)?\s*\$', '≤', render_text)
    render_text = re.sub(r'\$\s*\\ge(q)?\s*\$', '≥', render_text)
    render_text = re.sub(r'\$\s*\\pm\s*\$', '±', render_text)

    render_text = re.sub(r'\$\s*([0-9]+)\s*\^\\circ\s*\$', r'\1°', render_text)
    render_text = re.sub(r'\$\s*([0-9]+)\s*\^\{\\circ\}\s*\$', r'\1°', render_text)
    render_text = re.sub(r'([0-9]+)\s*\^\\circ', r'\1°', render_text)

    greek = {'\\alpha': 'α', '\\beta': 'β', '\\gamma': 'γ', '\\theta': 'θ', '\\sigma': 'σ'}
    for g_code, g_char in greek.items():
        render_text = re.sub(r'\$\s*([+-]?)\s*' + re.escape(g_code) + r'\s*\$', r'\1' + g_char, render_text)

    render_text = re.sub(r'\$\s*P\s*\(\s*H_([0-9])\s*(?:\\\||\|)\s*E\s*\)\s*=\s*(?:\\%|%)?\s*([0-9.,]+)%?\s*\$',
                         lambda m: 'P(H' + subscripts.get(m.group(1), m.group(1)) + '|E) = %' + m.group(2), render_text)
    render_text = re.sub(r'\$\s*P\s*\(\s*H_([0-9])\s*(?:\\\||\|)\s*E\s*\)\s*\$',
                         lambda m: 'P(H' + subscripts.get(m.group(1), m.group(1)) + '|E)', render_text)

    render_text = re.sub(r'\$([a-zA-Z0-9_ -]+)\$', r'<em>\1</em>', render_text)
    render_text = re.sub(r'\\rightarrow', '→', render_text)
    render_text = re.sub(r'\\Downarrow', '⇓', render_text)
    render_text = re.sub(r'\\Uparrow', '⇑', render_text)

    html_body = markdown.markdown(render_text, extensions=['tables', 'fenced_code', 'nl2br'])

    styled_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>CRUCIBLE v6.0 — {os.path.basename(md_path)}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.8;
            max-width: 960px;
            margin: 40px auto;
            padding: 35px;
            color: #1e293b;
            background-color: #f8fafc;
        }}
        h1, h2, h3, h4 {{
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 8px;
            margin-top: 1.6em;
        }}
        h1 {{
            text-align: center;
            font-size: 2.2em;
            border-bottom: 3px solid #cbd5e1;
            padding-bottom: 15px;
            color: #091e42;
        }}
        pre {{
            background: #0f172a;
            color: #f8fafc;
            padding: 18px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre code {{
            background: transparent !important;
            color: inherit !important;
            padding: 0 !important;
            border-radius: 0 !important;
            font-size: inherit !important;
        }}
        code {{
            background: #e2e8f0;
            color: #0f172a;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.9em;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 25px 0;
            font-size: 0.92em;
            background: #ffffff;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        th, td {{
            border: 1px solid #cbd5e1;
            padding: 12px 14px;
            text-align: left;
        }}
        th {{
            background-color: #1e293b;
            color: #ffffff;
            font-weight: 600;
        }}
        tr:nth-child(even) {{
            background-color: #f1f5f9;
        }}
        strong {{
            color: #991b1b;
        }}
        hr {{
            border: 0;
            height: 1px;
            background: #cbd5e1;
            margin: 35px 0;
        }}
        .surgeon-card, .cerrah-card {{
            background-color: #f0fdf4;
            border-left: 5px solid #16a34a;
            padding: 20px;
            margin: 30px 0;
            border-radius: 4px;
        }}
    </style>
    <script>
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]
            }}
        }};
    </script>
    <script type="text/javascript" id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
</head>
<body>
    {html_body}
</body>
</html>"""

    with open(html_output_path, 'w', encoding='utf-8') as f:
        f.write(styled_html)

    print(f"🎉 [SUCCESS] HTML Report Compiled: {os.path.basename(html_output_path)}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crucible_linter.py <path_to_report.md>")
        sys.exit(1)
    validate_and_convert(sys.argv[1])
