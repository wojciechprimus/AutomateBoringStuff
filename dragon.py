from collections import Counter

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope':1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+ ' ' + k)
        item_total += v
    print("Total number of items in Inventory: " + str(item_total))

z = dict(Counter(dragonLoot)+ Counter(inv))
displayInventory(z)
