# CSCI1133,Lab Section 004,lob7 Shanshan Zhong Challenge2
"""
Created on Thu Mar  7 13:33:11 2019

@author: shanshanzhong
"""
#Stock Market Data
import turtle
import time #for web url use
import urllib #website read module
from urllib import request #website read module

# Ask for input
sym = input('Input a stock ticker symbol (Capitalized): ')

beg_m = int(input('Input a beginning month: '))
beg_d = int(input('Input a beginning day: '))
beg_y = int(input('Input a beginning year: '))

end_m = int(input('Input a ending month: '))
end_d = int(input('Input a ending day: '))
end_y = int(input('Input a ending year: '))

# Work on time
t_s = (beg_y,beg_m,beg_d,23,0,0,0,0,0) #9 tuple, adjust EST -> CST (local time)
t_e = (end_y,end_m,end_d,23,0,0,0,0,0)
start = int(time.mktime(t_s)) #change time to int
end = int(time.mktime(t_e))
days = (end-start)//(60*60*24) #total number of days

# Interact w/ web
#Yahoo finance url not work at all; use the Wall Street Journals
startdate = "{}/{:02d}/{}".format(beg_m,beg_d,beg_y) #format date for url use
enddate = "{:02d}/{:02d}/{}".format(end_m,end_d,end_y)
url = 'https://quotes.wsj.com/%s/historical-prices/download?MOD_VIEW=page&num_rows=%d&range_days=%d&startDate=%s&endDate=%s' %(sym,days,days,startdate,enddate)

page_fina =  request.urlopen(url)
htmltext_fina = page_fina.read() #read page
line_fina = htmltext_fina.decode() #remove that 'b'

# Find index for value we want
ind_first_line = line_fina.find('\n')
title = line_fina[:ind_first_line]
ls_tl = title.split(', ')
for i in range(len(ls_tl)):
    print(i,ls_tl[i]) #0 Date;1 Open;4 Close
    
# Get data we need (date,open,close)
ls_text = line_fina.split('\n') #split string into lines(list)
ls_date = []
ls_open = []
ls_close = []
for line in ls_text:
    row = line.split(',') #split lines into elements(list)
    ls_date.append(row[0]) #get data
    ls_open.append(row[1])
    ls_close.append(row[4])

# Drop 'title'
ls_date.pop(0)
ls_open.pop(0)
ls_close.pop(0)

# Reorder data
ls_date.reverse()
ls_open.reverse()
ls_close.reverse()

# Print output
for i,j,k in [(i,j,k) for i in range(len(ls_date)) for j in range(len(ls_open)) for k in range(len(ls_close))]:
    if i==j==k:
        print('%8s %8s %8s'%(ls_date[i],ls_open[j],ls_close[k]))

# Turtle
turtle.showturtle()
t = turtle.Turtle()
d = turtle.Turtle()
d.color("#7D7EC0") #...Doesn't seem to work...

# Manipulate screen
screen = t.getscreen()
ls_open_n = [float(i) for i in ls_open] #change str in list to float
ls_close_n = [float(i) for i in ls_close]
screen.setworldcoordinates(0,min(ls_open_n+ls_close_n),days,max(ls_open_n+ls_close_n))

screen.tracer(100) #speed up turtle
t.goto(0,min(ls_open_n+ls_close_n)) #turtle goes to start point
d.goto(0,min(ls_open_n+ls_close_n)) #turtle goes to start point

# Run turtle
for i in range(len(ls_date)):
    t.goto(i,ls_open_n[i])
    d.goto(i,ls_close_n[i])

screen.update() #...Don't know what's this for...pair with .tracer()
screen.exitonclick()
