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
# LangChain Cheat Sheet

## What is LangChain?

LangChain is a framework that helps build AI applications using LLMs.

It connects:

LLM
↓

Prompts

↓

Memory

↓

Vector Database

↓

Tools

↓

Output Parser

---

## LangChain Flow

User Input
      │
      ▼
Prompt Template
      │
      ▼
LLM
      │
      ▼
Output Parser
      │
      ▼
Final Response

---

## Basic Example

```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

response = llm.invoke("What is AI?")

print(response.content)
```
# Prompt Template Cheat Sheet

## What is a Prompt Template?

A Prompt Template is a reusable prompt with variables.

Instead of writing prompts again and again,
we create one template and pass different values.

---

## Prompt Flow

User Input

↓

Variables

↓

Prompt Template

↓

LLM

↓

Response

---

## Basic Example

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Explain {topic} in simple words."
)

prompt = template.invoke({
    "topic": "Machine Learning"
})

print(prompt.text)
```

---

# Output Parser Cheat Sheet

## What is an Output Parser?

An Output Parser converts the LLM response into a structured format.

Instead of plain text,

LLM

↓

Parser

↓

JSON / List / Dictionary / Pydantic Object

---

## Basic Example

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

response = parser.invoke(llm_output)
```


---


# Conversation Memory Cheat Sheet

## What is Conversation Memory?

Conversation Memory stores previous messages so the chatbot can answer follow-up questions.

The LLM itself does NOT remember.

The application stores the history.

---

## Conversation Flow

User

↓

HumanMessage

↓

LLM

↓

AIMessage

↓

Store History

↓

Next Question

↓

Send Full History

↓

LLM

---

## Message Types

HumanMessage

User input

AIMessage

LLM response

SystemMessage

Rules for the AI

---

## Basic Example

```python
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
chat_history = InMemoryChatMessageHistory()
system_message = SystemMessage(
    content="You are a friendly AI assistant."
)

def chat(user_input):
    chat_history.add_user_message(HumanMessage(user_input))

    messages=[system_message]+chat_history.messages

    response=model.invoke(messages)

    chat_history.add_ai_message(AIMessage(response.content))

    return response.content
```


# AI Cheat Sheet – Conversational RAG & Memory

## What is Conversational RAG?

Conversational RAG combines **RAG** with **Conversation Memory**.

Instead of answering each question independently, it remembers previous messages and uses retrieved documents to answer follow-up questions.

---

## Conversational RAG Pipeline

```text
User Uploads PDF
        │
        ▼
Load PDF
        │
        ▼
Chunk Document
        │
        ▼
Generate Embeddings
        │
        ▼
Store in FAISS
        │
──────── User asks Question ────────
        │
        ▼
Conversation History
        │
        ▼
Generate Query Embedding
        │
        ▼
Retrieve Top-k Chunks
        │
        ▼
Prompt Template
(Context + Chat History + Question)
        │
        ▼
Gemini / OpenAI
        │
        ▼
Generate Answer
        │
        ▼
Store AI Response
```

---

# LangChain Messages

## HumanMessage

Message sent by the user.

```python
HumanMessage(content="What is AI?")
```

---

## AIMessage

Response generated by the LLM.

```python
AIMessage(content="AI stands for Artificial Intelligence.")
```

---

## SystemMessage

Defines how the AI should behave.

```python
SystemMessage(
content="You are a helpful AI assistant."
)
```

---

# Chat History

```text
SystemMessage
      │
      ▼
HumanMessage
      │
      ▼
AIMessage
      │
      ▼
HumanMessage
      │
      ▼
AIMessage
```

The entire history is sent to the LLM with every request.

---

# Prompt Template

```python
prompt = f"""
Context:
{retrieved_chunks}

Chat History:
{history}

Question:
{question}

Answer:
"""
```

---

# Retriever

```python
query_embedding = model.encode(query)

↓

FAISS Search

↓

Top-k Chunks
```

---

# Memory

The LLM **does not remember** conversations.

The application stores previous messages and sends them with each new request.

---

# Stateless vs Stateful

### Stateless

```text
Question

↓

LLM

↓

Answer
```

No memory.

---

### Stateful

```text
Question

↓

Chat History

↓

LLM

↓

Answer

↓

Save History
```

Remembers previous conversation.

---

# Common Libraries

```python
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)

from langchain_community.chat_message_histories import ChatMessageHistory

import faiss

from sentence_transformers import SentenceTransformer

import streamlit as st
```

---

# Important Terms

**Conversation History**
Previous user and AI messages.

**Memory**
Stores chat history in the application.

**HumanMessage**
Message from the user.

**AIMessage**
Response from the LLM.

**SystemMessage**
Instructions that define AI behavior.

**Retriever**
Finds relevant chunks from the vector database.

**Prompt Template**
Combines context, history, and the user's question.

---

# Why Conversational RAG?

✅ Answers follow-up questions

✅ Uses document context

✅ Reduces hallucinations

✅ Remembers conversation

✅ Better user experience

---

# Common Parameters

```python
top_k = 3

chunk_size = 500

embedding_model = "all-MiniLM-L6-v2"

llm = "gemini-2.5-flash"

temperature = 0.1
```

---

# Complete Architecture

```text
PDF
 │
 ▼
Load PDF
 │
 ▼
Chunk
 │
 ▼
Embeddings
 │
 ▼
FAISS
 │
 ▼
Retriever
 │
 ▼
Prompt Template
 │
 ▼
Gemini
 │
 ▼
Chat History
 │
 ▼
Streamlit UI
```
