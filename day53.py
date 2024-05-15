#map
def cube(x):
    return x*x*x
print(cube(2))
l = [1,2,3,4,5,6]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)
newl1 = list(map(cube,l))
print(newl1)
#filter
def filtered_function(a):
    return a>4
newl2 = list(filter(filtered_function,l))
print(newl2)
#reduce
from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y,numbers)
print(sum)
