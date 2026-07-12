# 📅 Day 16 – Conversational RAG

---

# 📚 Topics Learned

- Conversational RAG
- Memory
- Retriever
- Context Window
- Multi-turn Conversation
- Follow-up Questions

---

# 💡 What I Understood

## 1. What is Conversational RAG?

Conversational RAG (Retrieval-Augmented Generation) is a RAG system that can remember previous conversations while answering questions.

It combines:
- Conversation Memory
- Retriever
- Large Language Model (LLM)

Instead of answering each question independently, it uses both the chat history and the retrieved document context to generate better answers.

---

## 2. What is Memory?

Memory stores the conversation history between the user and the AI.

The LLM itself does not permanently remember anything. My application saves previous messages and sends them with every new request.

This allows the AI to answer follow-up questions correctly.

Example:

User:
> My favorite language is Python.

User:
> Why do I like it?

AI understands that **"it"** refers to **Python** because of the stored conversation history.

---

## 3. What is a Retriever?

A retriever is responsible for finding the most relevant information from the vector database.

Steps:
1. Convert the user's question into an embedding.
2. Search the vector database.
3. Retrieve the most similar chunks.
4. Send those chunks to the LLM.

The retriever helps the model answer questions using the uploaded documents instead of relying only on its training data.

---

## 4. What is a Context Window?

A context window is the maximum amount of information an LLM can process in a single request.

It includes:
- System message
- Conversation history
- Retrieved document chunks
- User's current question

If the total input exceeds the context window, older messages or extra text may need to be removed.

---

## 5. What is a Multi-turn Conversation?

A multi-turn conversation is a conversation where multiple questions and answers are connected.

Example:

User:
> What is Machine Learning?

AI:
> Machine Learning is a branch of AI.

User:
> Give me an example.

The AI understands that **"it"** refers to Machine Learning because the previous conversation is included in the chat history.

---

## 6. Why Do Follow-up Questions Work?

Follow-up questions work because the application sends the previous conversation along with the current question.

The LLM uses:
- Conversation history (memory)
- Retrieved document context (RAG)

Together, these provide enough context for the model to understand references like:
- it
- this
- that
- they

Without memory, the AI would treat every question as a completely new conversation.

---

# 🌍 Real-World Applications

- ChatGPT
- PDF Chatbots
- Customer Support Bots
- AI Tutors
- Medical Assistants
- Legal Document Assistants
- Company Knowledge Base Chatbots

---

# 🤔 What Confused Me

- How much conversation history should be stored?
- What happens when the context window becomes full?
- How do large AI assistants manage very long conversations?

---

# ❓ Questions

1. How can we store conversation history in a database?
2. What is the difference between short-term and long-term memory?
3. How do vector databases improve RAG performance?
4. How can we reduce token usage in long conversations?
5. How do production AI assistants manage memory efficiently?

---
