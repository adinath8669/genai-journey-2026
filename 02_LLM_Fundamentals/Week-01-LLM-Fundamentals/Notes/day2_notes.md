# 📅 Day 2

## 📚 Topics Learned

* Vocabulary
* Token IDs
* Encoding
* Decoding
* Special Tokens
* Attention Mask

---

## 💡 What I Understood

Today I learned how a tokenizer prepares text before it is sent to an LLM.

I understood that every tokenizer has its own **vocabulary**, which is a collection of all the tokens it knows. Each token is assigned a unique **token ID**.

I learned that **encoding** is the process of converting text into token IDs, and **decoding** is the process of converting those token IDs back into readable text.

I also learned about **special tokens** like `[CLS]`, `[SEP]`, `[PAD]`, and `[UNK]`. These tokens help the model understand the structure of the input, separate sentences, handle padding, and deal with unknown words.

Finally, I understood what an **attention mask** is. It tells the model which tokens are actual input (`1`) and which are just padding (`0`), so the model only focuses on meaningful information.

---

## 🤔 What Confused Me

* I still want to understand how the tokenizer decides where to split words into tokens.
* I want to know how different models have different vocabularies.
* I'm curious about how token IDs are converted into meaningful representations inside the model.

---

## ❓ Questions

1. How is a tokenizer's vocabulary created?
2. Why do different models use different tokenizers?
3. Can the same word have different token IDs in different models?
4. What happens if a word is not in the vocabulary?
5. How does the model use token IDs to understand the meaning of a sentence?

---

## ✅ Day 2 Summary

Today I learned how text is converted into a format that an LLM can understand. I understood the concepts of vocabulary, token IDs, encoding, decoding, special tokens, and attention masks. Now I know that before an AI model processes any text, it first converts it into numbers and uses additional information like special tokens and attention masks to understand the input correctly.
