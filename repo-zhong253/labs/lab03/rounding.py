num_raw = float(input("Input a floating-point number:"))
if num_raw > 0:
    num_round = int(num_raw + 0.5)
    print('The rounded integer is:', num_round)
else:
    num_round = int(num_raw - 0.5)
    print('The rounded integer is:', num_round)
