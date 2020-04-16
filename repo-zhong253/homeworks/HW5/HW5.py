# CSCI1133,Lab Section 004,HW 5 Shanshan Zhong
"""
Created on Sat Mar 30 14:28:02 2019

@author: shanshanzhong
"""
#1.
#============================================
# Name: cnt_occur
# Purpose: 
#       Given a list and a value and returns the number of times the element is in the list.
# Precondition:  
#       1)The value being counted cannot be a complex object such as a list or tuple. 
#           Assume numbers and strings are in the list and can be embedded in addition lists.
#       2)Only integers and strings will be in the lists.
#       3)Only an integer or a string can be counted for occurrences.
# Input Parameter(s)
#       mylist: a list contains integers and strings (can be embedded)
#       val: a value, can be string or integer
# Return Value(s)
#       --if mylist is empty: returns 0
#       --elif mylist[0] equals val: count 1 & reduce size of mylist
#       --elif mylist[0] is a list: call func for [0] & call func for [1:]
#       --else mylist[0] not equals val: reduce size of mylist call func
#============================================   
def cnt_occur(mylist, val): 
    if mylist == []:
        return 0 # Do the count using accumulation
    elif mylist[0] == val:
        return 1 + cnt_occur(mylist[1:],val)
    elif type(mylist[0]) is list:
        return cnt_occur(mylist[0],val)+ cnt_occur(mylist[1:],val)
    else: # mylist[0] not list != val
        return cnt_occur(mylist[1:],val)

"""   
cnt_occur ([1,2,3,1,1,5,6,1,1,2,2], 2)
cnt_occur([1,2,3,1,1, [1,1,2,3,[1]]], 1)
cnt_occur(["aa", 1, "bb", "bb", 2, 1, ["hello", "bb"]], "bb")
cnt_occur([], 3)
"""

#2.
#============================================
# Name: position
# Purpose: 
#       Given a list and an element and returns a list of numbers corresponding to the position 
#       of every occurrence of the element in the list.
# Precondition:  
#       1) Assume the first element of the list is element 0. 
#       2) If the element is not in the list, return the empty list, [].
# Input Parameter(s)
#       mylist: a list contains integers and strings
#       element: a value, can be string or integer
#       --helper--
#       count: default 0
# Return Value(s)
#       HELPER FUNCTION:
#       --if mylist is empty: returns [] (for list addition)
#       --elif mylist[0] equals element: 
#           i) [count] for list addition
#          ii) count 1 & reduce size of mylist & keep tracking
#       --else mylist[0] not equals element: count 1 & reduce size of mylist & keep tracking
#        POSITION FUNCTION:
#        --call helper function with count==0
#============================================ 
def helper(mylist,element,count):
    if mylist == []:
        return []
    elif mylist[0] == element:
        return [count] + helper(mylist[1:],element,count+1) # List addition; DONT forget count+1!!!
        # !count is not assigned variable, it's the imput at the time function called
    else:
        return helper(mylist[1:],element,count+1) # Reduce list and count +1

def position(mylist, element):
       return helper(mylist, element, 0) # Start count from 0

"""
position([1,2,3,4,1,1], 1)
position([3,3,3,3,6,'6',6],'6')
position([1,2,3], 4)
"""

#3.
#============================================
# Name: rm_conseq_dups
# Purpose: 
#       Given a list of elements and returns a new list with the consecutive 
#       duplicates of any element removed
# Precondition:  
#       1) There will be no embedded lists.
#       2) Only integers or strings will be in the list.
# Input Parameter(s)
#       mylist: a list contains integers and strings
#       --remove_d--
#       newlist: defualt []
# Return Value(s)
#       REMOVE_D FUNCTION(list, newlist):
#       --if mylist is empty: returns [] (for list addition)
#       --elif ls[0] not in newlist: (remove duplicates)
#           i) [ls[0]] for list addition
#          ii) add ls[0] to newlist & reduce size of ls & keep tracking
#       --else ls[0] in newlist: reduce size of mylist & keep tracking
#        POSITION FUNCTION:
#        --call remove_d with newlist == []
#============================================ 
def remove_d(ls,newlist):
    if ls ==[]:
        return []
    elif ls[0] not in newlist: # keep only one copy in newlist
        return [ls[0]] + remove_d(ls[1:],[ls[0]])
    else:
        return remove_d(ls[1:],newlist)

def rm_conseq_dups(mylist):
    return remove_d(mylist,[])

"""
rm_conseq_dups([])
rm_conseq_dups([1, 1, 1, 2, 3, 3, 3, 4, 4, 1, 1, 10])
rm_conseq_dups([1,2,3,4,1,2,3,4])
"""

#4.
#============================================
# Name: sequence
# Purpose: 
#       Given the one input parameter that represents the nth value to calculate
# Precondition:  
#       1) The input parameter will always be an integer.
#       2) Sequence must start at 3.
# Input Parameter(s)
#       par: a integer
#       --cal--
#       times: control 2's power
#       x: multiplier
# Return Value(s)
#       CAL FUNCTION(par,times,x):
#       --times equals par: 3 * x
#       --else: 
#           multiplers equals to 2 to the power of times
#           accumulate times to par & keep tracking
#        POSITION FUNCTION:
#        --return cal function with times==1 and x==1
#============================================ 
def cal(par,times,x): #x default 1
    if times == par:
        return 3 * x
    else:
        x = 2**times
        return cal(par,times+1,x) #times default 1
def sequence(par):
    return cal(par,1,1)

"""
sequence(1)
sequence(5)
sequence(3)
sequence(10)
"""

#5.
#============================================
# Name: rangeIt
# Purpose: 
#       Given a range and creates a list containing all integers within the range
# Precondition:  
#       1) The first number will always be less than or = to the second number.
#       2)The inputs will always be integer values.
# Input Parameter(s)
#       num1: smaller value
#       num2: bigger value
#       times: control 2's power
#       x: multiplier
# Return Value(s)
#       CAL FUNCTION(par,times,x):
#       --times equals par: 3 * x
#       --else: 
#           multiplers equals to 2 to the power of times
#           accumulate times to par & keep tracking
#        POSITION FUNCTION:
#        --return cal function with times==1 and x==0
#============================================ 
def rangeIt(num1,num2):
    if num1 == num2:
        return [num2]
    else:
        return [num1]+rangeIt(num1+1,num2)

"""
rangeIt(3,6)
rangeIt(3,3)
"""




