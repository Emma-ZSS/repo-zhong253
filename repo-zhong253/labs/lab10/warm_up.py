# CSCI1133,Lab Section 004,lab 10 Shanshan Zhong Warm- up
"""
Created on Thu Apr  4 12:23:32 2019

@author: shanshanzhong
"""
# Intro  
class rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0: 
            self.denominator = 1
        else:
            self.denominator = den
            
    # Call to print
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
            
num1 = rational(3,4)
num2 = rational(1,3)
print(num1)
num3= rational()
print(num3)

# Warm_up
class rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0: 
            self.denominator = 1
        else:
            self.denominator = den
            
    def scale(self,scale):
        self.denominator = self.denominator * scale
        self.numerator = self.numerator * scale
    
    def __str__(self):
        if self.numerator == 0:
            return str(0) # for print return need to be str type
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + '/' + str(self.denominator)

        
        
        
num4 = rational(5,1)       
print(num4)
num5 = rational(0,1)       
print(num5)
num6 = rational()
print(num6)

num1 = rational(3,4) # Always run this first
num1.scale(3)
print(num1)




















