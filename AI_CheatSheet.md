# 🤖 AI Engineering Cheat Sheet

A quick reference for Python, GenAI, FastAPI, Streamlit, Vector Databases, RAG, and more.

---

# 📌 Python

## Virtual Environment

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install package_name
```

Install from requirements

```bash
pip install -r requirements.txt
```

Freeze packages

```bash
pip freeze > requirements.txt
```

---

# 📌 Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")
```

---

# 📌 Google Gemini

```python
from google import genai

client = genai.Client(api_key=api_key)
```

Generate response

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
```

Generation Config

```python
config={
    "temperature":0.7,
    "max_output_tokens":1000
}
```

---

# 📌 Prompt Template

```python
prompt = f"""
You are a {mode}.

Answer the following question:

{question}
"""
```

---

# 📌 FastAPI

Create app

```python
from fastapi import FastAPI

app = FastAPI()
```

GET

```python
@app.get("/")
def home():
    return {"message":"Hello"}
```

POST

```python
@app.post("/ask")
def ask():
    return {"answer":"Hello"}
```

Run

```bash
python -m uvicorn app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 📌 Pydantic

```python
from pydantic import BaseModel

class Question(BaseModel):
    question:str
```

---

# 📌 Streamlit

Title

```python
st.title("AI Assistant")
```

Button

```python
st.button("Ask")
```

Text Area

```python
st.text_area("Question")
```

Text Input

```python
st.text_input("Name")
```

Sidebar

```python
with st.sidebar:
    pass
```

Spinner

```python
with st.spinner("Thinking..."):
    pass
```

Download

```python
st.download_button(...)
```

Session State

```python
if "history" not in st.session_state:
    st.session_state.history=[]
```

Run

```bash
streamlit run app.py
```

---

# 📌 Embeddings

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(sentences)
```

---

# 📌 FAISS

```python
import faiss
import numpy as np
```

Create Index

```python
index = faiss.IndexFlatL2(384)
```

Add vectors

```python
index.add(embeddings)
```

Search

```python
distances, indices = index.search(query,2)
```

---

# 📌 Cosine Similarity

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(embeddings)
```

---

# 📌 NumPy

Convert float32

```python
embeddings = np.array(embeddings).astype("float32")
```

---

# 📌 RAG Flow

```
Documents
      ↓
Embeddings
      ↓
Vector Database
      ↓
User Query
      ↓
Embedding
      ↓
Similarity Search
      ↓
Top Documents
      ↓
LLM
      ↓
Answer
```

---

# 📌 Git

Initialize

```bash
git init
```

Clone

```bash
git clone url
```

Status

```bash
git status
```

Add

```bash
git add .
```

Commit

```bash
git commit -m "message"
```

Push

```bash
git push
```

---

# 📌 Common Errors

### Module not found

```bash
pip install package_name
```

---

### Activate venv

```bash
venv\Scripts\activate
```

---

### Install requirements

```bash
pip install -r requirements.txt
```

---

### Check Python

```bash
python --version
```

---

### Check Installed Package

```bash
pip show package_name
```

---

# 📌 AI Workflow

```
User
   ↓
Prompt
   ↓
LLM
   ↓
Response
```

---

# 📌 RAG Workflow

```
Question
     ↓
Embedding
     ↓
Vector DB
     ↓
Retrieve Documents
     ↓
LLM
     ↓
Final Answer
```

---

# 📌 Useful Commands

Run FastAPI

```bash
python -m uvicorn app:app --reload
```

Run Streamlit

```bash
streamlit run app.py
```

Install Packages

```bash
pip install package
```

Requirements

```bash
pip freeze > requirements.txt
```

---

# 📚 RAG (Retrieval-Augmented Generation) Cheat Sheet

---

# What is RAG?

RAG combines a Vector Database with a Large Language Model (LLM).

Instead of relying only on the model's internal knowledge, it first retrieves relevant documents and then generates an answer.

---

# RAG Pipeline

```
PDF / Documents
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
Store in Vector Database (FAISS/ChromaDB)
        │
──────── User asks a Question ────────
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
Create Prompt
(Context + Question)
        │
        ▼
LLM (Gemini/OpenAI/Llama)
        │
        ▼
Final Answer
```

---

# Step 1: Read PDF

```python
from pypdf import PdfReader

reader = PdfReader("file.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()
```

---

# Step 2: Chunking

```python
chunks = [
    text[i:i+500]
    for i in range(0, len(text), 500)
]
```

---

# Step 3: Create Embeddings

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)
```

Convert to float32

```python
embeddings = np.array(embeddings).astype("float32")
```

---

# Step 4: Store in FAISS

```python
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)
```

---

# Step 5: User Query

```python
query = "What is AI?"
```

---

# Step 6: Query Embedding

```python
query_embedding = model.encode([query])

query_embedding = np.array(query_embedding).astype("float32")
```

---

# Step 7: Retrieve Chunks

```python
distances, indices = index.search(query_embedding, 3)
```

Retrieve text

```python
retrieved_chunks = "\n\n".join(
    [chunks[i] for i in indices[0]]
)
```

---

# Step 8: Prompt

```python
prompt = f"""
You are a helpful AI assistant.

Use only the context below.

Context:
{retrieved_chunks}

Question:
{query}

Answer:
"""
```

---

# Step 9: Generate Response

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
```

---

# Common Libraries

```python
from pypdf import PdfReader

from sentence_transformers import SentenceTransformer

import faiss

import numpy as np

from google import genai
```

---

# Important Terms

### Chunk

Small piece of a document.

---

### Embedding

Vector representation of text.

---

### Vector Database

Stores embeddings for similarity search.

---

### Retrieval

Finding the most relevant chunks.

---

### Context

Retrieved chunks passed to the LLM.

---

### Generation

LLM generates the final answer.

---

# Why RAG?

✅ Reduces hallucinations

✅ Uses external knowledge

✅ Doesn't require retraining

✅ Handles private documents

✅ Easy to update

---

# Common Parameters

```python
top_k = 3
chunk_size = 500
embedding_model = "all-MiniLM-L6-v2"
llm = "gemini-2.5-flash"
```

---
