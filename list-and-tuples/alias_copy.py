x = [10,20,30,40,50]

#Alias
y = x

x[1] = 99

print(x)
print(y)

#Copy
y = x[:]
x[1] = 100

print(x)
print(y)