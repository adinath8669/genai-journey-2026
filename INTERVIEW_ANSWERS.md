# LLM Fundamentals – Interview Questions & Answers

---

# 📅 Day 1

## Q1. What is a Large Language Model (LLM)?

A Large Language Model (LLM) is an AI model that is trained on a huge amount of text data. Because of this training, it can understand questions, generate text, summarize information, and have conversations like humans.

---

## Q2. What is the difference between Machine Learning and an LLM?

Machine Learning is a broad field where computers learn patterns from data. An LLM is a type of Machine Learning model that is specially trained on text data to understand and generate human language. In simple words, every LLM uses Machine Learning, but not every Machine Learning model is an LLM.

---

## Q3. What is a Token?

A token is a small piece of text that the AI processes. It can be a complete word, part of a word, or even a punctuation mark. Instead of reading full sentences, the model reads tokens.

---

## Q4. What is Tokenization?

Tokenization is the process of breaking text into smaller pieces called tokens. Before the model understands any text, it first converts it into tokens.

---

## Q5. What is a Context Window?

A context window is the amount of information the model can remember while generating a response. If the conversation becomes longer than the context window, the model may not remember the oldest parts.

---

# 📅 Day 2

## Q1. Why is tokenization required?

Tokenization is required because AI models cannot understand plain text directly. The text must first be broken into tokens and converted into numbers so the model can process it.

---

## Q2. What is the difference between a token and a token ID?

A token is a piece of text, while a token ID is the unique number given to that token. The tokenizer converts tokens into token IDs because the model works with numbers instead of text.

---

## Q3. What is a vocabulary?

A vocabulary is the list of all the tokens that a tokenizer knows. Every token in the vocabulary has its own unique token ID.

---

## Q4. Why do tokenizers use special tokens?

Special tokens help the model understand the structure of the input. For example, `[CLS]` is used for classification tasks, `[SEP]` separates sentences, `[PAD]` is used for padding, and `[UNK]` represents unknown words.

---

## Q5. What is an attention mask?

An attention mask tells the model which tokens are actual input and which are just padding. Tokens marked with `1` are processed, while tokens marked with `0` are ignored.

---

# 📅 Day 3

## Q1. What is an embedding?

An embedding is the vector representation of a word, sentence, or document. It helps the AI understand the meaning of text instead of just reading it as words.

---

## Q2. Why do we need embeddings?

We need embeddings because token IDs only identify words; they don't tell the model what the words mean. Embeddings capture the meaning of words, which helps the model understand similarities between them.

---

## Q3. What is the difference between a token ID and an embedding?

A token ID is just a unique number used to identify a token. An embedding is a vector that represents the meaning of that token. Token IDs help identify words, while embeddings help the model understand them.

---

## Q4. What is cosine similarity?

Cosine similarity is a way to compare two embeddings and check how similar they are. If the vectors point in a similar direction, their meanings are similar. If they point in different directions, their meanings are different.

---

## Q5. Where are embeddings used in real-world AI applications?

Embeddings are used in many AI applications like semantic search, chatbots, recommendation systems, Retrieval-Augmented Generation (RAG), document search, and question-answering systems because they help AI understand the meaning of text.

---

📅 Day 4
## Q1. What is next-token prediction?

Next-token prediction is the process where the model predicts the next word/token based on previous tokens using probability.

---

## Q2. What is probability distribution in LLMs?

It is the list of probabilities assigned to all possible next tokens. The model selects one based on these probabilities.

---

## Q3. What is temperature?

Temperature controls randomness. Low temperature gives stable answers, high temperature gives more creative answers.

---


## Q4. What is Top-k and Top-p sampling?
Top-k: selects from the top k most likely tokens
Top-p: selects from smallest set of tokens whose probability adds up to a threshold (like 0.9)

---

## Q5. Why do LLMs hallucinate?

LLMs hallucinate because they generate text based on probability, not real-world fact checking. So they can produce believable but incorrect answers.

---

📅 Day 5
## Q1. What is Prompt Engineering?

Prompt Engineering is the process of writing clear and effective prompts to get the best possible response from an LLM. A good prompt helps the model understand exactly what we want.

---

## Q2. What is the difference between Zero-shot and Few-shot prompting?

