# 🤖 AI Math Agent with LangChain Tools

An AI Agent built using **LangChain** and **Google Gemini** that can automatically choose the correct tool based on the user's query.

Instead of answering every question directly, the Agent decides which tool to use and then returns the final response.

---

# 🚀 Features

- 🧮 Calculator Tool
- 🐍 Python Teacher Tool
- 💼 Interview Question Generator
- 🤖 LangChain Agent
- 🔧 Tool Calling using `@tool`
- ✨ Google Gemini Integration

---

# 🏗️ Project Architecture

```text
                User
                  │
                  ▼
          LangChain Agent
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 Calculator   Python Teacher  Interview Generator
      │           │           │
      └───────────┴───────────┘
                  │
                  ▼
            Gemini LLM
                  │
                  ▼
           Final Response
```

---

# 📂 Project Structure

```text
15_AI_Agents/

│── app.py
│── agent.py
│── tools.py
│── prompts.py
│── README.md
│── notes.md
│── requirements.txt
```

---

# 🛠️ Technologies Used

- Python
- LangChain
- Google Gemini API
- python-dotenv

---

# ⚙️ Installation

### Clone the repository

```bash
git clone <repository-url>
cd 15_AI_Agents
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```text
GEN_API_KEY=your_google_gemini_api_key
```

---

# ▶️ Run the Project

```bash
python app.py
```

---

# 💬 Example Usage

### Calculator Tool

```text
You : 25 * 12

AI : 300
```

---

### Python Teacher Tool

```text
You : Explain decorators

AI :
Decorators are a Python feature used to modify the behavior of functions...
```

---

### Interview Generator Tool

```text
You : Generate Python interview questions

AI :

1. What is Python?
2. Explain List vs Tuple.
3. What are decorators?
4. What is a generator?
5. Explain *args and **kwargs.
```

---

# 🧠 Tools Used

### 🧮 Calculator Tool

Performs mathematical calculations.

---

### 🐍 Python Teacher Tool

Explains Python concepts in simple language with examples.

---

### 💼 Interview Generator Tool

Generates interview questions for technical topics.

---

# 📚 What I Learned

- LangChain Agents
- Tool Calling
- `@tool` Decorator
- Google Gemini Integration
- Creating Custom Tools
- Agent Decision Making

---

# 🎯 Future Improvements

- 🌦️ Real Weather API
- 🌐 Web Search Tool
- 📄 PDF Question Answering Tool
- 🧠 Conversation Memory
- 🎨 Streamlit Chat Interface

---

# 📖 Key Concepts

- **Agent** – Decides which tool to use.
- **Tool** – A Python function that performs a specific task.
- **Tool Calling** – The process of selecting and executing the appropriate tool.
- **LLM** – Generates the final response after receiving the tool output.

---

# 👨‍💻 Author

**Adinath Kadam**

AI Engineer Bootcamp 2026 🚀