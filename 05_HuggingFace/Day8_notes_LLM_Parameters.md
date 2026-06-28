# 📝 Day 8 Notes – LLM Parameters

## 1. What is Temperature?

**Temperature** controls the randomness of an LLM's output.

* **Low (0.0–0.3):** More accurate and predictable
* **Medium (0.5–0.7):** Balanced responses
* **High (0.8–1.5):** More creative and diverse

---

## 2. Top-k

**Top-k** limits the model to choosing the next token from the **top K most likely tokens**.

**Example:**

* Top-k = 10 → Select from the 10 most probable words.

---

## 3. Top-p (Nucleus Sampling)

**Top-p** selects the next token from the **smallest group of tokens whose total probability reaches p** (e.g., 0.9).

* More flexible than Top-k.
* The number of candidate tokens changes dynamically.

---

## 4. Max Tokens

**Max Tokens** (or `max_output_tokens`) limits the maximum number of tokens the model can generate.

**Why use it?**

* Controls response length
* Reduces API cost
* Improves response time

---

## 5. Stop Sequences

**Stop Sequences** are words or characters that tell the model **when to stop generating text**.

**Example:**

```text
Stop Sequence: "END"
```

If the model generates **END**, it immediately stops.

---

# ⚙️ Best Settings

| Use Case             | Temperature | Top-p | Top-k | Max Tokens |
| -------------------- | :---------: | :---: | :---: | :--------: |
| **Chatbot**          |     0.7     |  0.9  |   40  |   300–500  |
| **Coding**           |     0.2     |  0.9  | 20–40 |   300–800  |
| **Story Writing**    |     1.0     |  0.95 |   50  |  500–1000  |
| **Customer Support** |     0.3     |  0.9  | 20–40 |   200–400  |

> **Note:** These are recommended starting values. The ideal settings depend on the model and the specific application.

---