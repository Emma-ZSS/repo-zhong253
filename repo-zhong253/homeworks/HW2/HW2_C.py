#CSCI1133,Lab Section 004,HW2 Shanshan Zhong,Problem2C

import math
# Define the calories_short function
def calories_short(h,w,hr,age,t):
    return((age*0.074)+(hr*0.4472)-(w*0.05741)-20.4022)*(t)//4.184

# Define the calories_tall function
def calories_tall(h,w,hr,age,t):
    return((age*0.2017)+(hr*0.6309)-(w*0.09036)-55.0969)*(t)//4.184

# Define the main function
def main(h,w,hr,age,t):
    print('You entered the following information:')
    print('Height:', "{:.1f}".format(h))
    print('Body weight: %d' % w)
    print('Average heart rate: %d' % hr)
    print('Age: %d' % age)
    print('Duration of workout: %d' % t)
    if h <= 5.6:
        print('The number of calories burned for this short person is %d calories.' % calories_short(h,w,hr,age,t))
    else:
        print('The number of calories burned for this short person is %d calories.' % calories_tall(h,w,hr,age,t))

# Input and run functions
h = float(input('Please input the height of the person (for example, 5.6 means 5 feet 6 inches): '))
w = float(input('Please input the body weight of person, in pounds: '))
hr = float(input('Please input the average heart rate of the person during the workout, in beats per minute: '))
age = float(input('Please input the age of the person, in years: '))
t = float(input('Please input the duration of the workout of the person, in minutes: '))
main(h,w,hr,age,t)
