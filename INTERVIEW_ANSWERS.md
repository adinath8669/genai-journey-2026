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
