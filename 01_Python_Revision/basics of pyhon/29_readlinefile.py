f = open('28_file.txt' , 'r') # reading a file

while True:

   line = f.readline()
   if not line:
     break
   print(line)