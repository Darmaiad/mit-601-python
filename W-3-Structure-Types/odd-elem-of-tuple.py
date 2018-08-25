aTestTup = ('I', 'am', 'a', 'test', 'tuple')
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    for index, elem in enumerate(aTup, start = 1):
        if index % 2 != 0:
            newTup += (elem,)
    return newTup

print(oddTuples(aTestTup))
