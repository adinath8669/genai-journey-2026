from config import TOP_K
import numpy as np
from services.embedding_service import embad_query


def retrive_chuncks(query,index,chunks):
    query_embedding=embad_query(query)
    query_embedding=np.array(query_embedding).astype("float32")

    distances,indices =index.search(query_embedding,TOP_K)

    retrieved_chunks=[]

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks