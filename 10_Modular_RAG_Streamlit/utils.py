from pypdf import PdfReader
from config import CHUNK_SIZE

def load_pdf(pdf: str)->str:
    reader =PdfReader(pdf)
    text=""
    for page in reader.pages:
        text +=page.extract_text() or " "
    return text

def create_chunks(text:str)->list[str]:
    chunks=[
    text[i:i+CHUNK_SIZE]
    for i in range (0,len(text),CHUNK_SIZE)]
    return chunks
