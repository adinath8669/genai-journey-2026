from services.embedding_service import create_embeddings
from services.pdf_service import load_pdf
from services.chunking_service import create_chunks
# from vector_store_service import create_vector_store
import faiss
import numpy as np


def create_vector_store(embeddings: np.ndarray) -> faiss.IndexFlatL2:
    """
Create a FAISS vector index from embeddings.
Returns a searchable FAISS index.
"""
    dimensions=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimensions)
    index.add(embeddings)

    return index


def build_vector_store(pdf_path: str):
    """
    Complete pipeline:
    PDF -> Text -> Chunks -> Embeddings -> FAISS
    """

    text=load_pdf(pdf_path)

    chunks=create_chunks(text)

    embeddings = create_embeddings(chunks)

    index=create_vector_store(embeddings)

    return index,chunks

