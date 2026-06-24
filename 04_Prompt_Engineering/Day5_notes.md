# 📅 Day 5

## 📚 Topics Learned

* Prompt Engineering
* Zero-shot Prompting
* One-shot Prompting
* Few-shot Prompting
* System Prompt
* User Prompt
* Role Prompting

---

## 💡 What I Understood

Today I learned that the quality of an AI's response depends a lot on how the prompt is written. A clear and detailed prompt usually gives better results than a vague one.

I understood that **Prompt Engineering** is the skill of writing effective prompts to get accurate and useful responses from an LLM.

I learned about different prompting techniques. In **Zero-shot prompting**, we ask the model to perform a task without giving any examples. In **One-shot prompting**, we provide one example, and in **Few-shot prompting**, we give multiple examples so the model understands the pattern better.

I also learned the difference between a **System Prompt** and a **User Prompt**. A system prompt tells the model how it should behave throughout the conversation, while a user prompt is the actual question or instruction given by the user.

Finally, I learned about **Role Prompting**, where we ask the model to act as a specific expert, such as a teacher, doctor, or software engineer. This helps the model generate responses that match that role.

---

## 🌍 Real-World Applications

* Customer support chatbots use system prompts to maintain a consistent tone.
* AI coding assistants use role prompting to act like experienced software developers.
* Content writers use prompt engineering to generate blogs, emails, and social media posts.
* Companies use few-shot prompting to teach AI a specific response format.
* Educational AI tools use role prompting to explain concepts like a teacher.

---

## 🤔 What Confused Me

* I want to know when to use Zero-shot, One-shot, or Few-shot prompting in real projects.
* I'm curious about how long a system prompt can be.
* I want to understand how companies design prompts for production AI applications.

---

## ❓ Questions

1. How do we decide whether to use Zero-shot, One-shot, or Few-shot prompting?
2. Can a system prompt be changed during a conversation?
3. What are the best practices for writing effective prompts?
4. How do companies test and improve prompts in production?
5. Can prompt engineering improve the performance of every LLM?

---

## ✅ Day 5 Summary

Today I learned that writing a good prompt is an important skill when working with LLMs. I understood different prompting techniques like Zero-shot, One-shot, and Few-shot, along with System Prompts, User Prompts, and Role Prompting. These techniques help generate more accurate, relevant, and consistent responses from AI models.


---

# Prompting Examples

## 1. Zero-shot Prompting

In zero-shot prompting, we give the model only the task without any examples.

**Example:**

**Prompt:**

```
Translate the following sentence into French:

"I love learning AI."
```

**Output:**

```
J'aime apprendre l'IA.
```

---

## 2. One-shot Prompting

In one-shot prompting, we provide one example before asking the model to perform the task.

**Prompt:**

```
Example:
English: Hello
French: Bonjour

Now translate:

English: Good Morning
```

**Output:**

```
French: Bonjour
```

---

## 3. Few-shot Prompting

In few-shot prompting, we provide multiple examples so the model understands the pattern better.

**Prompt:**

```
Example 1:
Positive: I love this movie.

Example 2:
Negative: This food tastes terrible.

Example 3:
Positive: This phone is amazing.

Now classify:

"This laptop is very slow."
```

**Output:**

```
Negative
```

---

## 4. Role Prompting

In role prompting, we tell the model to behave like a specific person or expert.

**Prompt:**

```
You are an experienced Python teacher.

Explain the difference between a list and a tuple in simple words.
```

**Output:**

```
A list is mutable, which means you can change its elements after creating it. A tuple is immutable, so its elements cannot be changed once it is created.
```

---

## 5. System Prompt

A system prompt sets the overall behavior or rules for the AI before the user asks questions.

**System Prompt:**

```
You are a helpful AI assistant.

Always explain concepts in simple language with real-world examples.

Keep answers short and easy to understand.
```

**User Prompt:**

```
What is Machine Learning?
```

**Output:**

```
Machine Learning is a branch of AI where computers learn patterns from data instead of being explicitly programmed. For example, an email spam filter learns to identify spam emails by analyzing many examples.
```
