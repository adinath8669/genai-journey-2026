# 📅 Day 17 – AI Agents

---

# 📚 Topics Learned

- Agent
- Tool
- Tool Calling
- ReAct
- Observation
- Planning

---

# 💡 What I Understood

## 1. What is an Agent?

An Agent is an AI system that can think, decide, and use tools to complete a task. Instead of only answering questions, it first decides whether it needs a tool and then uses the appropriate tool before giving the final response.

Example:

User: `2 + 10`

Agent → Calculator Tool → `12`

---

## 2. What is a Tool?

A Tool is a Python function that the Agent can call to perform a specific task. Tools allow the Agent to do things like calculations, search documents, explain concepts, or generate interview questions.

Example:

- Calculator Tool
- Python Teacher Tool
- Interview Generator Tool

---

## 3. What is Tool Calling?

Tool Calling is the process where the Agent decides which tool should be used based on the user's request.

Example:

User: `Explain decorators`

↓

Agent

↓

Python Teacher Tool

↓

Explanation

↓

Final Answer

The user doesn't choose the tool—the Agent decides automatically.

---

## 4. What is ReAct?

ReAct stands for **Reason + Act**.

Instead of directly answering, the Agent follows these steps:

- Think about the problem.
- Decide if a tool is needed.
- Call the appropriate tool.
- Use the tool's output.
- Generate the final answer.

This makes the Agent more reliable and capable of solving complex tasks.

---

## 5. What is Observation?

Observation is the information returned by a tool after it has been executed.

Example:

Question:

`5 × 8`

Tool Output:

`40`

The Agent observes this result and uses it to generate the final response.

---

## 6. What is Planning?

Planning is the Agent's ability to decide the sequence of actions required to solve a problem.

Example:

User:

"Generate Python interview questions and explain decorators."

Plan:

1. Use Python Teacher Tool.
2. Use Interview Generator Tool.
3. Combine both results.
4. Return the final response.

---

# 🌍 Real-World Applications

- ChatGPT with tool calling
- AI Customer Support
- AI Coding Assistants
- AI Tutors
- Research Assistants
- Personal AI Assistants
- Multi-tool AI Agents

---

# 🤔 What Confused Me

- How does the Agent decide which tool to use?
- Can an Agent use multiple tools for one question?
- How are custom tools created?
- What happens if no suitable tool is available?

---

# ❓ Questions

1. Can an Agent call more than one tool in a single request?
2. How does LangChain decide which tool to select?
3. What is the difference between an Agent and a Chain?
4. Can we create our own custom tools?
5. How do production AI Agents use external APIs?

---

# 🚀 Day 16 Summary

Today I learned that an Agent is more than just an LLM. It can think about the user's request, decide whether a tool is needed, call the correct tool, observe the result, and then generate the final answer. I also learned about Tool Calling, ReAct, Observation, and Planning, which are the foundation of modern AI Agents.