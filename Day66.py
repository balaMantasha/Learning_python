class Family:
    Familyname = "Baba Family" #class variable
    No_of_Family_Members = 0
    def __init__(self,name):
        self.name = name #Instance variable
        self.age = 24
        Family.No_of_Family_Members +=1
    def showDetails(self):
        print(f"The name of the Family member is {self.name} and the age is {self.age} in {self.Familyname} of size{self.No_of_Family_Members}")
fm1 = Family("Sadaf")
fm1.showDetails()
fm2 =Family("Abu")
Family.showDetails(fm1)
fm2.showDetails()
fm2.age = 52
fm2.showDetails()
fm2.Familyname = "Peerzada Family"
fm2.showDetails()
fm1.showDetails()
print(fm2.Familyname)
print(Family.Familyname)
print(Family.No_of_Family_Members)





