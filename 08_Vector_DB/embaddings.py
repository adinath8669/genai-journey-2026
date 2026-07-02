from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

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

# Calculate cosine similarity
similarity = cosine_similarity(embeddings)

# Print similarity matrix
print("Cosine Similarity Matrix:\n")
print(similarity)

# Compare AI with others
print("\nSimilarity Scores:")
print(f"AI <-> Artificial Intelligence : {similarity[0][1]:.4f}")
print(f"AI <-> Football : {similarity[0][2]:.4f}")
print(f"Artificial Intelligence <-> Football : {similarity[1][2]:.4f}")