from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import mm

ROOT = Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

styles = getSampleStyleSheet()
title = ParagraphStyle("Title", parent=styles["Title"], fontName="DejaVu-Bold", fontSize=18, leading=23, alignment=TA_CENTER, spaceAfter=14)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontName="DejaVu-Bold", fontSize=14, leading=18, spaceBefore=10, spaceAfter=7)
body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="DejaVu", fontSize=10.5, leading=15, spaceAfter=7)
bullet = ParagraphStyle("Bullet", parent=body, leftIndent=14, firstLineIndent=-7, spaceAfter=4)

def inline(s):
    return escape(s.strip()).replace("**", "")

def make_pdf(md_path):
    out = md_path.with_suffix(".pdf")
    doc = SimpleDocTemplate(str(out), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=18*mm, bottomMargin=18*mm, title=md_path.stem, author="EduGenie")
    story = []
    lines = md_path.read_text(encoding="utf-8").splitlines()
    first = True
    i = 0
    while i < len(lines):
        raw = lines[i].strip()
        if not raw:
            story.append(Spacer(1, 4)); i += 1; continue
        if raw.startswith("# "):
            story.append(Paragraph(inline(raw[2:]), title if first else h1))
        elif raw.startswith("## ") or raw.startswith("### "):
            story.append(Paragraph(inline(raw.lstrip("#").strip()), h1))
        elif raw.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(ListItem(Paragraph(inline(lines[i].strip()[2:]), body))); i += 1
            story.append(ListFlowable(items, bulletType="bullet", leftIndent=18)); first = False; continue
        else:
            story.append(Paragraph(inline(raw), bullet if raw[:2].isdigit() and ". " in raw[:5] else body))
        first = False; i += 1
    doc.build(story)

def main():
    folders = [p for p in ROOT.iterdir() if p.is_dir() and p.name[:1].isdigit()]
    for folder in sorted(folders):
        for md in sorted(folder.glob("*.md")):
            if md.name.lower() != "readme.md":
                make_pdf(md)

if __name__ == "__main__":
    main()
