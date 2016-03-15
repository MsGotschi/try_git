#word jumble
import random

#set up the list of words
WORDS = ('eggs','bacon', 'toast', 'coffee', 'cinnamon buns')

#pick a random word from the list (tuple)
word=random.choice(WORDS)

#save it, so you know which the correct word is
correct = word

#create the jumbled word...start it off empty
jumble=''

#keep jumbling letters while the word still has letters to jumble
while word:

    #pick a random letter to extract
    pos= random.randrange(len(word))
    #concatenate this letter to the jumbled word
    jumble+=word[pos]
    #take it out of the word
    word = word[:pos]+word[pos+1:]

#start the game
print('Welcome to word jumble \n')
print('unscramble the letters to make a breakfast related word\n')
print('press ENTER to quit\n')
print('your jumble is {}'.format(jumble))

guess = input('what is your guess??\n')

while guess!=correct and guess!='':
    print('sorry, that is not it.. try again\n')
    guess = input('guess again?\n')

if guess == correct:
    print('you guessed it!!\n')

print('thanks for playing\n')
input('press enter to exit\n')

    
    
    

