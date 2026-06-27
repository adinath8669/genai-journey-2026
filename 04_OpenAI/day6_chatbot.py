from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("GENAI_API_KEY")

client=genai.Client(api_key=api_key)

chat_history=[]


while True:
    my_input=input("you : ")
    chat_history= chat_history[-10:]

    if my_input.lower()=="exit":
        print("bye")
        break
    elif my_input.lower()=="hello":
        print("hello , how can i help you")
        continue

    elif my_input.lower()=="what is ai":
        print("Ai is artificial intellegence, which can act like human brain!")
        continue
    else:
        chat_history.append({
            'role':'user',
            'parts':[{"text":my_input}]
            })
        response=client.models.generate_content(
            model='gemini-2.5-flash',
            contents=chat_history,
            config={
                "max_output_tokens": 220,
                "temperature": 0.7
                 }
        )

        model_reply = response.text if response.text else "No response"
        print("model :", model_reply)

        chat_history.append({
            'role':'model',
            'parts': [{"text": model_reply}]
        })



    
