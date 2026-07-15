from agent import crating_agent

agent=crating_agent()

# result=agent.invoke({"messages": [{"role": "user", "content": "2+10"}]})

# result2=agent.invoke({"messages": [{"role": "user", "content": "what is wheather in pune"}]})

# result3=agent.invoke({"messages":[{"role":"user","content":"what is string in python"}]})

# result4=agent.invoke({"messages":[{"role":"user","content":"give me interview questions on langchain"}]})


while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    result=agent.invoke({"messages":[{
        "role":"user",
        "content":user
    }]})
    print(result["messages"][-1].content)


# print(result2["messages"][-1].content)
# print(result3["messages"][-1].content)
# print(result4["messages"][-1].content)