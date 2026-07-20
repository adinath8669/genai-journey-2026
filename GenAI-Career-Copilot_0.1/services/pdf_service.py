from pypdf import PdfReader
import os
from config.settings import UPLOAD_DIR


def save_uploaded_file(uploaded_file ) -> str:
    """
    Save uploaded PDF and return its path.
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path



def load_pdf(pdf :str)->str:
    reader=PdfReader(pdf)
    text=""
    for pages in reader.pages:
        text += pages.extract_text() or " "

    return text