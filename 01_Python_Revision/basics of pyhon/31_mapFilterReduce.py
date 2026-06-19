def cube(x):
   return x*x*x


l=[1,2,3,4,5,6,7]


new=list(map(cube,l))
print(new)


def filter1(f):
   return f<4

new=list(filter(filter1,l))
print(new)

