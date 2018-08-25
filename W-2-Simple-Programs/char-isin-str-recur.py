def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if (len(aStr) == 0 or char == '' or char == None):
        return False
    elif (len(aStr) == 1):
        if aStr == char:
            return True
        else:
            return False
    else:
        middleCharIndex = len(aStr) // 2
        if aStr[middleCharIndex] == char:
            return True
        elif char > aStr[middleCharIndex]:
            return isIn(char, aStr[middleCharIndex+1:]) # Middle character included in range
        elif char < aStr[middleCharIndex]:
            return isIn(char, aStr[:middleCharIndex:]) # Middle character NOT included in range


print(str(isIn('u', 'abcdefghijklmnopqrstuvwxyz')))
print(str(isIn('c', 'abcdefghijklmnopqrstuvwxyz')))
