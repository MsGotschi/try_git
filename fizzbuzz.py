#fizzbuzz Year 12 homework Mon 21st Sept

#ask the user for the ending value
count = int (input('how far to count\n'))

#make sure they have answered something >1
while count < 1:
    print('that was not a valid value, please enter something >1\n')
    count = int (input('how far to count\n'))

#go through every value and check

for myLoop in range(1,count+1): #must go to count +1 otherwise it stops before end
    if myLoop%3 == 0 and myLoop%5==0:
        print(myLoop,'=fizzbuzz')
    elif myLoop%3 == 0:
            print(myLoop,'=fizz');
    elif myLoop%5==0:
        print(myLoop,'=buzz');
    else:
        print(myLoop);

print('the end \n')
            
