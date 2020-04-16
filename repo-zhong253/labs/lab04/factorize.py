def factorize():
    x = int(input("Input a positive integer: "))
    list_str = []
    for i in range(2, x+1):
        while x%i == 0:
            x = x/i
            list_str.append(str(i))
            m='*'
            m = m.join(list_str) 
    print("Factors: ", m)

def main():
    factorize()
    q = input("Continue (y/n)?")
    while q == 'y':
        factorize()
        q = input("Continue (y/n)?")
    

main()
