from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "I want to become a Generative AI Engineer."

tokens = tokenizer.tokenize(text)

print(tokens)


encode=tokenizer(text)
print(encode)


decode=tokenizer.decode(encode["input_ids"])
print(decode)