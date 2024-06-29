class Student():
    age=15
john=Student()
print(john.age)

class Rectangle:
    def __init__(self, length, breadth, unit_cost=0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    def get_per(self):
        return self.breadth*self.length
area=Rectangle(4,9,6)
print(area.get_per())


#inheritence

class person():
    def __init__(self,name,id):
          self.name=name
          self.id=id
    def get_stmt(self):
        print(self.name,self.id)
    
class emp(person):
    def disp():
        print("hi")
employee=emp("sharon","19")
print(emp.disp())
          
#polymorphism
class car:
    def wheel(self):
        print("carrr")
class truck:
    def wheel(self):
        print("truckk")
c=car()
print(c.wheel())
t=truck()
print(t.wheel())

#array
import numpy as np
a = np.array([1,2])
b = np.array([2,1])