In Zero-shot prompting, we ask the model to perform a task without giving any examples.

In Few-shot prompting, we provide a few examples before asking the actual question. These examples help the model understand the pattern and usually produce better results.

---

## Q3. What is a System Prompt?

A system prompt is a set of instructions given to the model before the user prompt. It defines the model's behavior, tone, and rules throughout the conversation.

---

## Q4. Why is role prompting useful?

Role prompting tells the model to act as a specific expert or person, such as a teacher, doctor, or software engineer. This helps the model generate responses that match that role and are more relevant to the user's request.

---

## Q5. Can prompt engineering completely eliminate hallucinations? Why or why not?

No. Prompt engineering can reduce hallucinations by giving the model clear instructions and enough context, but it cannot remove them completely. LLMs still generate responses by predicting the next token, so they can sometimes produce incorrect or made-up information.

---

# 🎤 Day 6 Interview Questions – API Basics

## Q1. What is an API?

An **API (Application Programming Interface)** allows two software applications to communicate. It lets Python send requests to an AI model and receive responses.

---

## Q2. How does Python communicate with an LLM?

Python uses an API and an SDK (like the OpenAI SDK) to send prompts to an LLM and receive generated responses.

---

## Q3. What is a chat completion?

A **chat completion** is the AI-generated response based on a conversation containing system, user, and assistant messages.

---

## Q4. Why do we use system prompts in APIs?

System prompts define the AI's role, behavior, and response style, helping it produce consistent and relevant answers.

---

## Q5. What happens when you send a request to OpenAI?


```text
Python Program
      ↓
 OpenAI SDK
      ↓
 OpenAI API
      ↓
   AI Model
      ↓
 Generated Response
```

The API receives the prompt, the model processes it, generates a response, and sends it back to your Python program.

---

# 🎤 Day 7 Interview Questions – Hugging Face

## Q1. What is Hugging Face?


Hugging Face is an open-source AI platform that provides pre-trained machine learning and Large Language Models (LLMs). It offers libraries like **Transformers**, **Datasets**, and **Tokenizers**, along with the **Model Hub**, where developers can discover, use, and share AI models for tasks such as text generation, translation, summarization, image processing, and speech recognition.

---

## Q2. What is the Transformers library?

The **Transformers** library is a Python library developed by Hugging Face that provides easy access to thousands of pre-trained transformer models such as **BERT**, **GPT**, **T5**, and **Llama**. It simplifies loading models, tokenization, training, fine-tuning, and inference with just a few lines of code.

---

## Q3. What is a pipeline?

A **pipeline** is a high-level API in the Transformers library that makes it easy to use pre-trained models without writing complex code. It automatically downloads the model, loads the tokenizer, preprocesses the input, performs inference, and returns the output.

