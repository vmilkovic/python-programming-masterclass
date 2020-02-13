# Write a small program to ask for a name and age.
# When both values have been entered, check if the person
# is the right age to go on a 18-30 holiday (they must be over 18 and under 31)
# If they are, welcome them to the holiday, otherwise print a (polite) message refusing them entry.

name = input("What is your name? ")
age = int(input("What is your age {}? ".format(name)))

if 18 <= age < 30:
    print("Welcome to your 18-30 holiday {}!".format(name))
else:
    print("Your age is not in 18-30 range!")
