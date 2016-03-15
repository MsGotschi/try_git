#Battle v trolls program

print('the hero is fighting against an army of trolls\n')

# initialise the values of the variables the program will need
health=10
trolls=0
damage=3

while health !=0:
    trolls+= 1 # a shorter way of writing trolls=trolls+1
    health -= damage # health = health - damage

    print('hero swings sword and defeats a troll, but takes ', damage,' damage points\n')

print('the hero fought valiantly and defeated ',trolls, 'trolls')
print('but is now dead')
print('press ENTER to exit')
