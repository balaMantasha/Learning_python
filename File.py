#f = open('myfile.txt', 'r')
#text  = f.read()
#print(text)
#f.close()
f = open('myfile.txt', 'a')
f.write('Hello, world')
f.close()
with open('myfile.txt', 'a') as f:
 f.write("hey, I am inside with")
 #dont have to close this
 f = open ('myfile.txt', 'r')
 while True:
  line = f.readline()
  print(line)
  if not line:
   print(line,type(line))
   break

