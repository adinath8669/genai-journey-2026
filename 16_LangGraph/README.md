# 🌐 LangGraph Workflow Demo

## 📌 Project Overview

This project demonstrates the basics of **LangGraph** by building a simple AI workflow with multiple nodes and conditional routing.

The application takes a user's question, classifies it, and routes it to the appropriate AI node before generating a response.

This project helped me understand how AI workflows are built using graphs instead of writing everything in a single function.

---

## 🚀 Features

- Accepts user questions
- Uses LangGraph to build workflows
- Implements multiple nodes
- Uses conditional routing
- Integrates Google's Gemini model
- Simple Streamlit interface

---

## 🏗 Workflow

### Basic Workflow

```text
User Question
      │
      ▼
Teacher Node
      │
      ▼
Answer
```

---

### Conditional Workflow

```text
             User Question
                    │
                    ▼
             Classifier Node
              /            \
             /              \
      Python?           Interview?
          │                  │
          ▼                  ▼
   Teacher Node      Interview Node
          │                  │
          └────────┬─────────┘
                   ▼
                 Answer
```

---

## 📂 Project Structure

```text
16_LangGraph/

│── app.py
│── graph.py
│── nodes.py
│── state.py
│── README.md
│── notes.md
│── requirements.txt
```

---

## 🛠 Technologies Used

- Python
- LangGraph
- LangChain
- Google Gemini API
- Streamlit
- python-dotenv

---

## ▶️ Installation

Clone the repository

```bash
git clone <your_repo_url>
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEN_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

---

## 📚 What I Learned

- What is LangGraph
- Graph-based AI workflows
- Nodes and Edges
- State management
- Conditional routing
- Building modular AI applications

---

## 🚀 Future Improvements

- Add Conversation Memory
- Add RAG support
- Add Calculator Tool
- Add Weather Tool
- Multi-Agent workflow
- Deploy on Streamlit Cloud

---

## 👨‍💻 Author

**Adinath Kadam**

Learning Generative AI Engineering 🚀