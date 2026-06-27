# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key=os.getenv("OPENAI_API_KEY")

# client=OpenAI(api_key=api_key)

# response = client.chat.completions.create(
#     model="gpt-4o-mini",   # works on free/low-cost tier
#     messages=[
#         {"role": "system", "content": "You are a helpful AI assistant."},
#         {"role": "user", "content": "Explain machine learning in simple words"}
#     ]

# )

import os
from dotenv import load_dotenv
from google import genai

# load env
load_dotenv()

# get API key
api_key = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Explain how to use the Gemini API in one sentence.',
)

print(response.text)