squares = [ x**2 for x in range(1,11) if x % 2 == 0]

#print(squares)

x = list(range(1,5))
print(x)

y = x # Here y is the alias of x, any modification done to 'x'  will also modify 'y' and vice versa.
z = x[:] #Getting a copy of of an existing object is cloning
y[1] = 10

print(y) #[1, 10, 3, 4]
print(x) #[1, 10, 3, 4]
print(z) #[1, 2, 3, 4]
