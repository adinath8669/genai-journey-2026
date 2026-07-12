from services.embedding_service import cerate_embaddings
from services.pdf_loader_service import load_pdf
from services.chuncking_service import create_chunks
from services.vectore_store_service import create_vector_db


def build_vectore_store(pdf_path:str):
    text=load_pdf(pdf_path)

    chunks=create_chunks(text)

    embadding=cerate_embaddings(chunks)

    vectore_db=create_vector_db(embadding)

    return vectore_db,chunks



