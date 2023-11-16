#Create a "Person" class
#Create an attribute "name" in the "Person" class
class Person:
    def __init__(self,name,lname,age:int):
        self.last_name = lname
        self.name = name
        self.age = age
x = Person("Allamurod","Xakimov",18)
# print(x.name,x.last_name,x.age,"yoshda")
