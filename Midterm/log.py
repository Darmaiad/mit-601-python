number = 64
base = 2

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''

    power = 1
    ans = 0
    while(True):
        if (b**power <= x):
            ans = power
            power +=1
        else: 
            break
    return ans

print('Log of: ' + str(number) + ' with base: ' + str(base) + ' is: ' + str(myLog(number, base)))