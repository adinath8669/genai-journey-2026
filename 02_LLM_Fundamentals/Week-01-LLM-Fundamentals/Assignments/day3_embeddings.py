from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love programming.",
    "Coding is fun.",
    "I enjoy playing football."
]

embeddings = model.encode(sentences)

print(embeddings.shape)


s1 = model.encode(["I love programming."])
s2 = model.encode(["Coding is enjoyable."])
s3 = model.encode(["I like pizza."])

print("Programming vs Coding:")
print(cosine_similarity(s1, s2))

print("Programming vs Pizza:")
print(cosine_similarity(s1, s3))

