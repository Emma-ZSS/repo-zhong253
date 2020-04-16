# CSCI1133,Lab Section 004,lab08 Shanshan Zhong Challenge
"""
Created on Thu Mar 14 12:18:43 2019

@author: shanshanzhong
"""
#1.
#============================================
# Base Case:
#   n//10 == 0
#   return n
# General Case:  
#   n//10 != 0
#   n%10: unit to add
#   n//10: what's left
#   (n//10)+(n%10) adding on unit (only the unit that matters)
#   return superDigit(n//10)+(n%10)
#============================================   

def superDigit(n):
    if n//10 ==0:
        return n
    else:
        new_n = (n//10)+(n%10) # Adding modulo to the unit
        return superDigit(new_n)
    
superDigit(1439)

#2.
#============================================
# Base Case:
#   b == 0
#   return a
# General Case:  
#   q = a//b
#   r = a%b
#   return gcd(b,r)
#============================================   

def gcd(a,b):
    if 0<a<b:
        return gcd(b,a)
    elif a<0 or b<0:
        return gcd(abs(a),abs(b))
    else:
        if b == 0:
            return a
        else:
            r = a%b
            return gcd(b,r)
gcd(198,1260)
gcd(-198,1260)
gcd(1260,198)