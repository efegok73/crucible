#!/usr/bin/env python3
"""
CRUCIBLE v7.2 — Deterministic Source Document Paragraph Indexer
===============================================================
Parses raw primary documents (.pdf, .docx, .txt, .md) and converts them into
a deterministically anchored text format where every paragraph is prefixed with
[P:0001], [P:0002], etc., matching the exact paragraph segmentation of crucible_linter.py.

Usage:
  python index_source.py input_file.pdf
  python index_source.py input_file.docx -o indexed_source.txt
  python index_source.py input_file.pdf --stats
"""

import os
import sys
import re
import argparse

try:
    import docx
except ImportError:
    docx = None

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


def extract_paragraphs(file_path: str) -> list[str]:
    """Extract paragraphs using the exact same logic as CrucibleLinter."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.pdf':
        try:
            import fitz
            doc = fitz.open(file_path)
            paras = []
            for page in doc:
                text = page.get_text()
                if text:
                    text = text.replace('\x00', '')
                    page_paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
                    paras.extend(page_paras)
            if paras:
                return paras
        except Exception:
            pass

        reader = None
        try:
            import pypdf
            reader = pypdf.PdfReader(file_path)
        except ImportError:
            try:
                import PyPDF2
                reader = PyPDF2.PdfReader(file_path)
            except ImportError:
                pass

        if reader is None:
            raise ImportError("Neither 'fitz' (PyMuPDF), 'pypdf', nor 'PyPDF2' is installed. Run: pip install pymupdf or pypdf")

        paras = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                text = text.replace('\x00', '')
                page_paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
                paras.extend(page_paras)
        return paras

    elif ext == '.docx':
        if docx is not None:
            doc = docx.Document(file_path)
            return [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        else:
            import zipfile
            import xml.etree.ElementTree as ET
            with zipfile.ZipFile(file_path) as z:
                tree = ET.fromstring(z.read('word/document.xml'))
            paras = []
            for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
                if texts:
                    paras.append(''.join(texts))
            return [p.strip() for p in paras if p.strip()]

    else:
        # Markdown / Plain text
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        return [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]


def index_paragraphs(paras: list[str]) -> list[str]:
    """Prefix each paragraph with zero-padded [P:xxxx]."""
    indexed = []
    width = max(4, len(str(len(paras))))
    for idx, p in enumerate(paras, start=1):
        anchor = f"[P:{str(idx).zfill(width)}]"
        indexed.append(f"{anchor} {p}")
    return indexed


def main():
    parser = argparse.ArgumentParser(
        description="CRUCIBLE v7.2 — Deterministic Source Document Paragraph Indexer"
    )
    parser.add_argument("source", help="Primary source document (.pdf, .docx, .txt, .md)")
    parser.add_argument("-o", "--output", default=None, help="Output file path (default: stdout)")
    parser.add_argument("--stats", action="store_true", help="Print corpus statistics")

    args = parser.parse_args()

    try:
        paras = extract_paragraphs(args.source)
    except Exception as e:
        print(f"Error extracting paragraphs: {e}", file=sys.stderr)
        sys.exit(1)

    total_paras = len(paras)
    total_words = sum(len(p.split()) for p in paras)
    total_chars = sum(len(p) for p in paras)

    if args.stats:
        print(f"=== CORPUS STATISTICS: {os.path.basename(args.source)} ===")
        print(f"Total Paragraphs: {total_paras:,}")
        print(f"Total Words:      {total_words:,}")
        print(f"Total Characters: {total_chars:,}")
        print(f"Est. Tokens:      ~{int(total_words * 1.3):,}")
        print("=" * 45)

    indexed = index_paragraphs(paras)
    output_text = "\n\n".join(indexed)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_text)
        print(f"Successfully indexed {total_paras} paragraphs to '{args.output}'.")
    elif not args.stats:
        print(output_text)


if __name__ == "__main__":
    main()
