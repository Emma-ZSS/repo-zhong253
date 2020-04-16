#CSCI1133,Lab Section 004,HW3 Shanshan Zhong,Problem3A

def RBG_to_CMYK(R,G,B):
    R1 = R/255
    G1 = G/255
    B1 = B/255
    CMYK = []
    K= 1 - max(R1, G1, B1)
    if K == 1:
       C = 0
       M = 0
       Y = 0
       CMYK.append(C)
       CMYK.append(M)
       CMYK.append(Y)
       CMYK.append(K)
    else:
        C = (1-R1-K)/(1-K)
        M = (1-G1-K)/(1-K)
        Y = (1-B1-K)/(1-K)
        CMYK.append(C)
        CMYK.append(M)
        CMYK.append(Y)
        CMYK.append(K)
    CMYK = [round(100*x) for x in CMYK]
    CMYK = " ".join(str(x) for x in CMYK)
    print('CMYK representation: %s' % CMYK)
    

def main():
    R = int(input('Red component: '))
    G = int(input('Green component: '))
    B = int(input('Blue component: '))
    RBG_to_CMYK(R,G,B)


main()
