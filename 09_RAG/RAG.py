from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# gemini api key inilitization

api_key=os.getenv("GIMINI_API_KRY")

# model creation
client=genai.Client(api_key=api_key)

# read pdf and  store it in string
reader=PdfReader("09_RAG\introductio_to_ai.pdf")

text=""

for page in reader.pages:
    text += page.extract_text()

# convert it into chunks
chunks=[
    text[i:i+500]
    for i in range (0,len(text),500)]

# apply embadding(convert into relevent vectors)
model= SentenceTransformer("all-MiniLM-L6-v2")

embeddings=model.encode(chunks)
embeddings = np.array(embeddings).astype("float32")

dimension=embeddings.shape[1]

# store it in vector database
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


query=input("enter your question : ")

# converting query into embaddings(vectors)
query_embedding=model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

distances,indices =index.search(query_embedding,3)

# retriving relevnet chuncks from pdf
retrieved_chunks = "\n\n".join(
    [chunks[i] for i in indices[0]]
)

# print(retrieved_chunks)
# crating prompt
prompt = f"""
You are an AI assistant.

Use only the information provided below to answer the user's question.

Context:
{retrieved_chunks}

Question:
{query}

If the answer is not present in the context, reply:
"I couldn't find the answer in the provided document."
"""

# gemini model 
response=client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config={
        "temperature":0.1,
        "max_output_tokens":1000
    }
)

# final response
print(response.text)
