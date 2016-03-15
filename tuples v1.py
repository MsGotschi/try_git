#tuples

inventory =('sword', 'armour', 'shield', 'potion')
chest =('gold', 'rubies')

inventory +=chest

if inventory:
    print(inventory)
else:
    print('you are empty handed \n')

l=len(inventory)
print('you have {} items in your inventory'.format(l))


for item in inventory:
    print(item)
    
