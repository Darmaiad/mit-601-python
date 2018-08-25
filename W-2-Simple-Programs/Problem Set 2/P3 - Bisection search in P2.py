annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12
balance = 999999

lower = balance / 12
upper = (balance * (1 + (annualInterestRate / 12))**12) / 12
iters = 0
while (True):
    iters += 1
    b = balance
    midPoint = (lower + upper) / 2

    for month in range(12):
        unpaidBalance = b - midPoint
        b = unpaidBalance + (annualInterestRate / 12) * unpaidBalance

    if abs(b) <= 0.00000001:
        print('Lowest Payment: ' + str(format(midPoint, '.2f')))
        break
    if b < 0:
        upper = midPoint
    else:
        lower = midPoint
print('No of iters: ' +  str(iters))
