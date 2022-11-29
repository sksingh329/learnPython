name = "subodh singh"

for char in name:
    #print(char)
    pass

number = "9,252;953:123 987;874"
seperator = ''

for char in number:
    if not char.isnumeric():
        seperator = seperator + char

#print(seperator)


for i in range(5):
    print(f'value of is is {i}')