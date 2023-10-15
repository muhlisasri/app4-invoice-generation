import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=50, h=8, txt=f"Date : {date}", ln=1)
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = df.columns
    columns = [item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=5, txt=columns[0], border=1)
    pdf.cell(w=65, h=5, txt=columns[1], border=1)
    pdf.cell(w=35, h=5, txt=columns[2], border=1)
    pdf.cell(w=30, h=5, txt=columns[3], border=1)
    pdf.cell(w=30, h=5, txt=columns[4], border=1, ln=1)

    for i in df.index:
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30, h=5, txt=str(df["product_id"][i]), border=1)
        pdf.cell(w=65, h=5, txt=str(df["product_name"][i]), border=1)
        pdf.cell(w=35, h=5, txt=str(df["amount_purchased"][i]), border=1)
        pdf.cell(w=30, h=5, txt=str(df["price_per_unit"][i]), border=1)
        pdf.cell(w=30, h=5, txt=str(df["total_price"][i]), border=1, ln=1)

    pdf.output(f"PDF/{filename}.pdf")