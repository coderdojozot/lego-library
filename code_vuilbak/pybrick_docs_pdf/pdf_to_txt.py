# pdf_to_txt.py
# Zet een PDF-bestand om naar een tekstbestand (.txt)
# Vereist: pip install PyPDF2

import sys
from PyPDF2 import PdfReader

if len(sys.argv) < 2:
    print("Gebruik: python pdf_to_txt.py bestand.pdf")
    sys.exit(1)

pdf_path = sys.argv[1]
txt_path = pdf_path.rsplit('.', 1)[0] + '.txt'

reader = PdfReader(pdf_path)
with open(txt_path, 'w', encoding='utf-8') as f:
    for page in reader.pages:
        text = page.extract_text()
        if text:
            f.write(text)

print(f"Tekst opgeslagen in {txt_path}")