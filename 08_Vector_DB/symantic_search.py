import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sentences
sentences =  [

"Python is a programming language.",

"Machine Learning uses data.",

"Football is a popular sport.",

"Neural Networks are inspired by the human brain."

]

# Generate embeddings
embeddings = model.encode(sentences)
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

query = input("Enter your question: ")

query_embedding = model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

distances, indices = index.search(query_embedding, 2)


print("\nTop Matching Documents:\n")

for i in range(len(indices[0])):
    print(f"{i+1}. {sentences[indices[0][i]]}")
    print(f"Distance: {distances[0][i]:.4f}\n")