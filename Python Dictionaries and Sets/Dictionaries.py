fruit = {"orange": "a sweet orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "round and crunchy"}

print(fruit)
print(fruit["lemon"])

bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engineSize": 250}
print(bike["engineSize"])
print(bike["colour"])

print(fruit)
print(fruit["lemon"])
fruit["pear"] = "an odd shaped apple"
print(fruit)
fruit["pear"] = "great with tequila"
print(fruit)

# del fruit["lemon"]
# print(fruit)
# fruit.clear()
# print(fruit)

# while True:
#     dictKey = input("Please enter a fruit: ")
#     if dictKey == "quit":
#         break
#     description = fruit.get(dictKey, "We don't have a " + dictKey)
#     print(description)
#     # if dictKey in fruit:
#     #     description = fruit[dictKey]
#     #     print(description)
#     # else:
#     #     print("We don't have a " + dictKey)

for snack in fruit:
    print(fruit[snack])

# orderedKeys = list(fruit.keys())
# orderedKeys.sort()

orderedKeys = sorted(list(fruit.keys()))

for f in orderedKeys:
    print(f + " - " + fruit[f])

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

print('-' * 40)
for key in fruit:
    print(fruit[key])

fruitKeys = fruit.keys()
print(fruitKeys)

fruit["tomato"] = "not nice with ice cream"
print(fruitKeys)

print(fruit.items())
fruitTuple = tuple(fruit.items())
print(fruitTuple)

for snack in fruitTuple:
    item, description = snack
    print(item + " is " + description)

print(dict(fruitTuple))
