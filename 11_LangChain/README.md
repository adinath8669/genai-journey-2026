# 🤖 LangChain Prompt Playground

A simple AI-powered web application built with **Streamlit**, **LangChain**, and **Google Gemini**.

This project demonstrates how to use **Prompt Templates** and **Chains** in LangChain to generate responses in different modes such as Teacher, Coder, and Interviewer.

---

## 🚀 Features

- 📚 Teacher Mode – Explains topics in simple language.
- 💻 Coder Mode – Explains concepts with Python examples.
- 🎤 Interviewer Mode – Generates interview questions with answers.
- ⚡ Built using LangChain Expression Language (LCEL).
- 🤖 Powered by Google Gemini 2.5 Flash.
- 🌐 Interactive Streamlit UI.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```
project/
│── app.py
│── prompt_templates.py
│── .env
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-prompt-playground.git
cd langchain-prompt-playground
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API Key

Create a `.env` file in the project root.

```env
GENAI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🖥️ How to Use

1. Select a mode from the sidebar.
   - Teacher
   - Coder
   - Interviewer

2. Enter a topic.

3. Click **Ask AI**.

4. View the generated response.

---

## 📸 Example

### Input

```
Topic:
Machine Learning

Mode:
Teacher
```

### Output

```
Machine Learning is a branch of Artificial Intelligence that enables computers to learn from data without being explicitly programmed...
```

---

## 📚 Concepts Learned

- LangChain
- Chat Models
- PromptTemplate
- LCEL (LangChain Expression Language)
- Chains
- Streamlit UI
- Google Gemini API Integration

---

## 📦 Future Improvements

- Conversation History
- Output Parser
- Multiple Prompt Templates
- Streaming Responses
- Chat Interface
- RAG Integration
- PDF Question Answering
- Memory Support

---

## 👨‍💻 Author

**Adinath Kadam**

AI & Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!