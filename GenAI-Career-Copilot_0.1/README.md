# 🚀 GenAI Career Copilot

> An AI-powered career assistant that analyzes resumes, identifies skill gaps, generates interview questions, creates personalized learning plans, recommends suitable job roles, and compares resumes against job descriptions.

GenAI Career Copilot is a portfolio project designed to demonstrate how modern Generative AI technologies can be combined to build a practical AI-powered application.

The project uses **RAG, LangChain, Gemini, FAISS, Sentence Transformers, Pydantic, and Streamlit** to transform an uploaded resume into personalized career recommendations.

---

## 🎯 Project Goal

The goal of GenAI Career Copilot is to create an AI career assistant that can understand a candidate's resume and provide actionable career guidance.

Instead of manually analyzing a resume, searching for suitable jobs, identifying missing skills, and creating a learning plan, the application brings these capabilities together in one platform.

---

# ✨ Features

## 📄 Resume Upload

Users can upload their resume as a PDF.

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Text Chunking
    ↓
Embeddings
    ↓
FAISS Vector Store
```

## 🔎 RAG-Based Resume Understanding

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the uploaded resume before sending the context to the LLM.

```text
User Query
    ↓
Query Embedding
    ↓
FAISS Similarity Search
    ↓
Relevant Resume Chunks
    ↓
Prompt
    ↓
Gemini
    ↓
Structured Response
```

## 📊 Resume Analysis

The Resume Analysis module provides:

- Resume Score
- ATS Score
- Strengths
- Weaknesses
- Missing Skills

## 🤖 Interview Question Generator

The application generates personalized interview questions based on the uploaded resume.

Questions are organized into:

- Technical Questions
- Behavioral Questions
- Project Questions
- Follow-up Questions

Each question contains:

- Question
- Difficulty
- Expected Answer

## 📅 Personalized 30-Day Study Plan

The application generates a personalized learning roadmap based on the candidate's resume and skill gaps.

The plan contains:

- Weekly Goals
- Study Topics
- Goals
- Estimated Hours
- Mini Projects
- Free Resources
- Interview Questions
- Weekly Deliverables

The plan is designed around approximately **3–4 hours/day**.

## 💼 Job Role Matching

The Job Matching module recommends suitable career roles.

Example:

```text
🥇 GenAI Engineer
Match: 94%

🥈 AI Engineer
Match: 90%

🥉 Machine Learning Engineer
Match: 86%

Python Backend Engineer
Match: 82%

Data Scientist
Match: 75%
```

For each role:

- Match Score
- Recommendation Reason
- Missing Skills
- Next Steps

## 📋 Job Description Matcher

Users can paste a job description and compare it against their resume.

The application provides:

- Overall Match Score
- Matching Skills
- Missing Skills
- Resume Weaknesses
- Resume Improvements
- ATS Keyword Suggestions
- Final Recommendation

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application and UI |
| LangChain | LLM application framework |
| Gemini | Large Language Model |
| FAISS | Vector similarity search |
| Sentence Transformers | Text embeddings |
| PyPDF | PDF text extraction |
| Pydantic | Structured output validation |
| PromptTemplate | Prompt management |
| NumPy | Numerical operations |
| python-dotenv | Environment configuration |

---

# 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │    Streamlit UI     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                           ┌────────────────┐
                           │   Resume PDF   │
                           └───────┬────────┘
                                   │
                                   ▼
                           ┌────────────────┐
                           │   PDF Loader   │
                           └───────┬────────┘
                                   │
                                   ▼
                           ┌────────────────┐
                           │    Chunking    │
                           └───────┬────────┘
                                   │
                                   ▼
                       ┌────────────────────────┐
                       │ Sentence Transformers │
                       └───────────┬────────────┘
                                   │
                                   ▼
                           ┌────────────────┐
                           │      FAISS     │
                           │  Vector Store  │
                           └───────┬────────┘
                                   │
                                   ▼
                           ┌────────────────┐
                           │    Retriever   │
                           └───────┬────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │     PromptTemplate  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │        Gemini       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Pydantic Output     │
                         │      Parser         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Career Insights     │
                         └─────────────────────┘
```

---

# 📁 Project Structure

