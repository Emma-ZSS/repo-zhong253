# CSCI1133,Lab Section 004,lab11 Shanshan Zhong Measure Class
"""
Created on Wed Apr 10 22:25:15 2019

@author: shanshanzhong
"""
class measure:
    def __init__(self,feet = 0,inches = 0):
        if inches < 12:
            self.feet = feet
            self.inches = inches
        else:
            self.feet = feet + inches//12
            self.inches = inches%12
        return
    
    def __str__(self):
        if self.feet == 0 and self.inches == 0:
            return '0'
        elif self.feet == 0:
            return ("%d\"" %(self.inches)) # \ to separate the ' ", so that the ' " can be printed
        elif self.inches == 0:
            return ("%d\'" %(self.feet))
        else:
            return ("%d\'%d\"" %(self.feet,self.inches))

    def __add__(self,other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches
        return measure(feet,inches)
    
    def __sub__(self,other):
        feet = self.feet - other.feet
        inches = self.inches - other.inches
        return measure(feet,inches)

m1 = measure()
m2 = measure(4,11)
m3 = measure(6,10)
print(m1)
print(m2+m3)
print(m3-m2)
