str = "Core Python"

i = 0
while( i < len(str)):
    #print(str[i])
    i += 1

i = -1
while( i >= -(len(str))):
    #print(str[i],end = ' ')
    i -= 1

for j in str:
    print(j,end = ' ' )

print()

for j in str[::-1]:
    print(j,end = ' ' )