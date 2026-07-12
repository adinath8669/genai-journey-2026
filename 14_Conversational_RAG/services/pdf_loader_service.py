from pypdf import PdfReader

def load_pdf(pdf: str)->str:
    reader =PdfReader(pdf)
    text=""
    for page in reader.pages:
        text +=page.extract_text() or " "
    return text



