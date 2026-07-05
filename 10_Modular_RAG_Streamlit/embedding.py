from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from config import EMBEDDING_MODEL

model= SentenceTransformer(EMBEDDING_MODEL)

def create_embeddings(chunks: list) -> np.ndarray:
   
    embeddings=model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")
    return embeddings
  
    

def create_vector_db(embeddings:np.ndarray):
    dimension=embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index 



   

