def mygen(x,y):
    while x <= y:
        yield x
        x += 1

g = list(mygen(5,10))

for i in g:
    print(i)