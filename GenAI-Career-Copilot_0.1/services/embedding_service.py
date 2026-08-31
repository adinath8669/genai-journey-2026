from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL
import numpy as np
import streamlit as st

# model=SentenceTransformer(EMBEDDING_MODEL)
"""
Generate embeddings for a list of text chunks.
Returns a NumPy array of shape (n_chunks, embedding_dimension).
"""
@st.cache_resource
def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)

def create_embeddings(chunks : list[str])->np.array:
    model = get_embedding_model()
    embeddings=model.encode(chunks)
    embedding=np.array(embeddings).astype("float32")

    return embedding

def embed_query(query :str):
    model = get_embedding_model()
    embaded_query=model.encode([query])
    embad_query=np.array(embaded_query).astype("float32")

    return embad_query