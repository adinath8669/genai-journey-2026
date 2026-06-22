# 📅 Day 3

## 📚 Topics Learned

* Vector
* Embedding
* Semantic Similarity
* Cosine Similarity

---

## 💡 What I Understood

Today I learned that AI cannot understand the meaning of words just by looking at their token IDs. Instead, it converts words into **vectors**, which are lists of numbers that represent their meaning.

I understood that an **embedding** is simply the vector representation of a word, sentence, or document. Words with similar meanings have similar embeddings, so they are placed close to each other in vector space.

I also learned about **semantic similarity**. It means comparing words based on their meaning instead of their spelling or token IDs. For example, "doctor" and "physician" have similar meanings, so their embeddings are close together.

Finally, I learned about **cosine similarity**. It is used to compare two embeddings and check how similar they are. If the vectors point in almost the same direction, the meanings are similar. If they point in different directions, the meanings are different.

---

## 🌍 Real-World Applications

* Search engines use embeddings to find results with similar meaning, not just exact words.
* Chatbots use embeddings to better understand user questions.
* RAG (Retrieval-Augmented Generation) uses embeddings to find relevant documents before generating an answer.
* Recommendation systems use embeddings to suggest similar movies, products, or songs.
* AI can compare documents, articles, or resumes based on their meaning instead of exact keywords.

---

## 🤔 What Confused Me

* I still want to understand how embeddings are actually created during model training.
* I want to know how many numbers are usually present in an embedding vector.
* I'm curious about how sentences and entire documents are converted into a single embedding.

---

## ❓ Questions

1. How does an AI model generate embeddings during training?
2. Why do different embedding models produce different vectors for the same text?
3. Can two different words have almost the same embedding?
4. How are embeddings stored and searched in vector databases?
5. Why is cosine similarity preferred over simply comparing token IDs?

---

## ✅ Day 3 Summary

Today I learned that token IDs only identify words, but embeddings represent their meaning. I understood that vectors help AI compare words based on semantic meaning instead of numbers. I also learned that cosine similarity is used to measure how similar two embeddings are. These concepts are important because they are the foundation of semantic search, RAG, recommendation systems, and many modern AI applications.
