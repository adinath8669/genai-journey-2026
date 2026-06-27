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
