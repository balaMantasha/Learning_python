#class Person:
   #name = "Peerzada_Sadaf_Ajaz_Baba"
    #Age = 24

#a= Person()
#a.name= 'Abu'
#a.Age= 63
class Family:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
    def info(self):
     print(f"{self.name} is a {self.occupation}")

a = Family("Sadaf", "Student")
b = Family("Abu","Business man")
a.info()
b.info()
#Two types of constructors: Parameterized,Default
