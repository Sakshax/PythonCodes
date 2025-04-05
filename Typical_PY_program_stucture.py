#This Program describes the typical structure of a Python program through commands in code 

# Python program structure  <----------------------- decoumentation section 

import math  #<----------------------- import section

radius = 5  #<----------------------- globle varible declaration section

class Circle():  #<----------------------- class  section
    def getArea(self):
        return math.pi * radius * radius
    def getCircumference(self):
        return 2 * math.pi * radius

def showradius(): #<----------------------- sub-program section
    print("The radius of the circle is:", radius) 

showradius() #<----------------------- playground section
c= Circle()
print("The area of the circle is:", c.getArea())  
print("The circumference of the circle is:", c.getCircumference())  