```text
GenAI-Career-Copilot/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
│
├── prompts/
│   ├── resume_prompt.py
│   ├── interview_prompt.py
│   ├── planner_prompt.py
│   ├── ats_prompt.py
│   └── job_description_prompt.py
│
├── services/
│   ├── pdf_service.py
│   ├── chunking_service.py
│   ├── embedding_service.py
│   ├── vector_store_service.py
│   ├── retrieval_service.py
│   ├── llm_service.py
│   ├── analysis_service.py
│   ├── interview_service.py
│   ├── study_plan_service.py
│   ├── job_match_service.py
│   └── job_description_service.py
│
├── parsers/
│   ├── output_parser.py
│   └── study_plan_parser.py
│
├── models/
│   ├── schemas.py
│   └── study_plan_models.py
│
├── ui/
│   ├── resume_analysis.py
│   ├── interview.py
│   ├── study_plan.py
│   ├── job_match.py
│   └── job_description.py
│
├── helper_utils/
│   └── helpers.py
│
├── uploads/
├── assets/
└── screenshots/
```

---

# 🔄 RAG Pipeline

```text
Resume PDF
    ↓
Extract Text
    ↓
Create Chunks
    ↓
Generate Embeddings
    ↓
Store Embeddings in FAISS
    ↓
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Top-K Relevant Chunks
    ↓
PromptTemplate
    ↓
Gemini
    ↓
Pydantic Structured Output
    ↓
Streamlit UI
```

---

# 🧩 LangChain Usage

LangChain is currently used for:

- Gemini integration
- PromptTemplate
- LCEL composition
- Runnable chains
- Output parsers
- Structured generation

Example:

```python
resume_analysis_chain = resume_prompt | llm | parser
```

---

# 📦 Structured Output

The project uses Pydantic models to validate LLM responses.

Example:

```text
ResumeAnalysis
│
├── resume_score
├── ats_score
├── strengths[]
├── weaknesses[]
└── missing_skills[]
```

Interview questions and study plans also use structured and nested Pydantic models.

---

# 💾 Session State

Streamlit session state is used to avoid repeatedly calling the LLM.

Cached results include:

```text
resume_analysis_data
interview_data
study_plan_data
job_matcher_data
job_description_matcher_data
```

The vector index and resume chunks are also maintained during the session.

---

# 📈 Project Progress

## Phase 1 — Foundations ✅

- [x] Python AI foundations
- [x] LLM fundamentals
- [x] Prompt Engineering
- [x] Gemini API
- [x] Hugging Face
- [x] FastAPI basics
- [x] Streamlit
- [x] Embeddings
- [x] FAISS
- [x] RAG
- [x] LangChain basics
- [x] PromptTemplate
- [x] Output Parsers
- [x] Pydantic structured output

## Phase 2 — GenAI Career Copilot 🚀

### Resume Processing

- [x] PDF Upload
- [x] PDF Text Extraction
- [x] Text Chunking
- [x] Embedding Generation
- [x] FAISS Vector Store
- [x] Semantic Retrieval

### Resume Analysis

- [x] Resume Score
- [x] ATS Score
- [x] Strength Analysis
- [x] Weakness Analysis
- [x] Missing Skill Detection
- [x] Structured Output

### Interview Preparation

- [x] Technical Questions
- [x] Behavioral Questions
- [x] Project Questions
- [x] Follow-up Questions
- [x] Difficulty Levels
- [x] Expected Answers

### Career Planning

- [x] Personalized 30-Day Study Plan
- [x] Weekly Goals
- [x] Study Topics
- [x] Mini Projects
- [x] Learning Resources
- [x] Interview Questions
- [x] Weekly Deliverables

### Job Recommendations

- [x] Job Role Matching
- [x] Match Scores
- [x] Recommendation Reasons
- [x] Missing Skills
- [x] Next Steps

### Job Description Matching

- [x] Job Description Input
- [x] Resume + JD Comparison
- [x] Overall Match Score
- [x] Matching Skills
- [x] Missing Skills
- [x] Resume Weaknesses
- [x] Resume Improvements
- [x] ATS Keyword Suggestions

---

# 🚧 Future Roadmap

## Phase 3 — Conversational Career Assistant

- [ ] Chat with Resume
- [ ] Conversation Memory
- [ ] Follow-up Questions
- [ ] Context-Aware Conversations

## Phase 4 — LangGraph Workflow

Planned workflow:

```text
Resume Upload
      ↓
Resume Analysis
      ↓
Skill Gap Analysis
      ↓
Job Role Matching
      ↓
Study Plan
      ↓
Interview Preparation
```

