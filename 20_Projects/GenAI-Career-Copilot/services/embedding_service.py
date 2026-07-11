from sentence_transformers import SentenceTransformer
import numpy as np 
from config import EMBEDDING_MODEL


model=SentenceTransformer(EMBEDDING_MODEL)

def create_embeddings(chunks: list) -> np.ndarray:
    embaddings=model.encode(chunks)
    embadding=np.array(embaddings).astype("float32")
    return embadding

def embed_query(query: str):
    return model.encode([query])