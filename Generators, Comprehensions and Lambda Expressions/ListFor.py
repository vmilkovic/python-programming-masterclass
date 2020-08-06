print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number, and I'll tell you its square: "))

squares = []
for number in numbers:
    squares.append(number ** 2)

index_pos = numbers.index(number)  # number is always 6 bcs number is in for loop as 5 index (python2 bug)
print(squares[index_pos])
print(squares)
