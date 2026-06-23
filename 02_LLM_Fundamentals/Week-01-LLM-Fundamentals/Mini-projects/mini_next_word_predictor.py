
import random

next_token={
    'i like':[('AI', 0.4), ('Python', 0.3), ('Coffee', 0.2), ('Cricket', 0.1)],
    'i want':[('to learn AI',0.4),('to become an AI Engineer',0.2),('to build projects',0.9)]
}



while True:
    prompt=input("Enter the prompt / i like / i want / exit : ")

    if prompt=="exit":
        print("exiting")
        break

    if prompt in next_token:
        
        words, probs = zip(*next_token[prompt])
        prediction = random.choices(words, weights=probs)[0]

        print(prompt,prediction)
    else:
        print("Unknown prompt. Try 'i like' or 'i want'")