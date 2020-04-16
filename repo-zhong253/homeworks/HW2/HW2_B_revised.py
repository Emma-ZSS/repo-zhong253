#CSCI1133,Lab Section 004,HW2 Shanshan Zhong,Problem2B

import turtle

# Define the fourSidedStar
def fourSidedStar(lengthOfSide):
    turtle.showturtle()
    turtle.left(75)
    turtle.forward(lengthOfSide)
    turtle.right(60)
    turtle.forward(lengthOfSide)
    turtle.left(150)
    turtle.forward(lengthOfSide)
    turtle.right(60)
    turtle.forward(lengthOfSide)
    turtle.left(150)
    turtle.forward(lengthOfSide)
    turtle.right(60)
    turtle.forward(lengthOfSide)
    turtle.left(150)
    turtle.forward(lengthOfSide)
    turtle.right(60)
    turtle.forward(lengthOfSide)

# Define the main function
def main():
    lengthOfSide = float(input('Enter the length of side: '))
    fourSidedStar(lengthOfSide)

#Input and run functions:

main()
