import shelve

with shelve.open('shelfTest') as fruit:
    fruit['orange'] = 'a sweet, orange, citrus fruit'
    fruit['apple'] = 'good for making cider'
    fruit['lemon'] = 'a sour, yellow citrus fruit'
    fruit['grape'] = 'a small, sweet fruit growing in bunches'
    fruit['lime'] = 'a sour, green citrus fruit'

    print(fruit['lemon'])
    print(fruit['grape'])

print(fruit)

newFruit = shelve.open('newShelfTest')

newFruit['orange'] = 'a sweet, orange, citrus fruit'
newFruit['apple'] = 'good for making cider'
newFruit['lemon'] = 'a sour, yellow citrus newFruit'
newFruit['grape'] = 'a small, sweet fruit growing in bunches'
newFruit['lime'] = 'a sour, green citrus fruit'

print(newFruit['lemon'])
print(newFruit['grape'])

newFruit['lime'] = 'great with tequila'

for snack in newFruit:
    print(snack + ": " + newFruit[snack])

while True:
    dictKey = input("Please enter a fruit: ")
    if dictKey == "quit":
        break

    if dictKey in newFruit:
        description = newFruit[dictKey]
        print(description)
    else:
        print("We don't have a " + dictKey)

orderedKeys = list(newFruit.keys())
orderedKeys.sort()

for f in orderedKeys:
    print(f + " - " + newFruit[f])

for v in newFruit.values():
    print(v)

print(newFruit.values())

for f in newFruit.items():
    print(f)

print(newFruit.items())

newFruit.close()

print(newFruit)

