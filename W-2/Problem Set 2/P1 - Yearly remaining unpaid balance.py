annualInterestRate = 0.2
balance = 484
monthlyPaymentRate = 0.04

for month in range(1, 13):
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    balance = unpaidBalance + (annualInterestRate / 12) * unpaidBalance

print('Remaining balance: ' + format(balance, '.2f'))
