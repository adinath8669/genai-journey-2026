from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBEDDING_MODEL

model=SentenceTransformer(EMBEDDING_MODEL)
def cerate_embaddings(chunks:str)->np.ndarray:
    embaddings=model.encode(chunks)
    embadding =np.array(embaddings).astype("float32")
    return embadding

def embad_query(query: str):
    return model.encode([query])
