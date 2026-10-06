import markdown
import os

md_path = os.path.join(os.path.dirname(__file__), "..", "docs", "CRUCIBLE_v6_Whitepaper.md")
html_path = os.path.join(os.path.dirname(__file__), "..", "docs", "CRUCIBLE_v6_Whitepaper.html")

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

html_body = markdown.markdown(text, extensions=["tables", "fenced_code"])

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUCIBLE v6.0 Whitepaper</title>
    <style>
        body {
            font-family: 'Georgia', 'Cambria', 'Times New Roman', serif;
            line-height: 1.7;
            color: #0f172a;
            background-color: #f1f5f9;
            margin: 0;
            padding: 40px 15px;
        }
        .container {
            max-width: 920px;
            margin: auto;
            background: #ffffff;
            padding: 60px 75px;
            border-radius: 8px;
            box-shadow: 0 4px 25px rgba(0,0,0,0.06);
            border: 1px solid #e2e8f0;
        }
        h1 {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
            color: #020617;
            font-size: 2.1rem;
            line-height: 1.25;
            border-bottom: 2px solid #0f172a;
            padding-bottom: 15px;
            margin-top: 0;
            letter-spacing: -0.02em;
        }
        h2 {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
            color: #0f172a;
            font-size: 1.45rem;
            margin-top: 40px;
            border-bottom: 1px solid #cbd5e1;
            padding-bottom: 8px;
            letter-spacing: -0.01em;
        }
        h3 {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
            color: #1e293b;
            font-size: 1.15rem;
            margin-top: 25px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.90rem;
        }
        th, td {
            border: 1px solid #cbd5e1;
            padding: 10px 12px;
            text-align: left;
        }
        th {
            background-color: #0f172a;
            color: #ffffff;
            font-weight: 600;
        }
        tr:nth-child(even) {
            background-color: #f8fafc;
        }
        pre {
            background-color: #0f172a;
            color: #f8fafc;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 0.88rem;
        }
        code {
            background-color: #f1f5f9;
            color: #991b1b;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: Consolas, 'Courier New', monospace;
            font-size: 0.9em;
        }
        pre code {
            background-color: transparent;
            color: inherit;
            padding: 0;
        }
        blockquote {
            border-left: 4px solid #0f172a;
            margin: 20px 0;
            padding: 10px 20px;
            background-color: #f8fafc;
            font-style: italic;
        }
        hr {
            border: 0;
            height: 1px;
            background: #cbd5e1;
            margin: 35px 0;
        }
        @media print {
            body { padding: 0; background: #fff; }
            .container { box-shadow: none; border: none; padding: 0; max-width: 100%; }
        }
    </style>
    <script>
        window.MathJax = {
            tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }
        };
    </script>
    <script type="text/javascript" id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
</head>
<body>
    <div class="container">
        __BODY__
    </div>
</body>
</html>"""

final_html = template.replace("__BODY__", html_body)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("SUCCESS: CRUCIBLE_v6_Whitepaper.html successfully compiled.")
