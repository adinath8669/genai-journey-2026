from services.embedding_service import embed_query
from config.settings import TOP_K



def retrieve_chunks(query,index,  chunks: list[str]) -> list[str]:
    """
    Retrieve the most relevant chunks for a query.
    """

    query_embadding=embed_query(query)

    distances, indices = index.search(query_embadding, TOP_K)

    retrieved_chunks =[]

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks