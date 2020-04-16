gen = input('Gender (M or F):')
wei = float(input('Weight in pounds:'))
hei = float(input('Height in inches:'))
age = float(input('Age in years: '))

if gen == 'M':
    BMR=66+(6.3*wei)+(12.9*hei)-(6.8*age)
    print(BMR)
else:
    BMR=655+(4.3*wei)+(4.7*hei)-(4.7*age)
    print(BMR)
