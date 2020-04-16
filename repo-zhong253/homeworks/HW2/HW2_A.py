#CSCI1133,Lab Section 004,HW2 Shanshan Zhong,Problem2A

import math

# Define the poiseuille function
def poiseuille(L,r,n):
    return((8*n*L)/((math.pi)*(r**4)))
    
# Define the main function
def main(L,r,n):
    if (L > 0) and (r >0) and (n > 0):
        print('The resistance is: ', poiseuille(L,r,n))
    else:
        print('Failed due to input error. Please make sure your inputs are all positive. Exiting program.')

# Input and run funtions
L = float(input('Please enter the length: '))
r = float(input('Please enter the radius: '))
n = float(input('Please enter the viscosity: '))
main(L,r,n)
