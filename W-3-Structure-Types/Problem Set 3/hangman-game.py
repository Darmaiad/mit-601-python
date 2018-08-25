import ps3_hangman as initialiser
from hangman import hangman

WORDLIST_FILENAME = "C:\\Users\\George\\Desktop\\Programming Projects\\mit-6.00.01x-python\\W-3\\Problem Set 3\\words.txt"

secretWord = initialiser.chooseWord(initialiser.loadWords(WORDLIST_FILENAME))

hangman(secretWord)
