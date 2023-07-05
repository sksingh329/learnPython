pv_name_vg_name_dict = {'sdd':['vg_data-lv_data_1','vg_data-lv_data_2'],'sde':['vg_data-lv_data_1']}

key = 'sde'
item = 'vg_data-lv_data_2'

if key in pv_name_vg_name_dict and item in pv_name_vg_name_dict[key]:
    print(f"The dictionary already has the item '{item}' for key '{key}'.")
else:
    print(f"The dictionary does not have the item '{item}' for key '{key}'.")