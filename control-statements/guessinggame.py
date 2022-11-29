import random

highest = 10
answer = random.randint(1,10)

value = int(input("Please guess number between 1 and 10:"))

while True:
    if value == 0:
        print("Quitting Game!")
        break
    elif value == answer:
        print("Your guess is right")
        break
    elif value > answer:
        value = int(input("Please enter lower number:"))
    else:
        value = int(input("Please enter higher number:"))