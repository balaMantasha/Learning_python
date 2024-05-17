#Family   #class
#Peerzada_Sadaf_Ajaz_Baba     #object
#Abu_jan                      #object
#Ami_jan                      #object
#Mammy                        #object
#Peerzad_Sadaf_Ajaz_Baba.changeName("Sadaf")
#incapsulation
#inheritence
#polymorphism
class Person:
    name = "Peerzada_Sadaf_Ajaz_Baba"
    occupation = 'xyz'
    gender = "Female"
    def info(self):
        print(f"{self.name} is a {self.occupation} ")
        #self means that object on which that methods is being called
    
a = Person()
a.name = 'Abu'
a.occupation = 'Business'
a.gender =  'Male'
print(a.name)
a.info()