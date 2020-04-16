# CSCI1133,Lab Section 004,lab 10 Shanshan Zhong Challenge
"""
Created on Sat Apr  6 22:47:30 2019

@author: shanshanzhong
"""
import re
class Poly:
    def __init__(self,coe): #default coefficient a list [0]
        self.coe = coe
        self.ls = re.split('[+-]',coe)#re character class [+-]
        self.ls.reverse()
        
        # Add x to all terms
        for i in range(len(self.ls)):
            if ('x' not in self.ls[i]) and ('^'not in self.ls[i]): # term is constant
                self.ls[i] = self.ls[i]+'x^0'
            elif ('x' in self.ls[i]) and ('^'not in self.ls[i]): # term is x^1
                self.ls[i] = self.ls[i]+'^1'
            else: # term is x^d
                pass
        
        # Degree of poly
        self.deg = int(self.ls[-1][self.ls[-1].index('^')+1:])
        
        self.de = [i for i in range(self.deg+1)] # create full list of degree
        
        # A dictionary of existing terms deg:coef
        self.helper = {}
        for term in self.ls:
            self.d = term[term.index('^')+1:] # degree
            self.c = term[:term.index('x')]  # coefficient
            if self.c == '':
                self.helper[int(self.d)] = 1
            else:
                self.helper[int(self.d)] = float(self.c)
        
        # A dictionary of full terms deg:coef
        self.diction = {}  
        for num in self.de: # can be used as index
            if num in self.helper:
                self.diction[num]=self.helper[num]
            else:
                self.diction[num]=0     
        
        # Coefficient list
        self.coefficient = list(self.diction.values())

    def degree(self):
        return self.deg
    
    def insertTerm(self,exp,coef):
        if exp < len(self.coefficient): #add into the list
            self.coefficient[exp] = coef
        elif exp > len(self.coefficient): #add to the back
            while exp != len(self.coefficient):
                self.coefficient.append(0)
            self.coefficient.append(coef)

    def __str__(self):
        self.ind = ['1' if i==0 else 'x' if i==1 else 'x^'+str(i) for i in range(len(self.coefficient))] #if/elif/else in list comprehension
        self.dic = {self.ind[i]:self.coefficient[i] for i in range(len(self.coefficient))}
        
        # deal with x^0 term
        if self.dic['1']==0:
            self.print = []
        elif self.dic['1'] < 0:
            self.print = [str(self.dic['1'])]
        else:
            self.print = ['+'+str(self.dic['1'])]
        
        # deal with the rest of terms
        for i in self.ind[1:]:
            if self.dic[i] == 0:
                pass # append nothing if coef is 0
            elif self.dic[i] < -1:
                self.print.append(str(self.dic[i])+i)
            elif self.dic[i] == -1:
                self.print.append('-'+i)
            elif self.dic[i] == 1:
                self.print.append('+'+i)
            else:
                self.print.append('+'+str(self.dic[i])+i)
        self.print.reverse() #largest power first
        self.string = ''.join(self.print) #convert to a str
        return self.string[1:]
    
    def calculate(self,val):
        self.ind = ['1' if i==0 else 'x' if i==1 else 'x^'+str(i) for i in range(len(self.coefficient))] #if/elif/else in list comprehension
        self.dic = {self.ind[i]:self.coefficient[i] for i in range(len(self.coefficient))} # NOTE: values are with sign
        
        self.keys = [i for i in self.dic] # keys
        self.cal = {self.dic[self.keys[i]]:(val**i)*self.dic[self.keys[i]] for i in range(len(self.keys))}# use index of keys as degree
        self.output = list(self.cal.values()) # values after calculated
        return sum(self.output)

    def integrate(self):
        self.ind = ['x' if i==0 else 'x^'+str(i+1) for i in range(0,len(self.coefficient))] # increase power of x
        self.de = [i for i in range(1,len(self.coefficient)+1)] # create list of denominator
        self.dic = {self.ind[i]:self.coefficient[i] for i in range(len(self.coefficient))} # dict ind:coef
        self.dic1 = {self.ind[i]:self.de[i] for i in range(len(self.coefficient))} # dict ind:denominator
        
        
        # Same as string
        if self.dic['x']==0:
            self.print = []
        elif self.dic['x'] < 0:
            self.print = [str(self.dic['x'])+'x']
        else:
            self.print = ['+'+str(self.dic['x'])+'x']

        for i in self.ind[1:]:
            if self.dic[i] == 0:
                pass
            elif self.dic[i] < -1:
                self.print.append(str(self.dic[i])+i+'/'+str(self.dic1[i]))
            elif self.dic[i] == -1:
                self.print.append('-'+ i +'/'+str(self.dic1[i]))
            elif self.dic[i] == 1:
                self.print.append('+'+ i +'/'+str(self.dic1[i]))
            else:
                self.print.append('+'+str(self.dic[i])+i+'/'+str(self.dic1[i]))
        self.print.reverse() #largest power first
        self.string = ''.join(self.print) #convert to a str
        return self.string[1:]
    
'''    
import re   
coe = 'x^2+3x-1'
ls = re.split('[+-]',coe)#re character class [+-]
diction = {}
for term in ls:
    if ('x' not in term) and ('^'not in term): # term is constant
        diction[0] = term
    elif ('x' in term) and ('^'not in term): # term is x^0
        c = term[:term.index('x')]  # coefficient
        diction[1] = c
    else: # term is x^d
        d = term[term.index('^')+1:] # degree
        c = term[:term.index('x')]  # coefficient
        diction[int(d)] = c
diction = {keys:diction[keys] for keys in sorted(diction.keys())} # reassign
coefficient = [int(i) if i!='' else 1 for i in list(diction.values())]
        
a = '2x^20'
if ('x' in term) and ('^'in term): # term is x^d
    coefficient[d] = c
elif ('x' in term) and ('^'not in term): # term is x^0
    coefficient[d] = 1
else: # term is constant
    coefficient[0] = term
d = a[a.index('^')+1:] # degree
c = a[:a.index('x')]  # coefficient
'''       
        
poly = Poly('x^2+2x+1') 

poly.degree()
print(poly)       
poly.calculate(2)       
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
