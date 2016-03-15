
'''l = [1,2,3,4,5]

print(l[len(l)-1])

print("list", l) 
del l[1]
print("del l[1] ",l)
l.remove(3)
print("remove 3 ", l)

x=l.pop(2)
print("pop 2", x)
print(l)
l.sort(reverse=True)
print(l)'''


d = {0:"one",0:"two",3:"three"}
'''ok=False
while not ok:
    x=int(input('enter a key as a number'))
    if d.get(x) != None:
        print(d[x])
        ok=True
    else:
        print('that key does not exist, try again')
          
print('done')
'''

print(d)
d[2]='seven'
print(d)
d[5]='five'
print(d)

if 9 in d:
    del d[9]
else:
    print('no such key')
print(d)

