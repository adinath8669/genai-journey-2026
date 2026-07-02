import faiss
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sentences
sentences = [
    "AI",
    "Artificial Intelligence",
    "Football"
]

# Generate embeddings
embeddings = model.encode(sentences)
index = faiss.IndexFlatL2(384)

index.add(embeddings)

Query=model.encode(
    ["What is Artificial Intelligence?"]
)

distance, index_result = index.search(Query, 2)

print(index_result)