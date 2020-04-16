# CSCI1133,Lab Section 004, lab 10 Shanshan Zhong Stretch
"""
Created on Thu Apr  4 12:53:26 2019

@author: shanshanzhong
"""
#1)
class Sentence:
    def __init__(self,string):
        self.sentence = string
    
    def getSentence(self):
        return self.sentence
    
    def getWords(self):
        self.words = self.sentence.split()
        return self.words
    
    def getLength(self):
        return len(self.sentence)
    
    def getNumWords(self):
        self.words = self.sentence.split()
        return len(self.words)
    
s = Sentence('hello how are you')
s.getSentence()
s.getWords()
s.getNumWords()
s.getLength()

#2)
class SentenceV1:
    def __init__(self,string):
        self.list = string.split()
    
    def getSentence(self):
        self.sentence = [[" ".join(i)] for i in self.list]
        return self.sentence
    
    def getWords(self):
        return self.list
    
    def getLength(self):
        return len(self.sentence)
    
    def getNumWords(self):
        self.words = self.sentence.split()
        return len(self.words)  
    
s1 = Sentence('hello how are you')
s1.getSentence()
s1.getWords()
s1.getNumWords()
s1.getLength()
