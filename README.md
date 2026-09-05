# 🚀 AI Engineer Bootcamp 2026

![CI](https://github.com/adinath8669/genai-journey-2026/actions/workflows/tests.yml/badge.svg)

Welcome to my **AI Engineer learning journey**.

This repository documents my transition from software engineering and machine learning into **Generative AI engineering**, with a focus on building practical, production-oriented AI applications.

Rather than learning AI only through tutorials, I am learning by **building projects, debugging real problems, refactoring code, writing tests, containerizing applications, and deploying them to the cloud**.

---

## 🎯 Goal

My goal is to become a **production-ready Generative AI Engineer** capable of designing, building, testing, and deploying AI-powered applications using:

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Embeddings & Vector Search
* LangChain
* LangGraph
* AI Agents
* FastAPI
* Streamlit
* Hugging Face
* Gemini API
* Docker
* GitHub Actions
* Cloud Deployment

The focus is not only on using AI frameworks, but on understanding the **architecture, engineering decisions, debugging process, and production considerations** behind AI applications.

---

# 🧠 Current Skills

## Programming

* Python
* Java
* SQL
* JavaScript

## Machine Learning

* Machine Learning
* Deep Learning
* Scikit-Learn
* TensorFlow
* NumPy
* Pandas

## Generative AI

* LLM Fundamentals
* Prompt Engineering
* Gemini API
* Hugging Face
* Embeddings
* Semantic Search
* Vector Databases
* FAISS
* Retrieval-Augmented Generation (RAG)
* LangChain

  * PromptTemplate
  * LCEL
  * Output Parsers
  * Pydantic Structured Output
  * Conversation Memory
* LangGraph

  * State
  * Nodes
  * Edges
  * Conditional Routing
  * Multi-Node Workflows

## Backend & Web

* Flask
* FastAPI
* Streamlit
* Spring Boot
* Angular
* HTML
* CSS
* Bootstrap

## Databases

* Oracle
* PostgreSQL

## DevOps & Tools

* Docker
* Git
* GitHub
* GitHub Actions
* CI/CD
* Linux
* VS Code

---

# 📚 Learning Roadmap

### Completed

* [x] LLM Fundamentals
* [x] Prompt Engineering
* [x] Gemini API
* [x] Hugging Face
* [x] Embeddings
* [x] Vector Databases
* [x] Semantic Search
* [x] RAG
* [x] LangChain
* [x] FastAPI
* [x] Streamlit
* [x] LangGraph Fundamentals
* [x] Conditional Routing
* [x] Multi-Node Workflows
* [x] Docker
* [x] GitHub Actions
* [x] CI/CD
* [x] Cloud Deployment

### In Progress / Next

* [ ] Advanced LangGraph
* [ ] AI Agents
* [ ] Multi-Agent Workflows
* [ ] Production AI Systems
* [ ] Monitoring & Observability
* [ ] Advanced RAG
* [ ] Interview Preparation

---

# 🛠️ Featured Project

# 🤖 GenAI Career Copilot

**GenAI Career Copilot** is an AI-powered career assistant that analyzes a user's resume and provides personalized career guidance.

The application combines **RAG, embeddings, FAISS, LangChain, Gemini, LangGraph, Pydantic structured output, Streamlit, Docker, testing, and CI/CD** into a single end-to-end application.

### 🌐 Live Application

👉 **[Open GenAI Career Copilot](https://genai-career-copilot-exek6rceoppageoxlqfh82.streamlit.app/)**

### 💻 Repository

👉 **[View the GenAI Career Copilot Source Code](https://github.com/adinath8669/genai-journey-2026/tree/main/GenAI-Career-Copilot_0.1)**

---

## ✨ Features

### 📊 Resume Analysis

Analyzes an uploaded resume and generates:

* Resume Score
* ATS Score
* Strengths
* Weaknesses
* Missing Skills

### 🤖 Interview Preparation

Generates personalized interview questions based on the resume:

* Technical Questions
* Behavioral Questions
* Project Questions
* Follow-up Questions
* Difficulty Level
* Model Answers

### 📅 Personalized Study Plan

Generates a structured 30-day learning plan containing:

* Weekly Goals
* Learning Topics
* Study Tasks
* Mini Projects
* Learning Resources
* Interview Questions
* Estimated Study Hours

### 💼 Job Role Matching

Analyzes the resume and recommends suitable roles with:

* Match Score
* Reasoning
* Missing Skills
* Recommended Next Steps

### 📋 Job Description Matcher

Compares a resume against a job description and provides:

* Overall Match Score
* Matched Skills
* Missing Skills
* Resume Weaknesses
* Resume Improvement Suggestions
* ATS Suggestions
* Final Recommendation

### 💬 Conversational Resume Chat

Allows users to ask questions about their resume using:

* RAG
* FAISS retrieval
* LLM generation
* Conversation memory

---

# 🏗️ Architecture

The application follows a modular architecture:

```text
                         ┌──────────────────┐
                         │    Streamlit UI  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     Services     │
                         │ PDF / RAG / LLM  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Embeddings +     │
                         │      FAISS       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    LangGraph     │
                         │                  │
                         │ State            │
                         │ Nodes            │
                         │ Routing          │
                         └────────┬─────────┘
                                  │
                  ┌───────────────┼───────────────┐
                  ▼               ▼               ▼
             Interview       Study Plan       Job Match
                  │               │               │
                  └───────────────┼───────────────┘
                                  ▼
                         ┌──────────────────┐
                         │   Gemini / LLM   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │      Result      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Streamlit UI  │
                         └──────────────────┘
```

---

# 🔄 RAG Pipeline

The resume processing pipeline follows:

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Text Chunking
    ↓
Sentence Transformer
    ↓
Embeddings
    ↓
FAISS Vector Store
    ↓
Similarity Search
    ↓
Relevant Resume Chunks
    ↓
Prompt + Context
    ↓
Gemini LLM
    ↓
Structured Response
```

This allows the application to retrieve relevant parts of the resume before generating an answer.

---

# 🧩 LangGraph Workflow

LangGraph is used to orchestrate the application's workflow.

The graph maintains shared information through a unified `GraphState` and uses conditional routing to determine which feature should process a request.

```text
START
  ↓
Resume Analysis
  ↓
Skill Gap Analysis
  ↓
Intent Analysis
  ↓
Conditional Router
  │
  ├── Interview
  │      ↓
  │     END
  │
  ├── Study Plan
  │      ↓
  │   Study Plan Generation
  │      ↓
  │     END
  │
  └── Job Match
         ↓
        END
```

### Key LangGraph concepts implemented

* State management
* Nodes
* Edges
* Conditional edges
* Intent-based routing
* Multi-node branches
* Shared state between workflow steps
* Integration with real application services

The LangGraph workflow is integrated directly with the Streamlit application rather than existing only as a standalone demonstration.

---

# 🧱 Project Structure

```text
GenAI-Career-Copilot_0.1/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env.example
│
├── services/
│   ├── pdf_service.py
│   ├── chunking_service.py
│   ├── embedding_service.py
│   ├── vector_store_service.py
│   ├── retrieval_service.py
│   ├── rag_service.py
│   ├── llm_service.py
│   ├── analysis_service.py
│   ├── interview_service.py
│   ├── study_plan_service.py
│   ├── job_match_service.py
│   ├── job_description_service.py
│   └── chat_service.py
│
├── graph/
│   ├── graph.py
│   ├── nodes.py
│   └── state.py
│
├── models/
│   ├── schemas.py
│   └── study_plan_models.py
│
├── parsers/
│   ├── output_parser.py
│   └── study_plan_parser.py
│
├── prompts/
│   ├── resume_prompt.py
│   ├── interview_prompt.py
│   ├── planner_prompt.py
│   ├── ats_prompt.py
│   ├── study_plan_prompt.py
│   └── job_description_prompt.py
│
├── ui/
│   ├── resume_analysis.py
│   ├── interview.py
│   ├── study_plan.py
│   ├── job_match.py
│   ├── job_description.py
│   └── chat.py
│
├── helper_utils/
│   ├── helper.py
│   └── chat_utils.py
│
├── tests/
│   ├── test_pdf_service.py
│   └── test_graph.py
│
└── memory/
    └── memory.py
```

---

# 🛡️ Production Readiness Work

After completing the core application, I performed an additional production-readiness pass before deployment.

## Day 1 — Architecture Review

* Traced the complete application flow.
* Reviewed `app → UI → services → LangChain → LangGraph → FAISS → Gemini`.
* Identified and fixed a routing bug that caused intent detection to fail silently.
* Fixed a router/edge-map mismatch.
* Removed repeated `graph.invoke()` boilerplate by introducing a shared helper.

## Day 2 — Error Handling & Validation

Improved PDF and LLM error handling.

The application now handles problems such as:

* Corrupted PDFs
* Password-protected PDFs
* Scanned/unreadable PDFs
* LLM failures

Errors provide useful diagnostic information instead of silently returning incorrect results.

## Day 3 — Caching & Performance

* Cached the embedding model using `st.cache_resource`.
* Reduced unnecessary model initialization.
* Improved UI behavior around generate/regenerate actions.
* Avoided unnecessary repeated LLM calls.

## Day 4 — Logging

Added structured logging across:

* PDF processing
* LLM services
* LangGraph routing
* Application operations

This provides a persistent record of important application events.

## Day 5 — Testing

Added automated tests using `pytest`.

The tests focus on deterministic, high-risk areas including:

* PDF validation
* LangGraph routing

The routing tests are particularly important because they protect against the same class of bug that was discovered during architecture review.

## Day 6 — Security

* Verified that API keys were not committed to Git history.
* Added `.env.example`.
* Updated `.gitignore`.
* Kept secrets outside the repository.

## Day 7 — Docker

Containerized the application using:

* Dockerfile
* `.dockerignore`

During local Docker setup, I also debugged a real Docker Desktop / WSL2 environment issue (BIOS virtualization, Windows feature flags, and a WSL version update were all required before the Docker engine would run).

## Day 8 — Deployment & CI/CD

The application was initially tested on Render.

The deployment exposed a real **512 MB memory limitation** caused by the ML dependencies (Streamlit + LangChain/LangGraph + Sentence Transformers + PyTorch).

After diagnosing the deployment logs and memory usage, I moved the application to **Streamlit Community Cloud**, which better fits the application's current resource requirements.

GitHub Actions was also added to automatically run the test suite on every push.

During CI setup, I found and fixed an issue where importing a module for testing indirectly constructed a live Gemini API client, causing tests to fail when no API key was available in the CI environment.

---

# 🧪 Testing

The project uses `pytest` for automated testing.

Run tests locally with:

```bash
python -m pytest tests/ -v
```

The CI pipeline automatically executes the test suite through GitHub Actions.

```text
Git Push
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
Run Pytest
   ↓
Pass / Fail
```

---

# 🐳 Docker

The application can also be containerized with Docker.

### Build

```bash
docker build -t genai-career-copilot .
```

### Run

```bash
docker run -p 8501:8501 --env-file .env genai-career-copilot
```

Then open:

```text
http://localhost:8501
```

> API keys are passed in at runtime via `--env-file`, never baked into the image, and should never be committed to GitHub.

---

# ⚙️ Local Setup

## 1. Clone the repository

```bash
git clone https://github.com/adinath8669/genai-journey-2026.git
cd genai-journey-2026/GenAI-Career-Copilot_0.1
```

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

Create a `.env` file based on `.env.example`.

Add your Gemini API key:

```env
GENAI_API_KEY=your_api_key_here
```

**Never commit `.env` or API keys to GitHub.**

## 5. Run the application

```bash
streamlit run app.py
```

---

# ☁️ Deployment

The application is currently deployed using **Streamlit Community Cloud**.

### Deployment Flow

```text
Developer
    ↓
Git Commit
    ↓
Git Push
    ↓
GitHub
    ↓
Streamlit Community Cloud
    ↓
Application Deployment
    ↓
Live GenAI Career Copilot
```

### Live Application

👉 **[Launch GenAI Career Copilot](https://genai-career-copilot-exek6rceoppageoxlqfh82.streamlit.app/)**

---

# 📈 Learning Journey

## Week 1 — LLM & Embeddings

### Goals

* Understand LLM fundamentals
* Understand tokens
* Understand embeddings
* Learn semantic search
* Build a basic AI application

### Project

Built a semantic search application using:

* Sentence Transformers
* Embeddings
* FAISS

---

## Week 2 — RAG & LangChain

Learned and implemented:

* RAG
* Document chunking
* Vector search
* LangChain
* PromptTemplate
* LCEL
* Output Parsers
* Pydantic Structured Output
* Conversation Memory

Started building the **GenAI Career Copilot**.

---

## LangGraph Phase

Learned LangGraph progressively rather than immediately jumping into complex agents.

### Progression

1. Basic sequential graph
2. State management
3. Nodes and edges
4. Conditional routing
5. Multi-node workflows
6. Conditional routing with real services
7. Job matching branch
8. Integration with the Streamlit application

The goal was to understand **workflow orchestration and state management** before moving toward AI agents.

---

# 💡 Key Engineering Lessons

Building this project taught me several lessons that are difficult to learn from tutorials alone.

### 1. Working code is not automatically production-ready

A feature can work correctly while still having problems with:

* Error handling
* Logging
* Testing
* Caching
* Security
* Deployment
* Maintainability

### 2. Bugs can hide in workflow logic

A routing bug can look harmless during code review while completely changing the application's behavior.

Automated tests for deterministic workflow logic are therefore important.

### 3. Deployment is part of engineering

A working application locally does not guarantee that it will work in the cloud.

The project exposed a real memory limitation during deployment, which required choosing a hosting platform appropriate for the application's workload.

### 4. AI applications still require traditional software engineering

Building GenAI applications involves much more than prompting an LLM.

Important engineering areas include:

* Modular architecture
* Validation
* Exception handling
* Testing
* Logging
* Configuration management
* Secret management
* Caching
* CI/CD
* Deployment

### 5. Frameworks should solve real problems

LangChain and LangGraph were introduced into the project with the goal of understanding their role in application architecture rather than using them simply because they are popular.

---

# 🚧 Future Improvements

Planned improvements include:

* [ ] LLM-based intent routing
* [ ] Gap-aware study plan generation
* [ ] Advanced RAG techniques
* [ ] Resume improvement
* [ ] Cover letter generation
* [ ] Better dashboard
* [ ] Exportable reports
* [ ] Advanced LangGraph workflows
* [ ] AI Agents
* [ ] Multi-Agent Architecture
* [ ] Monitoring & Observability
* [ ] Production-grade persistence
* [ ] Improved evaluation of LLM responses

---

# 📂 Other Projects

Other projects being explored or developed:

* AI Chatbot
* AI PDF Chatbot
* AI Interview Coach
* AI Research Assistant
* AI Code Reviewer

---

# 🎯 Final Goal

My long-term goal is to become an **AI Engineer who can take an AI idea from concept to production**.

That means being able to:

```text
Understand the Problem
        ↓
Design the Architecture
        ↓
Build the AI Workflow
        ↓
Integrate LLM / RAG / Agents
        ↓
Write Tests
        ↓
Handle Errors
        ↓
Containerize
        ↓
Deploy
        ↓
Monitor
        ↓
Improve
```

This repository represents that journey.

⭐ **Every project, bug, test, deployment issue, and commit is part of becoming a better AI Engineer.**
