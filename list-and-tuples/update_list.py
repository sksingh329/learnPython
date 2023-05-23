lst = list(range(5))
print(f"Before: {lst}")

lst.append(10)
print(f"After append: {lst}")

lst[1:3] = 11,12
print(f"After update: {lst}")

#del lst[1]
#print(f"After delete: {lst}")

lst.append(4)
print(f"Before remove: {lst}")

lst.remove(4)
print(f"After remove: {lst}")