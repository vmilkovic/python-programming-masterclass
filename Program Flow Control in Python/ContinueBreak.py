shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shoppingList:
    if item == 'spam':
        print("I am ignoring " + item)
        continue

    print("Buy " + item)

for item in shoppingList:
    if item == 'spam':
        break

    print("Buy " + item)

meal = ["egg", "bacon", "beans", "sausages"]
nastyFoodItem = ''
for item in meal:
    if item == 'spam':
        nastyFoodItem = item
        break
else:
    print("I'll have a plate of that, then please")

if nastyFoodItem:
    print("Cat't I have anything without spam in it")
