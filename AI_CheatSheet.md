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

# ⭐ Remember

❌ Don't memorize syntax.

✅ Understand the logic.

If you forget a function:
1. Read your cheat sheet.
2. Check the documentation.
3. Ask AI if needed.
4. Continue building.