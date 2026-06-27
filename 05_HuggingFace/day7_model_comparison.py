
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

result = generator(
    "Explain Machine Learning in simple words.",
    max_new_tokens=50,
    pad_token_id=generator.tokenizer.eos_token_id
)

# print(result[0]["generated_text"])


from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

client=genai.Client(api_key=api_key)

result2=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Machine Learning in simple words.",
    config={
                "max_output_tokens": 220,
                "temperature": 0.7
                 }
)

# print(result2.text)

hf_answer = result[0]["generated_text"]

gemini_answer = result2.text

print("="*50)
print("Hugging Face")
print(hf_answer)

print("="*50)
print("Gemini")
print(gemini_answer)