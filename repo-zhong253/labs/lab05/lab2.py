# CSCI1133,Lab Section 004,lab05 Shanshan Zhong,lab2
"""
Created on Wed Feb 20 21:44:13 2019

@author: shanshanzhong
"""
wrd = input('Insert word: ')
wrd_l = wrd.lower()
output = [] # Element in the list doesn't renew with loop
while wrd_l != '':
    wrd_list = [] # Start with an empty list each loop
    wrd_list.extend(wrd_l)
    if wrd_list.count(wrd_list[0]) >= 2: # Count number of the frist letter [0]
        output.append(wrd) # Save ORIGINAL input
    wrd = input('Insert word: ')
    wrd_l = wrd.lower()
for i in output:
    print(''.join(i)) # Print elements stored in the list one word per line
