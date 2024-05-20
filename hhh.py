
with open('myfile.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(4)
with open('myfile.txt','r') as f:
    print(f.read())