def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b:
        return a
        
    gcd = small = min(a, b)
    big  = max(a, b)
    
    while gcd > 1:
        if gcd == 1:
            return 1
        elif (small % gcd == 0 and big % gcd == 0) :
            return gcd
        else:
            gcd = gcd -1

print('Greatest common divisor: ' + str(gcdIter(9,12)))
