
input = list(range(5))

print(f"Input List: {input}")

reverse = []

i= -1
while( i >= -len(input)):
    reverse.append(input[i])
    i = i - 1

print(f"Reverse List: {reverse}")