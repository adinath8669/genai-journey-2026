# 📅 Day18 – LangGraph Basics

---

# 📚 Topics Learned

* LangGraph
* State
* Nodes
* Edges
* Conditional Edges
* Workflow
* Multi-Agent Systems

---

# 💡 What I Understood

## 1. What is LangGraph?

LangGraph is a framework built on top of LangChain that helps create AI workflows. Instead of running everything in a single chain, it connects multiple steps (nodes) together like a graph. This makes it easier to build complex AI applications with memory, decision-making, and multiple agents.

---

## 2. What is State?

State is the data that is shared between different nodes in the graph. It stores information like user input, chat history, retrieved documents, or AI responses. As the workflow moves from one node to another, the state gets updated.

Example:

```text
User Question
↓

State
{
question,
chat_history,
documents,
answer
}
```

---

## 3. What are Nodes?

Nodes are individual steps or functions in a LangGraph workflow. Each node performs one specific task and updates the state.

Examples:

* Read User Input
* Retrieve Documents
* Generate AI Response
* Save Chat History

Think of a node as one block in the workflow.

---

## 4. What are Edges?

Edges are connections between nodes. They define the order in which the workflow executes.

Example:

```text
User Input
      │
      ▼
Retriever
      │
      ▼
LLM
      │
      ▼
Final Answer
```

The arrows between nodes are called edges.

---

## 5. What are Conditional Edges?

Conditional edges allow the workflow to make decisions. Based on a condition, the graph can follow different paths.

Example:

```text
          Question
              │
      Is it Math?
        /       \
      Yes       No
      │          │
Calculator    LLM
      │          │
      └──────┬───┘
             ▼
        Final Answer
```

This makes AI applications smarter because they can choose different actions based on the user's request.

---

## 6. What is a Workflow?

A workflow is the complete sequence of nodes connected by edges to accomplish a task.

Example:

```text
User Question
      │
      ▼
Retrieve Context
      │
      ▼
Generate Answer
      │
      ▼
Store Memory
      │
      ▼
Return Response
```

LangGraph helps organize these workflows in a clean and structured way.

---

## 7. What are Multi-Agent Systems?

A Multi-Agent System contains multiple AI agents, where each agent is responsible for a specific task.

Example:

* Research Agent → Searches for information
* Math Agent → Solves calculations
* Coding Agent → Writes code
* Review Agent → Checks the final answer

The agents work together to solve more complex problems.

---

# 🌍 Real-World Applications

* AI Customer Support
* AI Research Assistant
* AI Coding Assistant
* Healthcare AI
* Multi-step Workflow Automation
* AI Travel Planner
* Multi-Agent Business Assistants

---

# 🤔 What Confused Me

* How is LangGraph different from LangChain?
* How is state shared between nodes?
* When should I use conditional edges?
* How do multiple agents communicate with each other?

---

# ❓ Questions

1. When should I choose LangGraph instead of LangChain?
2. Can a workflow have multiple conditional edges?
3. Where is the state stored during execution?
4. How do multiple agents share information?
5. Can LangGraph be combined with RAG and memory?

---

# 🚀 Day Summary

Today I learned that LangGraph is used to build AI workflows using nodes and edges. The state stores information that moves through the workflow, while conditional edges allow the graph to make decisions. I also learned that multiple AI agents can work together in a single application, with each agent handling a different task.
