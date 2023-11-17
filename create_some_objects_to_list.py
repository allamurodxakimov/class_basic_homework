from create_one_attribute import Person

#Create an object named "p1" whose name is "Anvar"
#Create an object named "p2" whose name is "Shavkat"
#Create an object named "p3" whose name is "Jasur"

#Add these objects to the "persons" named list
# class Person:
#     def __init__(self,name):
#         self.names = name
p1 = Person("Anvar")
p2 = Person("Shavkat")
p3 = Person("Jasur")
p = [p1.name,p2.name,p3.name]
print(p)