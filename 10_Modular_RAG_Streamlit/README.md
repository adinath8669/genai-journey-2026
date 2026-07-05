# 🤖 AI Study Assistant (RAG)

An AI-powered Study Assistant built with **Streamlit**, **Google Gemini**, **FAISS**, and **Sentence Transformers**.

The application allows users to upload a PDF, ask questions about its content, and receive answers generated using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- 📄 Upload any PDF
- ✂️ Automatic text chunking
- 🧠 Sentence embeddings using Sentence Transformers
- 🔍 Semantic search with FAISS
- 🤖 Google Gemini for answer generation
- 💬 Chat history
- 📥 Download chat history
- 🎨 Multiple AI modes
  - Teacher
  - Coder
  - Creative

---

## 📂 Project Structure

```
project/
│── app.py
│── rag.py
│── embedding.py
│── utils.py
│── config.py
│── requirements.txt
│── README.md
│
├── uploads/
└── data/
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- FAISS
- Sentence Transformers
- PyPDF
- NumPy

---

## ⚙️ Installation

Clone the repository

```bash
git clone <your-repository-url>
```

Go inside the project

```bash
cd project
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GENAI_API_KEY=your_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Create Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
──────────────
User Question
      │
      ▼
Embedding
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Top Chunks
      │
      ▼
Gemini
      │
      ▼
Answer
```

---

## 📸 Application Workflow

1. Upload a PDF.
2. The PDF is converted into text.
3. Text is split into chunks.
4. Embeddings are created.
5. Embeddings are stored in FAISS.
6. User asks a question.
7. Similar chunks are retrieved.
8. Gemini generates the final answer.

---

## 📚 Learning Concepts

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Semantic Search
- Vector Databases
- FAISS
- Streamlit
- Google Gemini API

---

## 📌 Future Improvements

- Support multiple PDFs
- Chat with multiple documents
- ChromaDB integration
- LangChain integration
- Conversation memory
- Source citations
- Docker support
- Authentication

---

## 👨‍💻 Author

**Adinath Kadam**

AI & Machine Learning Enthusiast

---

## ⭐ If you found this project useful

Give it a ⭐ on GitHub!