"""Convert scanned PDF pages to PNG images in /tmp for transcription.

Usage:
    python3 convert_pdf_to_images.py

Input : 03. The Four Fundamental Subspaces.pdf (same folder as this script)
Output: /tmp/four_subspaces_pages/page-01.png, page-02.png, ...
"""

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PDF_PATH = SCRIPT_DIR / "06. Eigen Values and Eigen Vectors.pdf"
OUT_DIR = Path(SCRIPT_DIR / "extracted")
DPI = 200


def convert_with_pymupdf() -> int:
    import fitz  # PyMuPDF

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(dpi=DPI)
        out = OUT_DIR / f"page-{i:02d}.png"
        pix.save(out)
        print(f"Wrote {out}")
    return len(doc)


def convert_with_pdftoppm() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    prefix = str(OUT_DIR / "page")
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(DPI), str(PDF_PATH), prefix],
        check=True,
    )
    # pdftoppm names files page-1.png, page-2.png, ... -> normalize to page-01.png
    files = sorted(OUT_DIR.glob("page-*.png"))
    for f in files:
        num = "".join(c for c in f.stem.split("-")[-1] if c.isdigit())
        new = OUT_DIR / f"page-{int(num):02d}.png"
        if f != new:
            f.rename(new)
        print(f"Wrote {new}")
    return len(files)


def main() -> None:
    if not PDF_PATH.exists():
        print(f"PDF not found: {PDF_PATH}", file=sys.stderr)
        sys.exit(1)
    try:
        n = convert_with_pymupdf()
        print(f"Done via PyMuPDF: {n} pages -> {OUT_DIR}")
    except ImportError:
        print("PyMuPDF not installed, trying pdftoppm...", file=sys.stderr)
        try:
            n = convert_with_pdftoppm()
            print(f"Done via pdftoppm: {n} pages -> {OUT_DIR}")
        except FileNotFoundError:
            print(
                "Neither PyMuPDF nor pdftoppm found.\n"
                "Install one with: pip install pymupdf",
                file=sys.stderr,
            )
            sys.exit(1)


if __name__ == "__main__":
    main()


"""
you have to convert the scanned handwritten notes in @[05. Determinants.pdf] into digital markdown notes (obsidian), each page is a scanned image and have be extracted out into the
  @[extracted] folder, go through each one and provide a single markdown file with the same name, leave placeholders for figures/diagrams, use latex for maths. Flag any mistakes (don't fix
  yourself) in the text.
"""