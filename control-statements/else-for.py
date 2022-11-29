numbers = [1,45,32,10,60]

for num in numbers:
    if num % 8 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("All numbers are fine")