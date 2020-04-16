# CSCI1133,Lab Section 004,HW 6 Shanshan Zhong
"""
Created on Fri Apr  5 13:30:23 2019

@author: shanshanzhong
"""
import re # regular expression operations for Question 4.

#1.
#============================================
# Name: sameKeys
# Purpose:   Given two dictionaries, 
#       looks for keys that are found in both dictionaries 
#       and returns a new dictionary that contains key
# Precondition: 
#       1) Both dictionaries can be empty and an empty dictionary is returned.
#       2) There can be any type of objects for the values of the keys.  
#       3) A new dictionary is created.
# Input Parameter(s)
#       diction1: any type of objects for the values of the keys
#       diction2: any type of objects for the values of the keys
# Return Value(s)
#       --if the input parameter is an empty dictionary , return a empty dictionary
#       --else return a dictionary new key’s value being a list of the values 
#           of diction1.key and diction2.key values concatenated together
#============================================   
def sameKeys(diction1, diction2):
    newdic = {}
    for i,j in [(i,j) for i in diction1 for j in diction2]:
        if i == j:
            newdic[i]=[diction1[i]]+[diction2[j]]
        else:
            pass
    return newdic

'''
sameKeys({1: 'a', 2: 'b', 3: 'c', 4: 5}, {1: 333, 3: 'k', 4: ['o', 'p']})
sameKeys({}, {})
sameKeys({1: "hello"}, {1: "there"})
sameKeys({1: "hello"}, {2: 666, 3: 777})
'''

#2.
#============================================
# Name:  averageGrades
# Purpose:   Given a dictionary with keys representing students 
#       and values representing their grades.
#       Return a new dictionary with keys representing students 
#       and values representing an average oftheir grades. 
# Precondition: 
#       1) Both dictionaries can be empty and an empty dictionary is returned.
#       2) Each key’s valueindictionwill either be a list of integers or an empty list.
#       3) A new dictionary is created.
# Input Parameter(s)
#       diction: the values of the keys should be integers or empty set.
# Return Value(s)
#       --if the input parameter has an empty list , return a 0 for average
#       --else return a dictionary new key’s value being a integer.
#============================================  
def averageGrades(diction):
    avedic = {}
    for i in sorted(diction): #returns a new sorted list while leaving the source unaltered
        if diction[i]==[]:
            avedic[i]=0    
        else:
            avedic[i]=int(sum(diction[i])/len(diction[i]))
    return avedic

'''
averageGrades({"Shana": [100, 90, 80], "Jody": [100, 70, 80, 90, 100], "Mike": [100, 100,20]})
averageGrades({1234: [20,20,20], 3333: [40,50,40]})
averageGrades({})
averageGrades({"bobby": []})
'''

#3.
#============================================
# Name:  allKeys
# Purpose:   Given two input parameters: a dictionary and an integer 
#       return a list of non-duplicated elements representing the keys 
#       from the dictionary where the element was found
# Precondition:
#       1)Each key will have as its value a list that is empty or a list of integers.
#       2)The passed in argument, called element,will always be an integer. 
#       3)A list is created.
#       4)There will be no duplicate elements in the new list. 
# Input Parameter(s)
#       diction: with strings as its keys and lists of integers as each key’s value
#       element: an integer
# Return Value(s)
#       --if the element is not find in the diction, return []
#       --else return a list of non-duplicated elements representing the keys 
#       from the dictionary where the element was found
#============================================  
def allKeys(diction, element):
    output = []
    for i in diction:
        if element in diction[i]:
            output.append(str(i))
        else:
            pass
    output.sort()
    return output

"""
allKeys({1:[2], "bb": [], "cc": []}, 2)
allKeys({"aa":[1,2,3], "bb": [2,3,4], "cc": [2]}, 2)
allKeys({"bb":[1,2,2], "aa": [2,2,2], "cc": [3,3,4,5]}, 2)
allKeys({"aa":[1,2,2], "bb": [2,2,2], "cc": [3,3,4,5]}, 5)
"""

#4.
#============================================
# Name:  invertFiles
# Purpose:   
#       Give a list of filenames, open them, record each word appears in the file
#       with the file number alphabetically 
# Precondition:
#       1)Only words (no delimiters) should be in the resulting inverted file
#       2)All of the files this file is working with (input and output) are text files (.txt).
#       3)Textfiles provided will NOT contain contractions or numbers.  
#       4)Files provided do not contain multiple sentence ending delimiters in sequence, such as an ellipsis (...).
# Input Parameter(s)
#       list_of_file_names: a list of .txt file names
# Return Value(s)
#       A text file called 'HW6_output.txt' that contains every words alphbethically in the
#       appears in the file in list_of_file_names, and the file number each word is in.
#============================================  
def invertFiles(list_of_file_names):
    diction = {}
    
    # Control the filename i.e.1,2,3,4
    #filename = 1
    
    # Mnipulate the files
    for files in list_of_file_names:
        
        # Open files
        with open(files,'r') as aFile: # ! Make sure the dir on the right up corner is same as HW6.py
            doc = aFile.readlines()
            
            filename = int(doc[0])
        
        # Create key for dictionary using words in files
        list_of_word = [] #[] for each file to restart counting on words
        for lines in doc:
            word = re.split("[ .,:;!?\s\b]+|[\r\n]+", lines) #remove all word delimiters
            word = filter(None, word) #remove space
            word = [i.lower() for i in word] #make all words lowercase
            [list_of_word.append(i) for i in word if i not in list_of_word] 
            #use .append(i.lower) for i in word if i not in list_of_word would cause multiple append since I != i
            #list comprehension for list.append(); unify case
        
        # Keep only words as keys and create the dictionary
        for word in list_of_word:
            if word.isdigit(): #get the rid of numbers in the key
                pass
            else:
                if word not in diction:
                    diction[word] = [filename]
                else:
                    diction[word].append(filename)
        
        # Control the filename i.e.1,2,3,4        
        #filename += 1
    
    # Reassign the dictionary SORTED
    diction_sorted = {keys:diction[keys] for keys in sorted(diction.keys())} 
    
    # Write the output to a new file (inverted file )
    new_file = open("HW6_output.txt", "w")
    for keys in diction_sorted:
        # Write again for each value for a key
        for i in range(len(diction_sorted[keys])):
            new_file.write('%s %s\r\n'%(keys,(diction_sorted[keys][i])))
    new_file.close()
        
    # Open and read the file
    #new_file = open("HW6_output.txt", "r")
    #print(new_file.read())

    return
        
'''
invertFiles(['doc6.txt','doc5.txt']) 
    
'''
'''
#check what's in the dir
import os
os.listdir()
'''