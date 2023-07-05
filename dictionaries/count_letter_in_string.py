dict = {}
search = "Book"

for x in search:
    dict[x] = dict.get(x,0)+ 1

print(dict)