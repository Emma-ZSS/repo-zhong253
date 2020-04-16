# CSCI1133,Lab Section 004,lab06 Shanshan Zhong name_message
"""
Created on Thu Feb 28 13:04:18 2019
@author: shanshanzhong
"""
person_name = 'Stephanie'
person_message = '    \t Hello! I am Stephaine! \n     '
#'\t' Tab; '\n' New line

print(person_name)
print(person_message)

# NOTE: functions below do not change string in place
person_message.lstrip()
print(person_message.lstrip())
#str.lstrip([char]): Return a copy of the string with leading characters removed.
person_message.rstrip()
print(person_message.rstrip())
#str.rstrip([char]): Return a copy of the string with trailing characters removed. 
person_message.strip()
print(person_message.strip())
#str.strip([char]): Return a copy of the string with the leading and trailing characters removed.

person_message = person_message.lstrip('    \t ')
person_message = person_message.rstrip(' \n     ')
print(person_message)

name_message = person_name + ' says '+person_message
print(name_message)
