annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12
balance = 818

b = balance
for minimumPayment in range(10, int(balance), 10):
    for month in range(12):
        unpaidBalance = b - minimumPayment
        b = unpaidBalance + (annualInterestRate / 12) * unpaidBalance
    if b < 0:
        print('Lowest Payment: ' + str(minimumPayment))
        break
    b = balance
        