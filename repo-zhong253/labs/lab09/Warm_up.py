# CSCI1133,Lab Section 004,lab09 Shanshan Zhong Warm-up
"""
Created on Thu Mar 28 01:12:24 2019

@author: shanshanzhong
"""
names= ['joe', 'tom', 'barb', 'sue','sally']
scores = [11,22,14,17,10]

#1)
def makeDictionary(names,scores):
    dictionary = {}
    for i in range(len(names)): # range()
        dictionary[names[i]] = scores[i]
    return dictionary

scoreDict = makeDictionary(names,scores)

#2)
scoreDict['barb']

#3)
scoreDict['john'] = 18

#4)
sorted_scores = sorted(scoreDict.values()) # Values only: dict.values()

#5)
ave = sum(sorted_scores)/len(sorted_scores)

#6)
del(scoreDict['tom'])

#7)
scoreDict['sally'] = 15

#8)
def getScore(name,dictionary):
    if name in dictionary:
        return dictionary[name]
    else:
        print('Error.')
        return -1
name = input('Enter a name: ')
getScore(name,scoreDict)