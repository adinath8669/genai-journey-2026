# 📘 Day 13 Notes – LangChain Basics

## What is LangChain?

LangChain is a Python framework that helps developers build AI applications using Large Language Models (LLMs). It provides reusable components to connect prompts, models, retrievers, tools, and memory into complete AI workflows.

---

## Why LangChain Exists

Writing AI applications directly with API calls can become repetitive and difficult to maintain. LangChain provides a structured way to organize prompts, models, retrieval, and other AI components, making applications easier to build and scale.

---

## PromptTemplate

A PromptTemplate is used to create dynamic prompts by inserting user input into a predefined template.

### Example

```python
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words."
)
```

### Benefits

- Reusable prompts
- Cleaner code
- Dynamic input handling
- Easy to modify prompts

---

## Chat Models

Chat Models are LLMs that generate responses based on prompts.

Examples:

- Gemini
- GPT-4
- Claude
- Llama

### Example

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
```

---

## Chains

A Chain connects multiple LangChain components together.

Example:

```
Prompt
   ↓
Chat Model
   ↓
Response
```

Instead of calling everything manually, LangChain executes the workflow in sequence.

---

## Runnable Sequence (`|`)

The `|` operator connects LangChain components together.

Example:

```python
chain = prompt | llm
```

This means:

```
PromptTemplate
        │
        ▼
 Chat Model
        │
        ▼
 Response
```

The output of one component becomes the input of the next.

---

## Advantages of LangChain

- Simple and organized code
- Easy integration with multiple LLMs
- Supports RAG applications
- Built-in prompt management
- Supports chains, memory, agents, and tools
- Easy to scale AI projects

---

## Disadvantages of LangChain

- Extra abstraction over simple API calls
- Learning curve for beginners
- Can feel unnecessary for very small projects
- Frequent updates may introduce breaking changes

---

# LangChain Workflow

```
User Input
      │
      ▼
PromptTemplate
      │
      ▼
Chat Model
      │
      ▼
Response
```

---

# Key Terms

| Term | Description |
|------|-------------|
| LangChain | Framework for building AI applications |
| PromptTemplate | Creates reusable prompts |
| Chat Model | LLM that generates responses |
| Chain | Connects multiple AI components |
| Runnable Sequence (`|`) | Links components together |

---

# Summary

- LangChain is a framework for building LLM applications.
- PromptTemplate creates reusable prompts.
- Chat Models generate AI responses.
- Chains connect components into workflows.
- The `|` operator creates Runnable Sequences.
- LangChain makes AI applications cleaner, modular, and easier to maintain.