# CSCI1133,Lab Section 004,HW # Shanshan Zhong
"""
Created on Thu Apr 18 13:58:32 2019

@author: shanshanzhong
"""
# 1.
def reverseList(mylist):
    if len(mylist) == 0:
        return []
    else:
        return [mylist[-1]]+reverseList(mylist[:-1])

reverseList([1,2,3,4])
reverseList([[1,2],3,4])

# 2.
def reverseString(mystr):
    if mystr == '':
        return ''
    else:
        return mystr[-1] + reverseString(mystr[:-1])

reverseString('shana')
reverseString('gogototheriver')

# 3.
def noDupKeys(diction1,diction2):
    dict3 = {}
    for i in diction1:
        if i not in diction2:
            dict3[i]=diction1[i]
    for j in diction2:
        if j not in diction1:
            dict3[j]=diction2[j]
    return dict3

noDupKeys({"a":3,"d":5,"mm":66,"ab":3},{"a":3,"d":5,"mm":66,"ab":3})
noDupKeys({"a":3,"d":5,"mm":66,"ab":3},{"a":6,"mm":66,"acccc":2})

# 4.
class Genus:
    def __init__(self,genus='unknown'):
        self.genus = genus
        
    def speak(self):
        return ("I speak but cannot say for certain what I sound like")
    
    def __str__(self):
        return ("I am animal of genus: " + self.genus)
    
class Dog(Genus):
    species = "Canis familiaris"
    
    def __init__(self,name,age,breed="unknwon",genus="unknown"):
        Genus.__init__(self,genus)
        self.name = name
        self.age = age
        self.breed = breed
        
    def description(self):
        return (self.name + " is " + self.age)
        
    def speak(self,sound):
        return "{} says {}".format(self.name,sound)
    
    def __eq__(self,other):
        return (self.breed == other.breed) and (self.genus == other.genus)
    
    def set_genus(self,val):
        self.genus = val
   
    def get_genus(self):
        return self.genus
    
    def whoIsOlder(self,other):
        if self.age == other.age:
            print('they are the same age')
        elif self.age > other.age:
            print(self.name + ' is older by '+ str(self.age-other.age) + ' years.')
        else:
            print(other.name + ' is older by '+str(other.age-self.age) + ' years.')
        
abby = Dog('Abby',12,'pit bull','Canis')  
jack = Dog('Jack',9,'australian cattle dog','Canis')    
shawn = Dog('Shawn',11,'pit bull','Canis')
    
print(abby)
print(jack)    
    
print(Dog.species)
print(abby.species)  
    
abby == jack   
abby == shawn

sasha = Dog("Sasha",14)
sasha

print(abby)

jack.speak('howl')

abby.set_genus('cats')
print(abby)

abby.get_genus()
Dog.whoIsOlder(abby,jack)
