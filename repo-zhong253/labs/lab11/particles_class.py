# CSCI1133,Lab Section 004,lab11 Shanshan Zhong Particles Class
"""
Created on Thu Apr 11 13:08:43 2019

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
        if type(other) is vector:
            return vector([self.vector[i]+other.vector[i] for i in range(len(self.vector))])
        else:
            return vector([i + other for i in self.vector])
    
    def __mul__(self,val):
        return vector([i*val for i in self.vector])
    
class particle:
    def __init__(self,mass = 0.0,position = vector(),velocity = vector()):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        
    def __str__(self):
        return ('mass=%f, position=%s, velocity=%s' %(self.mass, str(self.position), str(self.velocity)))
    
    def setMass(self,m):
        self.mass = m
        
    def momentum(self):
        return self.velocity.__mul__(self.mass)
    
    def accelerate(self,a,t):
        self.velocity = self.velocity + a*t
        self.position = self.position + self.velocity*t + (1/2)*a*(t**2)
        return particle(self.mass,self.position,self.position)
    
part1 = particle(0.0,vector([1,2,3]),vector([3,4,5]))
print(part1)

part1.setMass(2.9)
print(part1)

part2 = part1.momentum()
print(part2)

part3 = part1.accelerate(2,10) # Remember to return & class() for overload functions
print(part3)

