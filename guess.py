numToGuess=int(input('player one enter your chosen number\n'))

while numToGuess < 1 or numToGuess >10:
    numToGuess=int(input('not a valid choice, please enter another number\n'))

guess = 0
numOfGuesses = 0

while guess != numToGuess and numOfGuesses <5:
    guess = int(input('player 2 what is your guess?'))
    numOfGuesses+=1

if guess == numToGuess:
    print('player two wins')
else:
    print('player one wins')
