from google import genai
from dotenv import load_dotenv
load_dotenv()
import os
api_key=os.getenv("Gemini_api_key")
client=genai.Client(api_key=api_key)


mode=input("enter mode b/w 1,2,3 : ")
if mode == "1":
    response=client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Explain how AI works",
    config={
                "max_output_tokens": 1024,
                "system_instruction" : "You are an expert Python coding assistant.",
                "temperature": 0.2
                 }
    )


elif mode == "2":
    response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works",
    config={
                "max_output_tokens": 1024,
                "system_instruction" :"You are a creative story writer.",
                "temperature": 1.2
                 }
    )

elif mode == "3":
 response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works",
    config={
                "max_output_tokens": 1024,
                "system_instruction" : "You are a patient AI teacher.",
                "temperature": 0.5
                 }

)

print(response.text)