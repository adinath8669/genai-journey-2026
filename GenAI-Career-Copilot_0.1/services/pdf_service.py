from pypdf import PdfReader

def load_pdf(pdf :str)->str:
    reader=PdfReader(pdf)
    text=""
    for text in reader.pages:
        text += text.extract_text() or " "

    return text