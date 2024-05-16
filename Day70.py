class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e = Employee("Harry",12000)
print(e.name)
print(e.salary)
string = "Sadaf-120000"
e = Employee.fromstr(string)
print(e.name)
print(e.salary)