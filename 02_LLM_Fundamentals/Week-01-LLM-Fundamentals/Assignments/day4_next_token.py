# Program 1 – Simulate Next Token Prediction

import random

next_tokens = {
    "I love": ["AI", "Python", "coding", "pizza"],
    "AI is": ["powerful", "changing", "useful", "amazing"]
}

prompt = "I love"

prediction = random.choice(next_tokens[prompt])

print(prompt, prediction)

# Program 2 – Temperature Simulation

import random

words = [
    ("AI", 0.6),
    ("Python", 0.2),
    ("Machine Learning", 0.1),
    ("Pizza", 0.1)
]

print(random.choices(
    [w[0] for w in words],
    weights=[w[1] for w in words]
))