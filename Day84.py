import time

#def usingWhile():
 #i = 0
 #while i<50000:
    #i = i+1
    #print(i)
    
#def usingFor():
    #for i in range(50000):
        #print(i)

#init = time.time()
#usingFor()
#t1 = time.time() - init
#print(t1)
#usingWhile()

#print(time.time() - init)
#print(t1)
print(4)
time.sleep(10)
print("This is printed after 3 seconds")
s = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", s)
print(formatted_time)
