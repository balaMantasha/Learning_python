#class Myclass:
    #def __init__(self, value):
        #self._value = value
    #def show(self):
        #print(f"Value is {self._value} ")
    #@property
    #def value(self):
        #return self._value
#obj = Myclass(10)
#print(obj._value)
#obj.show()
class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname= lname
        #self.email=f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    @email.deleter
    def email(self):
     self.fname=None
     self.lname=None
arpit = Employee ("Arpit","Patidar")
manoj = Employee("Manoj","Yadav")
#print(arpit.explain())
#print(arpit.email)
#arpit.fname = "Arpu"
#print(arpit.email)

arpit.email="this.that@gmail.com"
print(arpit.email)
del arpit.email
print(arpit.email)