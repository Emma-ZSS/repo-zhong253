# CSCI1133,Lab Section 004,lob7 Shanshan Zhong Challenge1
"""
Created on Thu Mar  7 13:33:11 2019

@author: shanshanzhong
"""
#Reading Internet Data
import urllib #website read module
help(urllib) 

from urllib import request #website read module
page =  request.urlopen("http://cs.umn.edu")
htmltext = page.readline()#read first line
htmltext

#The string starts with ​b'instead of the usual quotation mark
#This is actually a ​byte array​ and needs to be converted to a string
#before we try to do the usual string operations:
line = htmltext.decode()
line
