# CSCI1133,Lab Section 004,lab06 Shanshan Zhong Stretch
"""
Created on Wed Feb 27 23:05:14 2019
@author: shanshanzhong
"""
import math
def shortestDist(my_list):
    dist_all = []
    #list comprehension used; i,j are two lists from my_list
    for i,j in [(i,j)for i in my_list for j in my_list]: 
    
        #make sure comparing a point with itself is avoided
        if i != j:
            x = (j[0]-i[0])**2
            y = (j[1]-i[1])**2
            dist = math.sqrt(x+y)
            dist_all.append(dist)
    #get the min distance
    dist_min = min(dist_all)
    return dist_min




my_list = [[45, -99], [24, 83], [-48, -68], [-97, 99], \
           [-8, -77], [-2, 50], [44, 41], [-48, -58], \
           [-1, 53], [14, 86], [31, 94], [12, -91], \
           [33, 50], [82, 72], [83, -90], [10, 78], \
           [7, -22], [90, -88], [-21, 5], [6, 23]]
shortestDist(my_list)
