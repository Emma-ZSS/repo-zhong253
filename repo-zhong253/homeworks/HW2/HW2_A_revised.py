#CSCI1133,Lab Section 004,HW2 Shanshan Zhong,Problem2A

import math

# Define the poiseuille function
def poiseuille(length,radius,viscosity):
    if (length > 0) and (radius > 0) and (viscosity > 0):
        print('The resistance is: ', (8*viscosity*length)/((math.pi)*(radius**4)))
    else:
        print('Failed due to input error. Please make sure your inputs are all positive. Exiting program.')
    
    
# Define the main function
def main():
    length = float(input('Please enter the length: '))
    radius = float(input('Please enter the radius: '))
    viscosity = float(input('Please enter the viscosity: '))
    poiseuille(length,radius,viscosity)
    

# Input and run funtions
main()
