# 📝 Day 12 Notes – Vector Databases

## 1. What are Embeddings?

Embeddings are numerical vector representations of text, images, or other data. They capture the semantic meaning of the data, allowing computers to compare similarity between different inputs.

**Example:**

- "AI"
- "Artificial Intelligence"

These produce similar embeddings because they have similar meanings.

---

## 2. What is a Vector Database?

A Vector Database stores embeddings (vectors) and performs fast similarity searches to find the most relevant data.

**Popular Vector Databases:**

- FAISS
- ChromaDB
- Pinecone
- Weaviate
- Milvus

---

## 3. What is FAISS?

FAISS (Facebook AI Similarity Search) is an open-source library developed by Meta for efficient similarity search and clustering of dense vectors.

### Features

- Fast vector search
- Handles millions of vectors
- Optimized for CPU and GPU
- Commonly used in RAG applications

---

## 4. What is ChromaDB?

ChromaDB is an open-source vector database designed for AI and LLM applications. It stores embeddings along with document metadata, making it easy to build semantic search and RAG systems.

### Features

- Easy to use
- Stores vectors and metadata
- Integrates with LangChain and LlamaIndex
- Suitable for small to medium AI projects

---

## 5. Similarity Search

Similarity Search finds documents whose embeddings are closest to the query embedding instead of matching exact keywords.

**Example:**

Query:

```
What is AI?
```

Results:

- Artificial Intelligence
- Neural Networks
- Machine Learning

---

## 6. Euclidean Distance

Euclidean Distance measures the straight-line distance between two vectors.

- Smaller distance → More similar
- Larger distance → Less similar

FAISS `IndexFlatL2` uses Euclidean Distance.

---

## 7. Cosine Similarity

Cosine Similarity measures the angle between two vectors rather than their distance.

Range:

- **1** → Exactly similar
- **0** → Unrelated
- **-1** → Opposite

Cosine Similarity is commonly used for comparing text embeddings.

---

## 8. Semantic Search

Semantic Search understands the meaning of a query instead of matching exact words.

**Example:**

Query:

```
How do computers learn?
```

Result:

```
Machine Learning uses data.
```

Even though the words are different, the meanings are related.

---

## 9. Why RAG Needs Vector Databases

RAG (Retrieval-Augmented Generation) uses a vector database to retrieve relevant documents before sending them to an LLM.

### Workflow

1. User asks a question.
2. Convert the question into an embedding.
3. Search the vector database for similar documents.
4. Retrieve the most relevant documents.
5. Send them to the LLM.
6. Generate an accurate answer.

Without a vector database, the LLM cannot efficiently search large collections of documents.

---
