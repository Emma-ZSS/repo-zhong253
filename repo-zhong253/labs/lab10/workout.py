# CSCI1133,Lab Section 004,lab 10 Shanshan Zhong Workout
"""
Created on Thu Apr  4 13:18:04 2019

@author: shanshanzhong
"""
class Poly:
    def __init__(self,coefficient = [0]): #default coefficient a list [0]
        self.coefficient = coefficient
        
    def degree(self):
        self.d = len(self.coefficient)-1 #list start with poly 0
        return self.d
    
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
        

coe = [1,2,1]
poly = Poly(coe)
poly.degree()
poly.insertTerm(4,3)
poly.degree()
poly.insertTerm(1,5)
poly.degree()
print(poly)
poly.integrate()

'''
# __string__ & integrate TEST #
coef = [1,2,1]   
def string(coef):
    ind = ['1' if i==0 else 'x' if i==1 else 'x^'+str(i) for i in range(len(coef))] #if/elif/else in list comprehension
    print(ind)
    if len(coef) == 0:
        return []
    else:
        dic = {ind[i]:coef[i] for i in range(len(coef))}
        if dic['1']==0:
            pr = []
        elif dic['1'] < 0:
            pr = [str(dic['1'])]
        else:
            pr = ['+'+str(dic['1'])]
        
        print(dic)
        for i in ind[1:]:
            if dic[i] == 0:
                pass
            elif dic[i] < -1:
                pr.append(str(dic[i])+i)
            elif dic[i] == -1:
                pr.append('-'+i)
            elif dic[i] == 1:
                pr.append('+'+i)
            else:
                pr.append('+'+str(dic[i])+i)
    #return pr
    print(pr)
    pr.reverse() #largest power first
    string = ''.join(pr)
    return string[1:]

string(coef)

def integrate(coef):
    ind = ['x' if i==0 else 'x^'+str(i+1) for i in range(0,len(coef))] #if/elif/else in list comprehension
    de = [i for i in range(1,len(coef)+1)]
    print(ind)
    dic = {ind[i]:coef[i] for i in range(len(coef))}
    dic1 = {ind[i]:de[i] for i in range(len(coef))}
    if dic['x']==0:
        pr = []
    elif dic['x'] < 0:
        pr = [str(dic['x'])+'x']
    else:
        pr = ['+'+str(dic['x'])+'x']
    
    print(dic)
    for i in ind[1:]:
        if dic[i] == 0:
            pass
        elif dic[i] < -1:
            pr.append(str(dic[i])+i+'/'+str(dic1[i]))
        elif dic[i] == -1:
            pr.append('-'+ i +'/'+str(dic1[i]))
        elif dic[i] == 1:
            pr.append('+'+ i +'/'+str(dic1[i]))
        else:
            pr.append('+'+str(dic[i])+i+'/'+str(dic1[i]))
    return pr
coef = [1,0,2,3] 
integrate(coef)       
len(coe)
range(1,len(coe)) 
'''
