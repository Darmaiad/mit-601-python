def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if (exp == 0):
        return 1
    total = base
    for e in range (1, exp ):
        total*=base
    return total

print(iterPower(0.2,0))

