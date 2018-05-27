def f(i):
    print('fi:' + str(i+2))
    return i + 2
def g(i):
    print('gi:' + str(i>5))
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    tempList = L[:]
    for listItem in tempList:
        if not g(f(listItem)):
            L.remove(listItem)
    if len(L) == 0:
        return -1
    else:
        return max(L)

L = []
print(applyF_filterG(L, f, g))
print(L)