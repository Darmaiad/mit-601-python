import string 

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    alphabet = string.ascii_lowercase
    subAlphabet = alphabet
    for letterGuessed in lettersGuessed:
        letterGuessedIndex = subAlphabet.find(letterGuessed)
        if letterGuessedIndex != -1:
            subAlphabet = subAlphabet[:letterGuessedIndex] + subAlphabet[letterGuessedIndex+1:]

    return subAlphabet
