#Square of numbers in a list
input = [1,2,3,4,5]

square = []

for i in input:
    square.append(i*i)

print(square)

square1 = [ i*i for i in input]
print(square1)

even_squares = [ i*i for i in range(11) if i %2 == 0]
print(even_squares)