# CSCI1133,Lab Section 004,Lab7 Shanshan Zhong Stretch
"""
Created on Thu Mar  7 01:10:16 2019

@author: shanshanzhong
"""
with open('/Users/shanshanzhong/CSCI1133_S19/repo-zhong253/labs/lab07/hack_ths.txt','r') as fileobj:
    newtext = ""
    albt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ls_txt = []
    ls_num = []
    dic = {}
    
    for line in fileobj:
        line = line.strip()
        if line.strip():
            newtext += line #change txt into a str
    newtext = newtext.lower() #unify characters
    
    for i in newtext:
        if i not in albt:
            newtext = newtext.replace(i,"") #replace function
        elif i in ['1','2','3','4','5','6','7','8','9','0']:
            newtext = newtext.replace(i,"") #replace numbers
            
    ls_txt.extend(newtext) #change str into list
    for i in albt:
        num = ls_txt.count(i)
        ls_num.append(num)
        dic[num]=i
    ls_num = sorted(ls_num,reverse=True)
    
    for num in ls_num:
        print(dic[num],num)
