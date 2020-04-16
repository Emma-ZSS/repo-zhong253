# CSCI1133,Lab Section 004,lab05 Shanshan Zhong,lab4
"""
Created on Thu Feb 21 12:18:42 2019

@author: shanshanzhong
"""
def expo(x,y):
    b = x
    x_0 = x
    for i in range(0,y):
        x_s = x_0
        for m in range(0,b-1):
            x_0 += x_s
    print(x_s)
