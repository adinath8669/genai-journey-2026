# 📅 Day 4

## 📚 Topics Learned

* Next Token Prediction
* Probability Distribution
* Temperature
* Top-k Sampling
* Top-p Sampling
* Hallucination

---

## 💡 What I Understood

Today I learned that an LLM does not generate full sentences at once. Instead, it generates text step by step by predicting the **next token** using probability.

I understood that for every step, the model looks at all possible tokens and assigns a **probability distribution** to them. The token with the highest probability (or sampled based on settings) is chosen as output.

I also learned about **temperature**, which controls randomness. Low temperature makes responses more focused and predictable, while high temperature makes responses more creative and random.

I understood **Top-k sampling**, where the model only considers the top k most probable tokens, and **Top-p sampling**, where it selects tokens until the cumulative probability reaches a threshold like 0.9 or 0.95.

Finally, I learned about **hallucination**, where the model generates information that sounds correct but is actually false, because it is predicting likely text instead of verifying facts.

---

## 🌍 Real-World Applications

* Chatbots use next-token prediction to generate responses in real time.
* Search engines and AI assistants use probability-based ranking to improve results.
* Temperature control is used in creative writing tools vs factual assistants.
* Top-k and Top-p are used in production systems to balance creativity and accuracy.
* Hallucination awareness is important in medical, legal, and financial AI systems.

---

## 🤔 What Confused Me

* I still want to clearly understand when to use Top-k vs Top-p in real applications.
* I am not fully clear how probability is calculated for each token.
* I want to understand why hallucinations happen even when models are trained on large datasets.

---

## ❓ Questions

1. How does the model calculate probability for each token?
2. What is the exact difference between Top-k and Top-p in real systems?
3. Why does increasing temperature sometimes reduce accuracy?
4. Can hallucination be completely removed from LLMs?
5. How do companies control hallucinations in production AI systems?

---

## ✅ Day 4 Summary

Today I understood that LLMs generate text using probability-based next token prediction. I also learned how temperature, Top-k, and Top-p control randomness in outputs. Finally, I learned that hallucinations happen because models predict likely text instead of verifying real facts, which is a key limitation of LLMs.
