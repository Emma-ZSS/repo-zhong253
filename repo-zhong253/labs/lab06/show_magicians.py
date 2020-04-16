# CSCI1133,Lab Section 004,lab06 Shanshan Zhong show magicians
"""
Created on Thu Feb 28 13:04:18 2019
@author: shanshanzhong
"""
list_name = ['David Blaine','Derren Brown','Jerry Sadowitz','Dynamo','Apollo Robbins']
def show_magicians(list_name):
    print(list_name)
    
def make_great(list_name):
    i = 0
    for i in range(len(list_name)):
        list_name[i] = 'Great '+list_name[i]
        i+=1
    return list_name

show_magicians(list_name)
make_great(list_name)
show_magicians(list_name)
