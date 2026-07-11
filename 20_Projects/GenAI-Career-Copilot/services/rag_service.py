from services.embedding_service import embed_query
import numpy as np
from services.pdf_service import load_pdf
from services.chunking_service import create_chunks
from services.embedding_service import create_embeddings
from services.vector_store_service import create_vector_db
from config import TOP_K

# print(create_vector_db)


def build_vector_store(pdf_path: str):

    text = load_pdf(pdf_path)

    chunks = create_chunks(text)

    embeddings = create_embeddings(chunks)
    # print("Embeddings:", type(embeddings))

    vector_db = create_vector_db(embeddings)
    # print("Vector DB:", type(vector_db))


    return vector_db, chunks


def retrieve_chunks(query, index, chunks):
    # print(type(index))
    query_embedding=embed_query(query)
    query_embedding = np.array(query_embedding).astype("float32")

    distances,indices =index.search(query_embedding,TOP_K)

    # retriving relevnet chuncks from pdf
    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks
        