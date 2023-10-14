from fpdf import FPDF
import glob
from pathlib import Path

files = glob.glob("file/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for file in files:
    title = Path(file).stem.title()
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=50, h=7, txt=title)
    pdf.ln(10)
    with open(file, "r") as content:
        content = content.read()
        pdf.set_font(family="Times", size=12)
        pdf.write(h=6, txt=content)

pdf.output("studpro.pdf")