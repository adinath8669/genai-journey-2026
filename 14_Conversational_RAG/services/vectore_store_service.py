import faiss
import numpy as np

def create_vector_db(embadding:np.ndarray):
    dimensions=embadding.shape[1]
    index=faiss.IndexFlatL2(dimensions)
    index.add(embadding)
    return index