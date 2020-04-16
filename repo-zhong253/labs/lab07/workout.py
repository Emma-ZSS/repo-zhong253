# CSCI1133,Lab Section 004,lab07 Shanshan Zhong Workout
"""
Created on Thu Mar  7 12:14:49 2019

@author: shanshanzhong
"""
#Earthquake Data, part 1
with open("/Users/shanshanzhong/CSCI1133_S19/repo-zhong253/labs/lab07/2.5_day.csv","r") as earthq1:
    first_line = earthq1.readline()
    print(first_line)
    ls = first_line.split(",")
    new_ls=[]
    for i in range(len(ls)):
        print(format(i+1,"2d"),ls[i])
        
#​Earthquake Data, part 2
with open("/Users/shanshanzhong/CSCI1133_S19/repo-zhong253/labs/lab07/2.5_day.csv","r") as earthq2:
    ls_line = []
    ls_place =[]
    ls_mag = []
    for lines in earthq2:
        lines = lines.replace('"',"")
        lines = lines.replace(' ',"") #clean up the lines
        ls_line = lines.split(",") #lines -> lists
        
        ls_mag.append(ls_line[4]) #assign list of magnitudes, index from Q above
        ls_place.append(ls_line[14]) #assign list of locations, index from Q above
    ls_place.pop(0)#remove original "title"
    ls_place.insert(0,"location")#add new "title", change title due to the ','
    for i, j in [(i,j) for i in range(len(ls_mag)) for j in range(len(ls_place))]:
        if i==j:
            print("%5s %s"%(ls_mag[i],ls_place[j]))#format the string & print
    

        
            