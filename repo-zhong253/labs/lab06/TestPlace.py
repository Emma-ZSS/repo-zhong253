# CSCI1133,Lab Section 004,lab06 Shanshan Zhong Test place
"""
Created on Thu Feb 28 13:01:22 2019
@author: shanshanzhong
"""
my_list = ['London', 'Edinburgh', 'Heidelberg', 'Paris', 'Brussels']
print('Original: ',my_list)

print('Sorted: ',sorted(my_list))
print('After Sorted: ',my_list)
#sorted() doesn't change the original list

print('Sorted reverse: ',sorted(my_list, reverse = True))
print('After sorted reverse: ',my_list)
#sorted(reverse=True) doesn't change the original list

my_list.reverse()
print('Reverse: ',my_list)
#list.reverse() change the original function

my_list.insert(0,'Berlin') #'0' at the begining of the list (BEFORE which you want to insert)
print('Insert: ',my_list)

my_list.append('Zurich')
print('list.append: ',my_list)

my_list.pop(1)
print('list.pop: ',my_list)
my_list.pop(1)
print('list.pop: ',my_list)
my_list.pop(3)
print('list.pop: ',my_list)

sec_p = my_list[1]
print('Second place: ',sec_p)

my_list.remove('Heidelberg')
print('Removed: ',my_list)

my_list[0] = 'TestPlace'
print('First place changed: ',my_list)

del my_list[1]
del my_list[1]
print('del: ',my_list)

print('Final output: ',my_list)
