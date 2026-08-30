from pypdf import PdfReader
import os
from config.settings import UPLOAD_DIR,MIN_RESUME_TEXT_LENGTH


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
    try:
        reader=PdfReader(pdf)

    except Exception as e:
        raise ValueError(
            f"could not read PDF '{pdf}'. It may corrupted or password-protected."
        ) from e
    
    text=""
    for pages in reader.pages:
        text += pages.extract_text() or ""

    text = text.strip()


    if len(text) < MIN_RESUME_TEXT_LENGTH:
        raise ValueError(
            "This PDF doesn't contain enough readable text to analyze. "
            "It may be a scanned image without OCR — try uploading a text-based PDF."
        )

    return text