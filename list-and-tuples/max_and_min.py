input = [100,50,10,80,3,60,5,1,200,50,40]

max = min = input[0]

for elem in input:
    if elem > max:
        max = elem
    if elem < min:
        min = elem

print(f"Max = {max} and Min = {min}")