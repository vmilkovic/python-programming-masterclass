import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = 0

while not guess == answer:

    guess = int(input())

    if guess == 0:
        break;

    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it")
