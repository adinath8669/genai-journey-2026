def fact(n):
    if(n==0 or n==1):
        print(1)
    
    else:
        x= n*fact(n-1)
        print( x)
    
fact(4)
