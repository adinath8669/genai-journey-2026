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

