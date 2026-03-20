import pdfplumber
from docx import Document

def extract_text(path):
    try:
        if path.endswith(".pdf"):
            with pdfplumber.open(path) as pdf:
                return " ".join([p.extract_text() or "" for p in pdf.pages])

        elif path.endswith(".docx"):
            doc = Document(path)
            return " ".join([p.text for p in doc.paragraphs])

        elif path.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

    except Exception as e:
        print("Error reading file:", e)
        return "Could not extract text from file."

    return ""