

print("1:add\n 2:sub \n 3:mul \n 4:div")

a=4
while (a!=5):
 x=int(input("enter your choice"))
 match x:
    case 1:
        print(4+5)
        
    
    case 2:
        print(4-5)
        
    case 3:
        print(4*5)
        
    case 4:
        print(4/5)
        
    case _:
        print("wrong input")