# 📝 Day  Notes – Retrieval-Augmented Generation (RAG)

## 1. What is RAG?

RAG (Retrieval-Augmented Generation) is an AI architecture that combines a **Vector Database** with a **Large Language Model (LLM)**. Before generating an answer, it retrieves the most relevant information from external documents and provides it as context to the LLM.

---

## 2. Why Do We Need RAG?

LLMs have limited knowledge based on their training data and may generate incorrect or outdated information (hallucinations).

RAG solves this by:
- Retrieving relevant information from external documents.
- Providing up-to-date knowledge.
- Reducing hallucinations.
- Answering questions about private documents.

---

## 3. RAG Workflow

```
Documents/PDF
      │
      ▼
Extract Text
      │
      ▼
Chunk Documents
      │
      ▼
Generate Embeddings
      │
      ▼
Store in Vector Database
      │
──────── User Question ────────
      │
      ▼
Generate Query Embedding
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Top-k Chunks
      │
      ▼
Prompt (Context + Question)
      │
      ▼
LLM (Gemini/OpenAI)
      │
      ▼
Final Answer
```

---

## 4. Document Chunking

Chunking is the process of splitting large documents into smaller pieces.

### Why Chunk?

- Improves retrieval accuracy.
- Fits within LLM token limits.
- Retrieves only relevant sections.
- Makes similarity search faster.

Example:

```
100-page PDF

↓

200 chunks

↓

Search only relevant chunks
```

---

## 5. Retrieval

Retrieval is the process of finding the most relevant document chunks for a user's query using embeddings and similarity search.

Instead of searching the entire document, only the most relevant chunks are retrieved.

---

## 6. Prompt Augmentation

The retrieved chunks are added to the prompt before sending it to the LLM.

Example:

```
Context:
<Retrieved Chunks>

Question:
What is AI?

Answer:
```

This allows the LLM to answer using the provided information.

---

## 7. Generation

The LLM reads:
- Retrieved context
- User question

Then generates the final answer based on the retrieved information.

---

## 8. Why RAG Reduces Hallucinations

Without RAG, the LLM relies only on its internal knowledge, which may be outdated or incorrect.

With RAG:
- The model receives relevant context.
- Answers are grounded in retrieved documents.
- The chance of making up information is greatly reduced.

---

## 9. Advantages of RAG

- Uses external knowledge.
- Reduces hallucinations.
- No retraining required.
- Easy to update by adding new documents.
- Works with private company data.
- Improves answer accuracy.

---

## 10. Limitations of RAG

- Depends on retrieval quality.
- Poor chunking reduces accuracy.
- Requires a vector database.
- Retrieval adds some latency.
- Large document collections require efficient indexing.

---

## 11. Components of a RAG System

- Document Loader (PDF, TXT, DOCX)
- Text Chunker
- Embedding Model
- Vector Database (FAISS, ChromaDB)
- Retriever
- Prompt Builder
- Large Language Model (LLM)

---

## 12. Common Libraries

```python
pypdf
sentence-transformers
faiss
numpy
google-genai
streamlit
fastapi
```

---

## 13. Real-World Applications

- PDF Question Answering
- Company Knowledge Base
- Customer Support Chatbots
- Legal Document Search
- Medical Document Assistant
- Research Paper Assistant
- Internal Enterprise Search

---

# 📌 Quick Revision

| Concept | Description |
|---------|-------------|
| RAG | Retrieval + Generation |
| Chunking | Splitting documents into smaller parts |
| Embedding | Numerical representation of text |
| Retrieval | Finding relevant chunks |
| Vector Database | Stores embeddings for fast search |
| Prompt Augmentation | Adding retrieved context to the prompt |
| Generation | LLM generates the final answer |
| Benefit | More accurate answers with fewer hallucinations |

---

# ⭐ Key Points to Remember

- RAG combines retrieval with text generation.
- Documents are split into chunks before indexing.
- Embeddings represent the meaning of text.
- Vector databases perform semantic search.
- Retrieved chunks are passed as context to the LLM.
- RAG improves accuracy without retraining the model.
- Updating documents updates the knowledge base instantly.