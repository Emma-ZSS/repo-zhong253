t = float(input("Enter a temperature in degrees Fahrenheit: "))
v = float(input("Enter a wind velocity in miles/hour: "))
windChill = 35.74 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
print(windChill)
