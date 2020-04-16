# CSCI1133,Lab Section 004,lab09 Shanshan Zhong Workout
"""
Created on Thu Mar 28 02:09:47 2019

@author: shanshanzhong
"""
def cntkey(context):
    print('Keyword frequency in alphabetic order: ')
    
    keywords = ['False','await','else','import','pass','None','break',
            'except','in','raise','True','class','finally','is','return','and',
            'continue','for','lambda','try','as','def','from','nonlocal','while',
            'assert','del','global','not','with','async','elif','if','or','yield']
    keywords.sort() # Alphabetical
    
    key_dict = {x:0 for x in keywords} # Make a dictionary
    
    # Count words & Assign
    for i in key_dict:
        key_dict[i] = context.count(i)
    for k,v in key_dict.items():
        if key_dict[k] != 0:        
            print('%s : %d' %(k,v))
    return
        
# Read files & operate
filename = input('Enter the filename: ')
with open(filename,'r') as file:
    lines = file.readlines()
    context = []
    for words in lines:
        context += words.split()
    # Call function
    cntkey(context)