#using break and continue in loops - can become confusing!

loop =True
number = 0

while loop:
    print(number)
    number +=1
    if number < 10:
        continue
    else:
        break
    
    
