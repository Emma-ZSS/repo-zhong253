# CSCI1133,Lab Section 004,HW 4 Shanshan Zhong
"""
Created on Thu Feb 21 23:29:02 2019
Updared on Sun Mar 10 2019

@author: shanshanzhong
"""
# Problem 1
#============================================
# Name:  separate_int_and_str
# Purpose:  Given a list of integer and strings, create two new lists.  One
#       list will contain the integers and the other list will contain the 
#       strings.
# Precondition:  The list will only contain ints and strings 
# Input Parameter(s)
#       mylist:  a list containing integers and strings
# Return Value(s)
#       --if the input parameter is an emptylist , return a list 
#           with two empty lists:  [ [ ], [ ] ]
#       --else return a list with the 0th index position containing the 
#           list of integers, and the 1st index positioncontaining the
#           list of strings.  If there are no ints or strings, return 
#           an empty listin that position
#============================================
def separate_int_and_str(mylist):
    num = []
    st = []
    output = []
    for i in mylist:
        #test 'type'
        if type(i) is int:
            num.append(i)
        elif type(i) is str:
            st.append(i)
    output.append(num)
    output.append(st)
    return output



# Problem 2
#============================================
# Name:  average_of_lists
# Purpose:  Given a list of lists that contain numbers, create a list of int
#       that contains the average of each list
# Precondition:  The list of lists will only contain numbers
# Input Parameter(s)
#       mylist:  a list of lists containing numbers
# Return Value(s)
#       --if the input parameter has an empty list , return the empty list 
#           back in the same index of the original list in the new list.
#       --else return a list with the average stored as an int for each list 
#           in the same index of the original list
#============================================
def average_of_lists(mylist):
    ave_ls = []
    for i in mylist:
        if i == []:
            ave_ls.append([])
        else:
            #calculate averages
            s = sum(i)
            l = len(i)
            ave = s/l
            #normal rounding rules
            if ave > 0: 
                ave = int(ave + 0.5)
            else:
                ave = int(ave - 0.5)

            ave_ls.append(ave)
    return ave_ls
        
    

# Problem 3   
#============================================
# Name:  min_of_lists 
# Purpose:   Given a list of lists containing numerical values, return the
#       minimum value of the list of lists
# Precondition:   The list of lists will only contains numerical values
# Input Parameter(s)
#        mylist:  a list of lists containing numerical values
# Return Value(s)
#       --if the input parameter is an empty list, return 0.
#       --else return a the minimum value of the list of lists.
#============================================
def min_of_lists(mylist):
    if mylist == []: #case of empty set
        return 0
    else:
        new_list = [] #new list to store min values of each lists
        for ls in mylist:
            if ls == []: #case of empty set
                min_v = 0
                new_list.append(min_v)
            else:
                min_v = ls[0]
                for i in range(len(ls)): #find the min value of list
                    if min_v > ls[i]:
                        min_v = ls[i]
                    else: min_v = min_v
                    i += 1
                new_list.append(min_v)
                
        min_v = new_list[0]
        for i in range(len(new_list)): #find the min value of mylist
            if min_v > new_list[i]:
                min_v = new_list[i]
            else: min_v = min_v
            i += 1
    return min_v
        
     
    
# Problem 4   
#============================================
# Name:  greater_than
# Purpose:   Given a list and a value, return value True if everything in 
#       the list is greater than the value and False otherwise
# Precondition:  The list will only contain numerical values;
#       x is a numerical value
# Input Parameter(s)
#       mylist:  a list containing numerical values
#       x:  a numerical value
# Return Value(s)
#       --if everything in the list is greater than the value x, return True.
#       --else return False.
#============================================
def greater_than(mylist, x):
     min_v = 0
     if mylist == []:
         min_v = 0
     else: 
         min_v = mylist[0]
         for i in range(len(mylist)):
             if min_v > mylist[i]:
                 min_v = mylist[i]
             else: min_v = min_v
             i += 1
     
     #test if the min value of mylist is larger than x
     if min_v > x:
         return True
     elif min_v == 0:
         return True
     else: 
         return False
        


# Problem 5     
#============================================
# Name:  selection_sort
# Purpose:   Given a list, implement the selection-sort algorithm to sort 
#       a list of integers in ascending order
# Precondition:   The list will only contain numerical values
# Input Parameter(s)
#       mylist:  a list containing numerical values
# Return Value(s)
#       The function will not return anything. 
#       It will affect the list passed in.
#============================================    
def selection_sort(mylist):
    st = 0
    #loop for new range
    for st in range(len(mylist)):
        min_v = mylist[st]
        
        #loop to find min_value in a range
        for i in range(st,len(mylist)):
            if min_v > mylist[i]:
                min_v = mylist[i]
            else: min_v = min_v
            #control the loop
            i += 1 
    
        #replace min_V  
        if mylist[st] != min_v:
            ind_min = mylist.index(min_v)
            mylist[st],mylist[ind_min] = mylist[ind_min],mylist[st] #swap
        else:
            mylist[st] == min_v
        #control the range
        st += 1 
        

    
    
    
    
    
    
    
    
    
    
    
    
