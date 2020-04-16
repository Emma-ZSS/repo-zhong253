import math
tolerance = float(input('Enter a tolerance: '))

def estimatePi(tolerance):
    approx_p = 0
    t = 1
    i = 1
    term_0 = 6/math.sqrt(3)
    term = 1/((3**(t-1))*i)
    approx_c = term_0 * (-1)**(t-1) * term
    while abs(approx_p - approx_c) >= tolerance:
        approx_p = approx_c
        t += 1
        i += 2
        
        term_n = 1/((3**(t-1))*i)
        term = term + (term_n*(-1)**(t-1))
        approx_c = term_0 * term
    
    print("The computed value of ​π is ", approx_c)
    print("Number of terms that were required is ", t)
estimatePi(tolerance)

