Q = input('Start? (Y or N)')
while Q == 'Y':
    value = float(input('Enter a value: '))
    unit = input('Enter a unit: ')
    if unit == "pounds":
        value_n=value/2.205
        print(value, unit, 'is ', format(round(value_n,4)),'kilos')
    elif unit == "ounces":
        value_n = value*28.3495
        print(value, unit, 'is ', format(round(value_n,4)), 'grams')
    elif unit == "miles":
        value_n = value*1.60934
        print(value, unit, 'is ', format(round(value_n,4)), 'kilometers')
    elif unit == "inches":
        value_n = value*2.54
        print(value, unit, 'is ', format(round(value_n,4)), 'centimeters')
    elif unit == "kilos":
        value_n=value*2.205
        print(value, unit, 'is ', format(round(value_n,4)), 'pounds')
    elif unit == "grams":
        value_n = value/28.3495
        print(value, unit, 'is ', format(round(value_n,4)), 'ounces')
    elif unit == "kilometers":
        value_n = value/1.60934
        print(value, unit, 'is ', format(round(value_n,4)), 'miles')
    elif unit == "centimeters":
        value_n = value/2.54
        print(value, unit, 'is ', format(round(value_n,4)), 'inches')
    else:
        print('Error!')
    Q = input('Continue? (Y or N)')
print('Thank you! :)')

