# CSCI1133,Lab Section 004,lab06 Shanshan Zhong my calculator
"""
Created on Thu Feb 28 13:04:18 2019
@author: shanshanzhong
"""
def my_calculator(list1, list2, op_name):
    output = []
    i = 0
    j = 0
    if op_name == '+':
        for i,j in [(i,j) for i in range(len(list1)) for j in range(len(list2))]:
            if i == j:
                output.append(list1[i]+list2[j])
            i += 1
            j += 1
    elif op_name == '-':
        for i,j in [(i,j) for i in range(len(list1)) for j in range(len(list2))]:
            if i == j:
                output.append(list1[i]-list2[j])
            i += 1
            j += 1
    elif op_name == '*':
        for i,j in [(i,j) for i in range(len(list1)) for j in range(len(list2))]:
            if i == j:
                output.append(list1[i]*list2[j])
            i += 1
            j += 1
    elif op_name == '/':
        for i,j in [(i,j) for i in range(len(list1)) for j in range(len(list2))]:
            if i == j:
                out = list1[i]/list2[j]
                if out > 0 :
                    out = int(out + 0.5)
                    output.append(out)
                else:
                    out = int(out - 0.5)
                    output.append(out)
            i += 1
            j += 1
    else: print('Wrong operation name input.')
    print(output)

list1 = [3,4]
list2 = [1,2]
my_calculator(list1,list2,'+')
my_calculator(list1,list2,'-')
my_calculator(list1,list2,'*')
my_calculator(list1,list2,'/')
