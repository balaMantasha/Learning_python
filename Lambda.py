def double(x):
    return x*2
print(double(5))
sss = lambda x: x*2
print(sss(5))
cube = lambda x:x*x*x
print(cube(5))
avg = lambda x,y,z:(x+y+z)/3
print (avg(7,7,7))
def apply(fx,value):
    return 6 + fx(value)
print(apply(cube,2))
print(apply(lambda x:x*x*x,2))