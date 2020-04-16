# CSCI1133,Lab Section 004,lab09 Shanshan Zhong Stretch
"""
Created on Thu Mar 28 01:53:06 2019

@author: shanshanzhong
"""
def morse(message):
    morseDictionary = {' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 
                 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
                 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 
                 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..'}
    mes_cap = message.upper()
    for i in mes_cap:
        print(morseDictionary[i],end=' ')

message = input('Enter a message: ')
morse(message)