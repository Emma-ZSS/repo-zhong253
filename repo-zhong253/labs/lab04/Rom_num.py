def Rom_num(num):
    print_str = ''
    if 1 <= num <= 999:
        while num >= 1000:
            print_str += "M"
            num -= 1000
        while num >= 900:
            print_str += "CM"
            num -= 900
        while num >= 500:
            print_str += "D"
            num -= 500
        while num >= 400:
            print_str += "CD"
            num -= 400
        while num >= 100:
            print_str += "C"
            num -= 100
        while num >= 90:
            print_str += "XC"
            num -= 90
        while num >= 50:
            print_str += "L"
            num -= 50
        while num >= 40:
            print_str += "XL"
            num -= 40
        while num >= 10:
            print_str += "X"
            num -= 10
        while num >= 9:
            print_str += "IX"
            num -= 9
        while num >= 5:
            print_str += "V"
            num -= 5
        while num >= 4:
            print_str += "IV"
            num -= 4
        while num >= 1:
            print_str += "I"
            num -= 1
        print('Roman numeral equivalent: %s' % print_str)
    else:
        print('Invalid input')

def main():
    num = int(input('Enter an integer value from 1 to 999: '))
    Rom_num(num)
    q = input('Continue? (y/n)')
    while q == 'y':
        num = int(input('Enter an integer value from 1 to 999: '))
        Rom_num(num)
        q = input('Continue? (y/n)')
    print('Thanks! Bye!')

main()
