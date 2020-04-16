import math
import random

def estimatePi(sampleSize):
    d_in = []
    d_out = []
    # repeat sampleSize times
    for i in range(0,sampleSize):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        r = math.sqrt(x**2+y**2)
        if (r <= 1):
            d_in.append(1)
        else:
            d_out.append(0)
    d_in = d_in.count(1)
    d_out = d_out.count(0)
    p = d_in/sampleSize
    Pi = p*4
    print(Pi)

def loop():
    sampleSize = int(input('Enter a sample size: '))
    estimatePi(sampleSize)
    ans = input("Do you want to continue (y/n)?")
    while ans == 'y':
        sampleSize = int(input('Enter a sample size: '))
        estimatePi(sampleSize)
        ans = input("Do you want to continue (y/n)?")
    print('Thank you! Bye!')


loop()
    
