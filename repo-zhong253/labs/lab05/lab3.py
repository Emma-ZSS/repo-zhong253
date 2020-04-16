# CSCI1133,Lab Section 004,lab05 Shanshan Zhong,lab3
"""
Created on Wed Feb 20 23:04:15 2019

@author: shanshanzhong
"""

def minimumIndex(ls,ind):
    min_v = ls[ind]
    new_list = ls[ind:]
    for i in new_list:
        if i < min_v:
            min_v = i
            indx = new_list.index(i)
        else:
            min_v = min_v
            indx = new_list.index(min_v)
    print(indx+ind)
