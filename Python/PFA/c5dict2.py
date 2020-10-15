def addToInventory(inventory, addedItems):
    total=0
    for k,v in inventory.items():
            for i in addedItems:
                if i==k:
                    total = total + 1
                    inventory[k] = v + total
                elif(i=='ruby' or i=='dagger') :
                    inventory[i]=1
    return inventory

def displayInventory(inv):
    a=[]
    a=inv.values()
    for x, y in inv.items():
        print y,x
    SUM = sum(a)
    print "Total Number of items:",SUM


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
