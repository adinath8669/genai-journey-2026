x=10   #gloable variable

def localVariable():
    # y=5 #local variable
    global y
    y=5

    print(y)
    print(x)
localVariable()

print(x)
print(y)