Planned:

- [ ] Graph State
- [ ] Nodes
- [ ] Edges
- [ ] Conditional Routing
- [ ] Workflow State Management

## Phase 5 — Resume Improvement

- [ ] AI Resume Rewriter
- [ ] ATS Bullet Rewriting
- [ ] Professional Summary Generator
- [ ] Project Description Improvement
- [ ] Keyword Optimization

## Phase 6 — Career Dashboard

Planned dashboard metrics:

```text
Resume Score
ATS Score
Missing Skills
Job Match
Study Progress
Interview Readiness
```

---

# 🎯 What This Project Demonstrates

### Generative AI

- LLM Integration
- Prompt Engineering
- Structured Generation
- RAG
- Semantic Search

### LangChain

- PromptTemplate
- LCEL
- Runnable Chains
- Output Parsers
- Gemini Integration

### Vector Search

- Embeddings
- FAISS
- Similarity Search
- Retrieval

### Software Engineering

- Modular Architecture
- Service Layer
- UI Separation
- Type Hints
- Docstrings
- Session State
- Error Handling
- Reusable Components

### AI Application Development

- PDF Processing
- Resume Analysis
- Career Recommendations
- Skill Gap Analysis
- Personalized Learning
- Interview Preparation
- Job Description Matching

---

# 🔐 Environment Variables

Create a `.env` file:

```env
GENAI_API_KEY=your_gemini_api_key
```

Never commit your `.env` file to GitHub.

Use `.env.example`:

```env
GENAI_API_KEY=your_api_key_here
```

---

# ⚙️ Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
GENAI_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

# 🔄 Application Flow

```text
                Upload Resume
                     │
                     ▼
              Process Resume
                     │
                     ▼
              Build FAISS DB
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
     Resume       Interview     Study Plan
    Analysis       Questions
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
                Job Matching
                     │
                     ▼
              JD Job Matching
```

---

# 📚 Learning Philosophy

This project is being developed alongside learning rather than simply copying a finished application.

The focus is on understanding:

1. Why each component is required.
2. How components communicate.
3. How RAG works internally.
4. How LangChain connects LLM components.
5. How structured output is generated and validated.
6. How to organize an AI application into maintainable modules.
7. How to move from a prototype toward production architecture.

The objective is not just to make the application work, but to understand **why it works**.

---

# 📊 Current Status

**🚀 Active Development**

```text
Resume Processing       ████████████████████ 100%
RAG Pipeline            ████████████████████ 100%
Resume Analysis         ████████████████████ 100%
Interview Generator     ████████████████████ 100%
Study Plan              ████████████████████ 100%
Job Matching            ████████████████████ 100%
JD Matching              ████████████████████ 100%

Conversation Memory     ░░░░░░░░░░░░░░░░░░░░   0%
LangGraph Workflow      ░░░░░░░░░░░░░░░░░░░░   0%
Resume Rewriter         ░░░░░░░░░░░░░░░░░░░░   0%
Career Dashboard        ░░░░░░░░░░░░░░░░░░░░   0%
```

---

# ⭐ Project Roadmap

| Phase | Feature | Status |
|---|---|---|
| Phase 1 | Resume Upload & Processing | ✅ |
| Phase 2 | RAG Pipeline | ✅ |
| Phase 3 | Resume Analysis | ✅ |
| Phase 4 | Interview Generator | ✅ |
| Phase 5 | 30-Day Study Plan | ✅ |
| Phase 6 | Job Role Matching | ✅ |
| Phase 7 | Job Description Matcher | ✅ |
| Phase 8 | Conversational Resume Assistant | 🚧 |
| Phase 9 | Conversation Memory | ⏳ |
| Phase 10 | LangGraph Workflow | ⏳ |
| Phase 11 | Resume Rewriter | ⏳ |
| Phase 12 | Career Dashboard | ⏳ |

---

# 💡 Project Vision

GenAI Career Copilot aims to connect:

```text
Resume
   +
AI
   +
RAG
   +
Job Requirements
   +
Skill Gaps
   +
Learning Plan
   +
Interview Preparation
```

into one intelligent career assistant.

---

## 🚀 Built With

**Python • Streamlit • LangChain • Gemini • LangGraph • FAISS • Sentence Transformers • Pydantic • PyPDF**

---

> 🚧 This project is actively evolving as part of my AI Engineer learning journey.
