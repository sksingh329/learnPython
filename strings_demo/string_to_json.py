import json

with open('input', 'r') as file:
    # Read the contents of the file into a string
    input = file.read()
lvs_data = []
#print(input)
parse = input.split("***LVS***")[1].rstrip().lstrip()
lvs_data_json = '['+parse+']'
print(lvs_data_json)
data = json.loads(lvs_data_json)

lvm_vg_dict = {}
for item in data:
    lvm_name = item['lv_name']
    vg_name = item['vg_name']

    lvm_vg_dict[lvm_name] = vg_name

print(lvm_vg_dict)