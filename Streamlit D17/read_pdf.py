#pip install pypdf
from pathlib import Path
from pypdf import PdfReader

SAMPLE = Path(__file__).resolve().parent / "Deep Learning mod 3.pdf"

def read_pdf(path) -> str:
    reader = PdfReader(path)      
    for page in reader.pages:
        print(page.extract_text())

read_pdf(SAMPLE)
