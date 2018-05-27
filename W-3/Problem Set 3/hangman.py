from availableLetters import getAvailableLetters
from guessedWord import getGuessedWord
from wordGuessed import isWordGuessed

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + ' letters long.')

    guessesLeft = 8
    lettersGuessed = []

    while (True):
      print('-----------')
      if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
        break
      elif guessesLeft == 0:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)
        break
      else:
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))

        guess = input('Please guess a letter: ').lower()

        if not guess in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word: ' +
                      getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1
        else:
            print("Oops! You've already guessed that letter: " +
                  getGuessedWord(secretWord, lettersGuessed))
