# CSCI1133,Lab Section 004,lab11 Shanshan Zhong Vector Class
"""
Created on Thu Apr 11 12:21:26 2019

@author: shanshanzhong
"""
class vector:
    def __init__(self,vect = [0,0,0]):
        self.vector = vect
        
    def __str__(self):
        return str(self.vector)
    
    def getValues(self):
        return self.vector
    
    def setValues(self,newlist = []):
        self.vector = newlist
        
    def magnitude(self):
        self.mag = sum(i**2 for i in self.vector)
        return self.mag
    
    def __add__(self,other):
        return vector([self.vector[i]+other.vector[i] for i in range(len(self.vector))])
         
    
    def __mul__(self,val):
        return vector([i*val for i in self.vector])
    
    
# Test
vect1 = vector()
print(vect1)
vect2 = vector([1,2,3])
print(vect2)

vect1.getValues()
vect2.getValues()

vect1.setValues([2,3,4])
vect1.getValues()

vect1.magnitude()
vect2.magnitude()

vect3 = vector.__add__(vect1,vect2)
print(vect3)

vect4 = vector.__mul__(vect1,2)
print(vect4)

type(vect1)
