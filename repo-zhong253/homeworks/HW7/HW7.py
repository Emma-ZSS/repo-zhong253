# CSCI1133,Lab Section 004,HW 7 Shanshan Zhong
"""
Created on Sun Apr 14 15:09:18 2019

@author: shanshanzhong
"""
# A.
#============================================
# Name: __init__(self,start= time(), end= time())
# Purpose: Initialize the values of instance members for the 
#       new object everytime it is called
# Precondition:  
#       Sets both start and end times with the current time of day 
#       as returned by the time()function
# Input Parameter(s)
#       --self
#       --Start & End: float of seconds
# Return Value(s)
#       None
#
# Name: get_start(self) & get_end(self)
# Purpose: Return the value stored in the instance variables start/end
# Precondition:  
#       None
# Input Parameter(s)
#       self
# Return Value(s)
#       Return the value stored in the instance variables start/end
#
# Name: current_time(self)
# Purpose: Return the current local time in the form: HH:MM:SS
# Precondition:  
#       --HH is the number of hours in military time (0 –23);
#       --MM is a the number of  minutes(a number in the range 0 and 59);
#       --SS is the number of seconds (a number in the range 0 -59).
# Input Parameter(s)
#       self
# Return Value(s)
#       Return the current local time in the form: HH:MM:SS
#
# Name: set_start(self) & set_end(self)
# Purpose: Reset start/end to the current time
# Precondition:  
#       Current time is in seconds
# Input Parameter(s)
#       self
# Return Value(s)
#       Returns the current time in seconds
#
# Name: elapsed_time(self)
# Purpose: Returns the elapsed time for the stop watch as a float.
# Precondition:  
#       Difference between the end time(float) and the start time(float)
# Input Parameter(s)
#       self
# Return Value(s)
#       Returns the elapsed time for the stop watch as a float.
#============================================   
from time import time, localtime
import random
class StopWatch:
    def __init__(self,start= time(), end= time()):
        self.start = start
        self.end = end
        
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end
    
    def current_time(self):
        self.t = localtime(time())
        return("{:02d}:{:02d}:{:02d}").format(self.t.tm_hour,self.t.tm_min,self.t.tm_sec)
      
    def set_start(self):
        self.start = time()

    def set_end(self):
        self.end = time()
        
    def elapsed_time(self):
        self.e_s = self.end-self.start
        #self.sec = (self.e_s%3600)%60
        #self.min = (self.e_s%3600)//60
        #self.hr = self.e_s//3600
        #return("{0:.1f} {0:.1f} {0:.1f}").format(self.hr,self.min,self.sec)
        return ("{0:.1f}").format(self.e_s)

if __name__ == '__main__':
#1.    
    t=StopWatch()
    print(t.current_time())

#2.
    mylist = []
    for i in range(30000):
        random.randint(0,10000)
        mylist.append(i)
    t.set_start()
    mylist.sort()
    t.set_end()
    print(t.elapsed_time())

#3.  
    t=StopWatch()
    print(t.current_time())

#4.
    t=StopWatch() 
    mylist = []
    for i in range(50000):
        random.randint(0,10000)
        mylist.append(i)
    t.set_start()
    mylist.sort()
    t.set_end()
    print(t.elapsed_time())

#5.    
    t=StopWatch() 
    print(t.current_time())

# B.
#============================================
# Name: __init__(self,game_title,ESRB_rating,list_of_ratings=[0])
# Purpose: Initialize the values of instance members for the 
#       new object everytime it is called
#       Create an object of type VideoGame with the game title, ESRB rating, and parameter for the list of ratings for each category
# Precondition:  
#       --list of ratings should be saved as a single instance variable
# Input Parameter(s)
#       --self
#       --game_title: string
#       --ESRB_rating: string (E, E10+, T, M, AO, RP)
#       --list_of_ratings: 1 (Awesome),2 (Great),3 (Good),4 (Poor),5 (Horrid)
# Return Value(s)
#       --If the “list of ratings” parameter is not included in the call,return [0]
#
# Name: set_title(self,title) & set_esrb(self,esrb)
# Purpose: Reset title/esrb to the input(parameter)
# Precondition:  
#       title is string; esrb is string
# Input Parameter(s)
#       --self
#       --title: string
#       --esrb: string
# Return Value(s)
#       None
#
# Name: get_title(self) & get_esrb(self)
# Purpose: Return the value stored in the instance variables title/esrb
# Precondition:  
#       None
# Input Parameter(s)
#       self
# Return Value(s)
#       Return the value stored in the instance variables title/esrb
#
# Name: get_average(self)
# Purpose: Returns the average value for all of the ratings for a video game
# Precondition:  
#       Ratings for a video game is in stored in a list under list_of_rating parameter
# Input Parameter(s)
#       self
# Return Value(s)
#       Returns the average value for all of the ratings for a video game as an integer by truncating the original value.
#
# Name: __str__(self)
# Purpose: Returns a string containing the game title, ESRB rating and average rating in certain form
# Precondition:  
#       game_title: string
#       ESRB_rating: string
#       list_of_rating: list
# Input Parameter(s)
#       self
# Return Value(s)
#       Returns in the form:
#       Title: Call of Duty, ESRB Rating: AO, Average Rating: 4
#============================================  
class VideoGame:
    def __init__(self,game_title,ESRB_rating,list_of_ratings=[0]):
        self.gt = game_title
        self.ESRB = ESRB_rating
        self.rate = list_of_ratings
        
        
    def set_title(self,title):
        self.gt = title
    
    def set_esrb(self,esrb):
        self.ESRB = esrb
    
    def get_title(self):
        return self.gt
    
    def get_esrb(self):
        return self.ESRB  
    
    def get_average(self):
        self.sum_rate = sum(self.rate)
        self.len_rate = len(self.rate)
        self.ave = self.sum_rate//self.len_rate #turncate
        return self.ave
    
    def __str__(self):
        return('Title: %s, ESRB Rating: %s, Average Rating: %d')%(self.gt,self.ESRB,self.ave)

if __name__ == '__main__':    
#creat list data and add objects   
    data = []   
    a = VideoGame('Red Dead Redemption 2','M')
    data.append(a)
    b = VideoGame('Age of Empires II: Definitive Edition','T',[1,5,4,2,4])
    data.append(b)
    c = VideoGame('FTL: Faster Than Light','E10+',[1,2,3,2,1,3,1,2])
    data.append(c)

#loop and print each
    for i in data:
        print('Title: ',i.gt)
        print('ESRB Rating:',i.ESRB)
        print('Average Rating: ',i.rate)

#change title    
    data[0].set_title('New Title')
    data[0].get_title()

#change esrb
    data[1].set_esrb('E')
    data[1].get_esrb()

#print all
    for i in data:
        i.get_average()
        print(i)
