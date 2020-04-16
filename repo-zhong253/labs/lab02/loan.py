loan_amount = float(input("Enter a loan amount: "))
annual_r = float(input("Enter an annual interest rate: "))
n = float(input("Enter a loan duration in months: "))
r = annual_r/12
payment = r*loan_amount/(1-(1+r)**(-n))
print(payment)
