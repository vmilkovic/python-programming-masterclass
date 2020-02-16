farmAnimals = {"sheep", "cow", "hen"}
print(farmAnimals)

for animal in farmAnimals:
    print(animal)

print("=" * 40)

wildAnimals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wildAnimals)

for animal in wildAnimals:
    print(animal)

farmAnimals.add("horse")
wildAnimals.add("horse")
print(farmAnimals)
print(wildAnimals)

emptySet = set()
# emptySet2 = {}  #dictionary
emptySet.add("a")
# emptySet2.add("a")  #error

even = set(range(0, 40, 2))
print(even)
squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)
print(squares)

even = set(range(0, 40, 2))
print(even)
print(len(even))

squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))
print(squares.union(even))

print("-" * 40)

print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

even = set(range(0, 40, 2))
print(sorted(even))

squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)
print(sorted(squares))

print("Even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("Squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

print("=" * 40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

even = set(range(0, 40, 2))
print(sorted(even))

squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)
print(sorted(squares))

print("Symmetric even minus squares")
print(even ^ squares)
print(sorted(even.symmetric_difference(squares)))

print("Symmetric squares minus even")
print(squares ^ even)
print(sorted(squares.symmetric_difference(even)))

squares.discard(4)
squares.remove(16)  # error if not exits in set
squares.discard(8)
print(squares)
try:
    squares.remove(8)  # error if no try
except KeyError:
    print("The item 8 is not a member of the set")

even = set(range(0, 40, 2))
print(sorted(even))

squaresTuple = (4, 6, 16)
squares = set(squaresTuple)
print(sorted(squares))

if squares.issubset(even):
    print("Squares is a subset of even")

if even.issuperset(squares):
    print("Even is a superset of squares")

even = frozenset(range(0, 100, 2))
print(even)
# even.add(3) # error - frozenset is immutable
