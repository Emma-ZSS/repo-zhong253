# CSCI1133,Lab Section 004,lab09 Shanshan Zhong challenge_1
"""
Created on Thu Mar 28 13:15:40 2019

@author: shanshanzhong
"""
#1)
def addDB(dic,str1,str2):
    if str1 in dic:
        dic[str1].append(str2)
    else:
        dic[str1] = [str2]
    if str2 in dic:
        dic[str2].append(str1)
    else:
        dic[str2] = [str1]
    return dic
    


######## To be used later ############
#dic = {}
#enter = input('Enter your command: ')
#while enter != 'n':
#    command = enter.split()
#    str1 = command[1]
#    str2 = command[2]
#    addDB(dic, str1, str2)
#    enter = input('Enter your command: ')
######################################
    
#2)
def findDB(dic,key):
    if key in dic:
        return dic[key]
    else:
        return []

#findDB('bob')
#findDB('emma')
#del dic['bob']
#del dic['755.3632']
#findDB('755.3632')


#3）
def removeDB(dic,str1,str2):
    if (str1 in dic) and (str2 in dic):
        dic[str1].remove(str2)
        dic[str2].remove(str1)
    elif (str1 in dic) and (str2 not in dic):
        del(dic[str2])
    elif (str2 in dic) and (str1 not in dic):
        del(dic[str1])
    
#removeDB(dic,'bob','755.3632')
    
#4)
def main():
    dic = {}
    enter = input()
    while enter != 'end':
        command = enter.split()
        opr = command[0]
        str1 = command[1]
        if opr == 'add':
            str2 = command[2]
            addDB(dic, str1, str2)
        elif opr == 'find':
            print(findDB(dic,str1)) # print function's return
        elif opr == 'del':
            str2 = command[2]
            removeDB(dic, str1, str2)
        else:
            print('Not Valid')
        enter = input()

main()
