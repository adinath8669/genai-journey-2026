from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL
import numpy as np

model=SentenceTransformer(EMBEDDING_MODEL)
"""
Generate embeddings for a list of text chunks.
Returns a NumPy array of shape (n_chunks, embedding_dimension).
"""
def create_embeddings(chunks : list[str])->np.array:
    embeddings=model.encode(chunks)
    embedding=np.array(embeddings).astype("float32")

    return embedding

def embed_query(query :str):
    embaded_query=model.encode([query])
    embad_query=np.array(embaded_query).astype("float32")

    return embad_query