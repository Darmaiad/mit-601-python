print('Please think of a number between 0 and 100! ')
high = 100
low = 0
found = False
while not found:
    guess = (high + low)  // 2
    print('Is your secret number ' + str(guess) + '?')
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if hint == 'h':
        high = guess
    elif hint == 'l':
        low = guess
    elif hint == 'c':
        found = True
        print('Game over. Your secret number was: ' + str(guess))
    else:
        print('Sorry, I did not understand your input.')
    