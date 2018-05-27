def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    total = 0
    for e in range (1, exp):
        total+=base*e
    return total
