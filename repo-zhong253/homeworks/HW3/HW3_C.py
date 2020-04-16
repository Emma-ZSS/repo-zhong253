#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 16:25:48 2019

@author: shanshanzhong
"""
# CSCI1133,Lab Section 004,HW3 Shanshan Zhong,Problem3C

def main():
    print('Welcome to the installment loan evaluation program')
    P = float(input('Please input the amount of money you will be borrowing: '))
    R = float(input('Please input the interest rate (i.e enter 15 for 15%): '))
    t = int(input('Please input the term for the loan (in years): '))
    
    if (100 <= P <= 1000) and (0 < R <= 15) and (0 < t <= 10):
        i = P * (R/100) * t
        F = P + i
        print('The face value of the loan is: $',"{:.2f}".format(F))
        print('Your monthly payment each month for 24 months is: $',"{:.2f}".format(F/24))
    elif P < 100:
        print('Error: The amount of principal is too low, the minimum is $100.')
    elif P > 1000:
        print('Error: The amount of principal is too high, the maximum is $1000.')  
    elif R <= 0:
        print('Error: The amount of principal is too low, the minimum is 0.')
    elif P > 15:
        print('Error: The amount of principal is too high, the maximum is 15 percent.')   
    elif t <= 0:
        print('Error: The term of loan is too short, the minimum is 0.')
    elif t > 10:
        print('Error: The term of loan is too long, the maximum is 10.')

    

main()