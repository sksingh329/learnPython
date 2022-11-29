answer = 5

response = int(input("Enter your guess: "))

if response < answer:
    print("Guess high number")
elif response > answer:
    print("Guess low number")
else:
    print("Your guess is correct")