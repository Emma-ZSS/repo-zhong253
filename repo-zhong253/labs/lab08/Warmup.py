# CSCI1133,Lab Section 004,lab08 Shanshan Zhong Warmup
"""
Created on Wed Mar 13 21:33:49 2019

@author: shanshanzhong
"""
#1.
#============================================
# a. Base Case:
#   if len(n)==0:
#       return
# b. General Case:
#   else:
#       print(n[-1]) 
#       return reverseString n[:-1]
#============================================   
def reverseString(n):
    if len(n)==0:
        return
    else:
        print(n[-1],end="") # end="" on the same line!
        return reverseString(n[:-1])
    
reverseString("olleh")


#2.
#============================================
# a. Base Case:
#   if len(mylist)==1:
#       return mylist[0]
# b. General Case:
#keep dropping position 0 if small
#   elif mylist[0]<=mylist[1]:
#       mylist.pop(0)
#       return maxValue(mylist)
#
#keep dropping position 1 if small
#   elif mylist[1]<=mylist[0]:
#       mylist.pop(1)
#       return maxValue(mylist)
#
#Do both way to make true only MAX value left
#============================================ 
def maxValue(mylist):
    print(mylist)
    if len(mylist)==1:
        return mylist[0]
    elif mylist[0]<=mylist[1]:
        mylist.pop(0)
        return maxValue(mylist)
    elif mylist[1]<=mylist[0]:
        mylist.pop(1)
        return maxValue(mylist)

mylist = [3,4,9,7,3,0]
mylist = [0,0,0,0]
maxValue(mylist)

