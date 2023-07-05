tup = (10,20,30)
print(tup[2])

tup5 = 1,2,3,4,5 # this is a tuple
print(tup5)

tup1 = 10,2,3,11,15,1,1,20,1
print(min(tup1))
print(tup1.count(1))

#Search Element in tuple
search = 200


try:
        pos = tup1.index(search)
        print(f"Element {search} is found at: {pos+1}")
except:
        print(f"Element {search} not found in tuple {tup1}")