input = [1,5,3,4,2]

for i in range(len(input)):
    for j in range(i+1,len(input)):
        if input[i] > input[j]:
            temp = input[j]
            input[j] = input[i]
            input[i] = temp


print(input)