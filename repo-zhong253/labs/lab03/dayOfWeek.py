import math
m = int(input('Enter month: '))
d = int(input('Enter day: '))
y = int(input('Enter year: '))
if m == 1 or m == 2:
    mm = m + 12
    ym = y - 1
else:
    mm = m
    ym = y
    
date = (d+5+(26*(mm+1)//10)+(5*(ym%100)//4)+(21*(ym//100)//4))%7
week = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
print('%s/%s/%s is a ' % (d,m,y),week[date])
Q = input('Do you wish to continue (y/n)?')
while Q == 'y':
    m = int(input('Enter month: '))
    d = int(input('Enter day: '))
    y = int(input('Enter year: '))
    if m == 1 or m == 2:
        mm = m + 12
        ym = y - 1
    else:
        mm = m
        ym = y
    date = (d+5+(26*(mm+1)//10)+(5*(ym%100)//4)+(21*(ym//100)//4))%7
    week = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    print('%s/%s/%s is a ' % (d,m,y),week[date])
    Q = input('Do you wish to continue (y/n)?')
print('Done.')
