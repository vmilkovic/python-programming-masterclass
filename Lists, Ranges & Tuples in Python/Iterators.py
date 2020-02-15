string = "1234567890"

for char in string:
    print(char)

myIterator = iter(string)
print(myIterator)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

for char in string:
    print(char)

for char in iter(string):
    print(char)
