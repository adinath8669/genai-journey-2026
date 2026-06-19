#list in python

#list 



arr = tuple(map(int, input().split()))
x = int(input())

########### Write your code below ###############
# Print the index of x in arr
if x in arr:
    print(arr.index(x));
    
else:
    print("index not present")




    # Taking input and initializing dictionary
keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

# Insert k,v in my_dict
# Print Inserted if inserted successfuly
my_dict=dict(k,v)
k,v=input.split()
v=int(v)
my_dict[k]=v
print('inserted')


d = input()
if d in my_dict:
  my_dict.pop(d)
  print('deleted')
  
else:
    print(-1)

p = input()

if p in my_dict:
    print(my_dict[p])
else:
    print(-1)
    
# Print marks of given key p if key present, else print -1
