# try :
#  a= int(input("enter your number"))

#  print(f"multiplication table of {a} is")

#  for i in range(1,11):
#     print(f"{a} X {i} = {a*i}")
# except :
#   print("error handled")

# print("some imp lines of code")

def my():
    a=20
    b=0

    try:
        c=a/b

        print(c)
        return 1

    except Exception as e:
        print(e)
        return 0


    finally: 
     print("this was test")

x= my()
print(x)


a=10

if (a<5 or a>9):
   raise ValueError("invalid number")
