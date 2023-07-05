
colors = {"b":"blue","r":"red","w":"white","g":"green"}

#Display keys
for k in colors:
    print(k)

#Display values
for k in colors:
    print(colors[k])

#Display key and values
for k,v in colors.items():
    print(f"Key= {k} and value= {v}")