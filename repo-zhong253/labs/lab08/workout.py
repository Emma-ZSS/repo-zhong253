# CSCI1133,Lab Section 004,lab08 Shanshan Zhong Workout
"""
Created on Wed Mar 13 22:58:26 2019

@author: shanshanzhong
"""
#============================================
# ***The empty lists are omitted
#
# a. Base Case:
#   (mylist[0] is int) 
#   square it
#   return mylist[1:]
# b. General Cases:
#   (mylist[0] is list) 
#   if not empty return list recall function
#   reduce list length
#============================================   

def flatDeepSquare(mylist):
        if len(mylist) == 0:
            return []
        else:
            if type(mylist[0]) is int:
                return [mylist[0]**2] + flatDeepSquare(mylist[1:]) #[1,2,3]; [2:]==[]
            elif type(mylist[0]) is list:
                return flatDeepSquare(mylist[0]) + flatDeepSquare(mylist[1:])
    
    

""" 
    
    if mylist != []: # Empty list omitted
        if len(mylist) == 1:
            if type(mylist[0]) is list:
                return flatDeepSquare(mylist[0])
            else:
                #new_list.append((mylist[0])**2)
                return mylist[0]**2
        else:
            if type(mylist[0]) is list:
                # mylist[0] + mylist[1:] removed [] around position 0
                # i.e. [2]+[3,4] = [2,3,4]
                return flatDeepSquare(mylist[0]+mylist[1:]) 
            else:
                #new_list.append((mylist[0])**2) # Add to new list
                return flatDeepSquare([mylist[0]**2]+mylist[1:]) # Reduce list length
"""

new_list = []   #where to create new list???  
flatDeepSquare([[-1,[2],[3],[[[-4,5]]],[],[]]])
