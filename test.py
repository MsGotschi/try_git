#convert a binary number into decimal/denary 

binary = input('enter an 8-bit number in binary - must be only 1s and 0s!')

#only 1s and 0s!

while len(binary)!=8:
    print('Please enter exactly 8 bits!')
    binary = input('enter an 8-bit number in binary - must be only 1s and 0s!')

base=128 #this is the place value of the MSB
#for every character - 1 or 0
decimal = 0 #initial value for decimal number
for x in range(8):
    if binary[x]=='1':
        decimal+=base
        base = base/2

print('your number', binary, 'is = ', decimal)
input('please enter ENTER to exit')
        
    

