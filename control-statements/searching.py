shopping_list = ["iphone","ipad","monitor","garmin"]

item_to_find = "cycle"
found_at = None

print(type(found_at))

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at:
    print(f'Item is found at position {found_at}')
else:
    print(f'Item not found')