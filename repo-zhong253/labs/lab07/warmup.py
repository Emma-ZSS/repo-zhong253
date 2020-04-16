# CSCI1133,Lab Section 004,Lab7 Shanshan Zhong Warmup
"""
Created on Mon Mar  4 18:46:08 2019

@author: shanshanzhong
"""
#Review from Pre-Exercise:
s = "  There... are... a... lot ...of: delimiters,,, Ryan?!!!"
for i in s:
    if i in [".",",","?","!",":"]:
        s = s.replace(i,"") #replace function
print(s)

s = s.lstrip() #remove spaces from the beginning
print(s)

s = s.replace(" Ryan",", Fred")
print(s)

s_ls = s.split()
print(s_ls)


#Primer on CSV File Format
filename = "somefile.txt"
fileobj = open('/Users/shanshanzhong/Desktop/somefile.txt','w')
for i in range(3):    
    record = ''  # start with a null string    
    for j in range(1,4):        
        record += str(i*3+j) + ','  # append each value and comma    
    record = record[:-1]  # strip off the last comma    
    fileobj.write(record)    
    if i < 2:
        fileobj.write('\n')  # no \n on last record!
fileobj.close()

#Generating Synthetic Test Data
import random
filename = input("Name your file: ")
filedir = '/Users/shanshanzhong/Desktop/'+filename
fileobj = open(filedir,'w')   #need to be a dir to open
for i in range(1,1001):    
    record = ''  # start with a null string    
    rand = random.randint(-1000,1000)
    record = str(i) + ',' + str(rand) # append each value and comma     
    fileobj.write(record)    
    if i < 1000:
        fileobj.write('\n')  # no \n on last record!
fileobj.close()




