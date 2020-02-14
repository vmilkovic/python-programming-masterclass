i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

availableExits = ["east", "north east", "south"]
choseExit = ""

while choseExit not in availableExits:
    choseExit = input("Please chose a direction: ")
    if choseExit == "quit":
        print("Game Over")
        break
else:
    print("Aren't you glad you got out of there!")
