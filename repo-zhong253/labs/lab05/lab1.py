# CSCI1133,Lab Section 004,lab05 Shanshan Zhong,lab1
"""
Created on Wed Feb 20 20:53:34 2019

@author: shanshanzhong
"""
import random

die_sum = []
for m in range(0,10000):
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    die_sum.append(die_1 + die_2)
for i in range(2,13):
    print(format(i,"2d"),':',format(die_sum.count(i),"5d"))
# Yes. The histogram supports that 7 is the most likely outcome.
