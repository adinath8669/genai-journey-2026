from transformers import pipeline

# generator = pipeline(
#     "text-generation",
#     model="distilgpt2"
# )

# result = generator(
#     "Artificial Intelligence is",
#     max_new_tokens=50
# )

# print(result[0]["generated_text"])

Classifier=pipeline("sentiment-analysis")

result2=Classifier("I am excited to become a Generative AI Engineer.")

print(result2)