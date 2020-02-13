parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give ma an {}, Vedran".format(letter))
else:
    print("I don't need that letter")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give ma an {}, Vedran".format(letter))
