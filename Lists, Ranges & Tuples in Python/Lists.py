ipAddress = "127.0.0.1"
print(ipAddress.count("."))

parrotList = ["non pining", "no more", "a stiff", "bereft of live"]

parrotList.append("A Norwegian Blue")

for state in parrotList:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 7, 8]

numbers = even + odd
numbers.sort()
print(numbers)

Numbers = even + odd
NumbersInOrder = sorted(Numbers)
print(NumbersInOrder)

if numbers == Numbers:
    print("The lists are equal")
else:
    print("The lists are not equal")

if NumbersInOrder == sorted(Numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")

list1 = []
list2 = list()

print("List 1: {}".format(list1))
print("List 2: {}".format(list2))

if list1 == list2:
    print("The lists are equal")

print(list("The lists are equal"))

even = [2, 4, 6, 8]
anotherEven = list(even)

print(anotherEven is even)

anotherEven.sort(reverse=True)
print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even, odd]

for numberSet in numbers:
    print(numberSet)

    for value in numberSet:
        print(value)
