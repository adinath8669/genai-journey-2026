# 🧠 Simple LangGraph Workflow

A beginner-friendly AI application built using **LangGraph**, **LangChain**, **Google Gemini**, and **Streamlit**.

This project demonstrates how to create AI workflows using nodes, state, and conditional routing.

---

## 📌 Features

- Ask any question
- Classifies the question
- Routes to the appropriate node
- Teacher Node for Python questions
- Interview Node for interview-related questions
- Summary Node for other questions
- Displays conversation history
- Built with Streamlit UI

---

## 🏗 Workflow

```
User Question
      │
      ▼
Classifier Node
      │
 ┌────┴─────────┐
 ▼              ▼
Teacher     Interview
      │
      ▼
 Summary
      │
      ▼
Final Answer
```

---

## 📂 Project Structure

```
16_LangGraph/

│── app.py
│── graph.py
│── nodes.py
│── models.py
│── services.py
│── prompts.py
│── config.py
│── README.md
│── requirements.txt
```

---

## 🚀 Technologies Used

- Python
- Streamlit
- LangGraph
- LangChain
- Google Gemini
- python-dotenv

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```text
GEN_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. User enters a question.
2. The Classifier Node identifies the question category.
3. LangGraph routes the question to the correct node.
4. The selected node generates the answer using Gemini.
5. The answer and category are displayed.
6. Conversation history is stored in Streamlit session state.

---

## 📚 Concepts Learned

- LangGraph
- StateGraph
- Nodes
- Edges
- Conditional Routing
- State Management
- Streamlit
- Google Gemini
- Modular Project Structure

---

## 🎯 Future Improvements

- Add Conversation Memory
- Add RAG Support
- Add PDF Chat
- Add Tool Calling
- Add Agents
- Save Chat History to Database
- Multi-Agent Workflow

---

## 👨‍💻 Author

**Adinath Kadam**

AI Engineer Bootcamp 2026
``