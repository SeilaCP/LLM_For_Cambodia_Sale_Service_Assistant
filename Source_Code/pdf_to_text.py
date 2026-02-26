import pdfplumber
from pathlib import Path

# Resolve paths relative to the repository root (parent of Source_Code)
base_dir = Path(__file__).resolve().parent.parent
pdf_path = base_dir / "Data" / "Raw_data" / "AEON.pdf"
out_path = base_dir / "Data" / "Cleaning_data" / "text_1.txt"

pdf_path_str = str(pdf_path)
out_path_str = str(out_path)

with pdfplumber.open(pdf_path_str) as pdf, open(out_path_str, "w", encoding="utf-8") as f:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            f.write(text + "\n")