import pdfplumber
import re

async def extract_text(file) -> str:
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def find_term_value(text: str, term: str) -> str:
    lines = text.lower().splitlines()
    for line in lines:
        if term.lower() in line:
            match = re.search(r'([\d.]+)', line)
            return match.group(1) if match else None
    return None
