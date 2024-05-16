class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"The name of Employee {self.id} is {self.name}")
class Programmer(Employee):
    def showlanguage(self):
        print('The Default language is python')


e1 = Employee("Rohan Das",6)
e1.showdetails()
e2 = Employee("Mohan Das",7)
e2 = Programmer("Mohan Das",7)

e2.showdetails()
e2.showlanguage()
#Types of inheritance
#Single inhertance
#Multiple inheritance
#Multilelel inheritance
#Hierarchieal inheritance
#hybrid Inheritance

