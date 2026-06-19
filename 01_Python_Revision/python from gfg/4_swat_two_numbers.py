# swapping veriable with 3 different types

# swap two numbers without 3rd veriable
x=10;
y=20;
print('X :',x,'Y :',y)
#swapping veriables

x,y=y,x
print('X :',x,'Y :',y)

# swap two veriables eith 3rd veriable

temp=x;
x=y;
y=temp;

print('X :',x,'Y :',y)

# without 3rd veroable and python functionality

x=x+y;
y=x-y;
x=x-y;

print('X :',x,'Y :',y)