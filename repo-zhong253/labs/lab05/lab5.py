# CSCI1133,Lab Section 004,lab05 Shanshan Zhong,lab5
"""
Created on Thu Feb 21 13:54:51 2019

@author: shanshanzhong
"""
s = input('Enter a sentence: ') # last index of string removed
con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']
vow = ['a','e','i','o','u']
output = []

# if there is a punctuation or not
if s[-1] not in con+vow:
    p = s[-1]
    s = s[:-1]
else: p = ''

s_l = s.split(' ') # split the sentence into list by ' '
for word in s_l: # word is str
    word = word.lower()
    n = len(word)
    first = ''
    # For other situations
    if word[0] in vow:
        word_n = word + 'way'
        output.append(word_n)
    else: # For any word that begins with one or more consonants
        for i in range(0,n):
            if word[i] in con:
                first += word[i]
                word_n = word + first + 'ay'
                word_n = word_n[i+1:]
            else: break
        output.append(word_n)

# combine list and print output
sp = ' '
output = sp.join(output)
final_output = output.capitalize() + p
print(final_output)
