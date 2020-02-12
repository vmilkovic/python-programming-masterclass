# greeting = "Hello"
# name = input("Please enter your name: ")
# print(greeting + ' ' + name)

# splitString = "This string has been\nsplit over\nseveral\nlines"
# print(splitString)
#
# tabbedString = "1\t2\t3\t4\t5"
# print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting"')
print("The pet shop owner said \"No, no, 'e's uh,...he\'s resting\"")

anotherSplitString = """This string has been
split over
several lines"""

print(anotherSplitString)

print('''The pet shop owner said "No, no, 'es' uh,...he's resting''')
print("""The pet shop owner said "No, no, 'es' uh,...he's resting""")

parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(number[0::3])

string1 = "he's"
string2 = "probably"
print(string1 + string2)
print("he's" " probably " "pining")
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")