**Example:**

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love learning AI!")
print(result)
```

---

## Q4. What is the difference between API-based models and local models?

| API-Based Models                     | Local Models                                |
| ------------------------------------ | ------------------------------------------- |
| Run on cloud servers.                | Run on your own computer.                   |
| Require an internet connection.      | Can work offline after downloading.         |
| Usually require an API key.          | No API key is needed.                       |
| Cloud provider manages the hardware. | You manage your own hardware and resources. |
| Easier to get started.               | Offers more control and privacy.            |

---

## Q5. Name three popular open-source LLMs.

1. Llama (Meta)
2. Mistral
3. Gemma (Google)

Other popular open-source models include Falcon, Qwen, DeepSeek, and Phi.

---
# 🎤 Day 8 Interview Questions – LLM Parameters

## Q1. What does temperature control in an LLM?

Temperature controls the randomness of the model's output. A low temperature gives more predictable answers, while a high temperature produces more creative and varied responses.

---

## Q2. What is the difference between Top-k and Top-p?


* **Top-k:** Chooses the next token from the top **k** most likely options.
* **Top-p:** Chooses from the smallest group of tokens whose cumulative probability reaches **p** (e.g., 0.9).

---

## Q3. Why do we use `max_output_tokens`?

`max_output_tokens` limits the maximum length of the generated response, helping control response size, cost, and generation time.

---

## Q4. When would you use a low temperature?

Use a low temperature for tasks that require accuracy and consistency, such as coding, mathematics, data analysis, or factual question answering.

---

## Q5. Can changing the temperature make an LLM smarter?

No. Changing the temperature only affects the randomness and creativity of the output. It does not change the model's knowledge or intelligence.

---
# 🎤 Day 09 Interview Questions – FastAPI Basics

## Q1. What is FastAPI?
*
FastAPI is a modern, high-performance Python framework used to build REST APIs. It is fast, easy to use, and automatically generates API documentation.

---

## Q2. What is the difference between GET and POST?

* **GET:** Retrieves data from the server.
* **POST:** Sends data to the server to create or process a resource.

---

## Q3. What is a path parameter?

A path parameter is a value included in the URL that is used to identify a specific resource.

**Example:**

```text
/user/10
```

Here, `10` is the path parameter.

---

## Q4. What is a request body?

A request body is the JSON data sent by the client to the server, usually with a POST request.

**Example:**

```json
{
  "question": "What is AI?"
}
```

---

## Q5. Why is FastAPI popular for AI backends?

FastAPI is popular because it is fast, supports asynchronous programming, validates data using Pydantic, generates Swagger documentation automatically, and integrates easily with AI models like Gemini and OpenAI.

---

#  Day 10 Interview Questions – Streamlit

## Q1. What is Streamlit?

**Answer:**
Streamlit is an open-source Python framework used to build interactive web applications for data science, machine learning, and AI with minimal code.

---

## Q2. What is Session State?

**Answer:**
Session State stores data during a user's session, allowing information like chat history, user inputs, and settings to persist across interactions.

---

## Q3. What is the difference between Streamlit and FastAPI?

**Answer:**

* **Streamlit:** Used to build interactive user interfaces for AI and data apps.
* **FastAPI:** Used to build backend REST APIs that process requests and return data.

---

## Q4. Why is Streamlit popular in AI?

**Answer:**
Streamlit is popular because it lets developers quickly create AI demos and applications without needing HTML, CSS, or JavaScript. It integrates easily with machine learning and LLM libraries.

---

## Q5. Can Streamlit replace FastAPI?

**Answer:**
No. Streamlit is designed for building front-end web apps, while FastAPI is designed for creating backend APIs. They are often used together in AI applications.

---

# 🎤 Day 11 Interview Questions – Vector Databases

## Q1. What is a Vector Database?

**Answer:**  
A Vector Database stores embeddings (vectors) and performs fast similarity searches to find data with similar meanings instead of exact keyword matches.

---

## Q2. What is Semantic Search?

**Answer:**  
Semantic Search finds information based on the meaning and context of a query rather than exact words. It uses embeddings to retrieve relevant results.

---

## Q3. What is FAISS?

**Answer:**  
FAISS (Facebook AI Similarity Search) is an open-source library developed by Meta for efficient similarity search and clustering of dense vectors. It is widely used in AI and RAG applications.

---

## Q4. What is the difference between keyword search and semantic search?

**Answer:**

| Keyword Search | Semantic Search |
|---------------|-----------------|
| Matches exact words | Understands meaning and context |
| Uses SQL or text indexing | Uses embeddings and vector search |
| Misses similar terms | Finds related concepts |
| Less effective for AI | Ideal for AI and RAG systems |

---

## Q5. Why do RAG systems use embeddings?

**Answer:**  
RAG systems use embeddings to convert documents and user queries into vectors. These vectors allow the system to retrieve the most semantically relevant documents from a vector database before generating an answer.

---

# 🎤 Day 12 Interview Questions – RAG (Retrieval-Augmented Generation)

## Q1. What is RAG?

**Answer:**
RAG (Retrieval-Augmented Generation) is an AI technique that retrieves relevant information from external documents before sending it to an LLM. This helps the model generate more accurate and context-aware answers.

---

## Q2. Why do we split documents into chunks?

**Answer:**
Large documents are divided into smaller chunks because LLMs have context limits. Chunking also improves retrieval accuracy by searching smaller, more relevant pieces of text.

---

## Q3. What is retrieval?

**Answer:**
Retrieval is the process of finding the most relevant document chunks from a vector database based on the user's query using similarity search.

---

## Q4. Why do we pass retrieved chunks to the LLM?

**Answer:**
Retrieved chunks provide the LLM with relevant context so it can answer questions based on the document instead of relying only on its pre-trained knowledge.

---

## Q5. Can RAG update an LLM's knowledge without retraining?

**Answer:**
Yes. RAG updates the information available to the LLM by retrieving new documents from a vector database. There is no need to retrain the model.

---



# 🎤 Day 14 – LangChain Interview Questions

## Q1. What is LangChain?

**Answer:**

LangChain is an open-source framework for building applications powered by Large Language Models (LLMs). It helps developers connect LLMs with prompts, documents, databases, APIs, and other tools using reusable components.

---

## Q2. Why do we use PromptTemplate?

**Answer:**

PromptTemplate helps create dynamic prompts by inserting user input into a predefined template. It keeps prompts organized, reusable, and easier to maintain instead of writing long prompt strings manually.

---

## Q3. What is a Chain?

**Answer:**

A Chain is a sequence of connected components where the output of one component becomes the input of the next. For example:

User Input → PromptTemplate → LLM → Output

Chains simplify AI workflows by combining multiple steps into one pipeline.

---

## Q4. What is RunnableSequence (`|`)?

**Answer:**

The `|` operator in LangChain creates a RunnableSequence by connecting components together.

Example:

```python
chain = prompt | llm
```

Here, the prompt is passed to the LLM automatically. It provides a clean and readable way to build AI pipelines.

---

## Q5. Can LangChain work with different LLM providers?

**Answer:**

Yes. LangChain supports multiple LLM providers, including:

- Google Gemini
- OpenAI (ChatGPT)
- Anthropic Claude
- Ollama (Local Models)
- Hugging Face
- Groq
- Mistral AI

This allows developers to switch providers with minimal code changes.

---
# 🎤 Day 14 – Output Parsers Interview Questions

## Q1. What is an Output Parser?

**Answer:**

An Output Parser is a LangChain component that converts the raw text generated by an LLM into a structured format such as JSON or a Python object. It makes AI responses easier to process programmatically.

---

## Q2. Why do AI applications prefer JSON responses?

**Answer:**

JSON responses are structured, consistent, and easy for applications to read. They allow developers to extract specific fields without manually parsing text, making AI systems more reliable.

---

## Q3. What is PromptTemplate?

**Answer:**

PromptTemplate is a LangChain component used to create reusable and dynamic prompts. It inserts user input into predefined templates, making prompts cleaner and easier to maintain.

---

## Q4. What is the benefit of structured output?

**Answer:**

Structured output provides predictable and organized responses. It simplifies data extraction, validation, and integration with databases, APIs, and user interfaces.

---

## Q5. Can an LLM always generate valid JSON?

**Answer:**

No. LLMs can sometimes produce invalid or incomplete JSON. Output Parsers and validation tools like `PydanticOutputParser` help enforce the expected format and detect errors.

---
# 🎤 Day 15 – Interview Questions

---

## Q1. What is a HumanMessage?

A HumanMessage represents the input given by the user. Every question or instruction from the user is stored as a HumanMessage before it is sent to the LLM.

---

## Q2. What is an AIMessage?

An AIMessage is the response generated by the LLM. After the model processes the user's request, its reply is stored as an AIMessage.

---

## Q3. What is a SystemMessage?

A SystemMessage contains instructions that define how the AI should behave during the conversation. It sets the model's role, tone, and rules before any user messages are processed.

---

## Q4. What is the difference between a stateless and stateful AI application?

A **stateless** AI application does not remember previous conversations. Every request is treated as a new request.

A **stateful** AI application stores conversation history and sends it with every new request, allowing the AI to respond with context and remember earlier parts of the conversation.

---

## Q5. Why can't an LLM remember previous conversations automatically?

An LLM is stateless by default. After generating a response, it does not permanently store the conversation. If we want the model to remember previous messages, our application must save the conversation history and include it in each API request.

---

| Concept              | My Understanding                                            |
| -------------------- | ----------------------------------------------------------- |
| Memory               | Previous conversation stored by the application.            |
| Conversation History | Collection of all user and AI messages.                     |
| HumanMessage         | Message sent by the user.                                   |
| AIMessage            | Response generated by the AI.                               |
| SystemMessage        | Instructions that define the AI's behavior.                 |
| Stateless            | AI does not remember previous conversations.                |
| Stateful             | AI uses stored conversation history to answer with context. |

---

## 💡 Interview Tip

A common interview question is: **"Does ChatGPT actually remember conversations?"**

A good answer is:

> "No. The LLM itself is stateless. The application stores the conversation history and sends it with every new request. That's why it appears as if the AI remembers previous messages."


# 🎤 Day 16 – Conversational RAG Interview Questions

---

## Q1. What is Conversational RAG?

Conversational RAG (Retrieval-Augmented Generation) is a RAG system that can remember previous conversations while answering questions. It combines document retrieval, an LLM, and chat history to generate context-aware responses. This allows users to ask follow-up questions naturally without repeating all the details.

---

## Q2. How is Conversational RAG different from traditional RAG?

Traditional RAG only uses the user's current question to retrieve relevant information from documents. It doesn't consider previous conversations.

Conversational RAG uses both the current question and the conversation history. This helps the AI understand the context and answer follow-up questions more accurately.

---

## Q3. Why is chat history important?

Chat history helps the AI understand the context of the conversation. It remembers what the user asked earlier and what the AI replied. This makes the conversation more natural and allows the user to ask follow-up questions without repeating previous information.

---

## Q4. What happens if we don't include previous messages?

If previous messages are not included, the AI treats every question as a new conversation. It loses the context and may give incorrect or incomplete answers to follow-up questions because it doesn't know what was discussed earlier.

Example:

**User:** My favorite programming language is Python.

**User:** What is my favorite programming language?

Without chat history:

**AI:** I don't know.

With chat history:

**AI:** Your favorite programming language is Python.

---

## Q5. How would you improve a Conversational RAG system for production?

For a production-ready Conversational RAG system, I would:

* Store chat history in a database instead of memory.
* Use better chunking and retrieval strategies.
* Add conversation summarization for long chats.
* Cache embeddings and vector databases for better performance.
* Implement authentication and session management.
* Add streaming responses for a better user experience.
* Monitor retrieval quality and optimize prompts to reduce hallucinations.

---

# 📝 Quick Revision

| Concept                 | My Understanding                                                        |
| ----------------------- | ----------------------------------------------------------------------- |
| Conversational RAG      | RAG + Conversation Memory                                               |
| Traditional RAG         | Retrieves context only from documents                                   |
| Conversational RAG      | Retrieves context from documents and previous conversation              |
| Chat History            | Stores previous user and AI messages                                    |
| Production Improvements | Database, caching, summarization, better retrieval, security, streaming |

---



# 🎤 Day 17 – AI Agents Interview Questions

---

## Q1. What is an AI Agent?

An AI Agent is an application that uses an LLM to understand a user's request, decide what action to take, use the required tools if needed, and then generate the final response. Unlike a normal chatbot, an AI Agent can perform tasks using external tools.

---

## Q2. What is a Tool?

A Tool is a Python function or external service that an AI Agent can use to perform specific tasks. Tools allow the agent to do things that an LLM cannot do on its own, such as calculations, searching documents, or calling APIs.

---

## Q3. What is Tool Calling?

Tool Calling is the process where an AI Agent automatically selects and executes the appropriate tool based on the user's request. The LLM decides which tool to use, sends the required input to that tool, receives the result, and then generates the final response.

---

## Q4. Can an LLM perform calculations accurately without tools?

No. An LLM predicts the next token based on probability and may make mistakes in calculations. For accurate mathematical operations, it is better to use a calculator tool or another specialized tool instead of relying only on the LLM.

---

## Q5. Give three examples of tools an AI agent might use.

Some common tools used by AI agents are:

- **Calculator Tool** – Performs mathematical calculations.
- **Python Teacher Tool** – Explains Python concepts and programming topics.
- **Interview Generator Tool** – Generates interview questions for a given topic.

Other examples include:
- Weather API Tool
- Web Search Tool
- PDF Reader Tool
- Database Query Tool
- Email Sender Tool

---

**"What is the difference between an LLM and an AI Agent?"**

**Answer:**

An **LLM** only generates text based on the input it receives. It cannot directly perform actions like calculations, web searches, or database queries.

An **AI Agent** uses an LLM as its brain but can also use external tools to perform real-world tasks. The agent decides when to call a tool, executes it, and then uses the result to provide a more accurate and useful response.