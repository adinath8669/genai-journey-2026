# f = open('28_file.txt' , 'r') # reading a file

# print(f.read())

# f.close()


f=open('28_file.txt' , 'w')

f.write('hello my name is ---')

f.close()


with open('28_file.txt','a') as f:
    f.write("adinath")
