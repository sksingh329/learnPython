import json

pvs_data = [{'pv_name':'/dev/sda1', 'vg_name':'cis', 'lv_name':'var_tmp', 'pv_size':'2147483648', 'pv_free':'0'}, {'pv_name':'/dev/sda2', 'vg_name':'data', 'lv_name':'home', 'pv_size':'19323158528', 'pv_free':'2680160256'}, {'pv_name':'/dev/sda2', 'vg_name':'data', 'lv_name':'var_log_audit', 'pv_size':'19323158528', 'pv_free':'2680160256'}, {'pv_name':'/dev/sda2', 'vg_name':'data', 'lv_name':'var_log', 'pv_size':'19323158528', 'pv_free':'2680160256'}, {'pv_name':'/dev/sdb4', 'vg_name':'rootvg', 'lv_name':'rootlv', 'pv_size':'67981279232', 'pv_free':'0'}, {'pv_name':'/dev/sdb4', 'vg_name':'rootvg', 'lv_name':'rootlv', 'pv_size':'67981279232', 'pv_free':'0'}]
temp_pvs_list = []

print(f"{pvs_data}")

for i in pvs_data:
    #res = json.loads(i)
    substring = str(i).split(',')
    search = ','.join(substring[:2])
    #is_found = all(str(item).startswith(search) for item in pvs_list) if pvs_list else False
    is_found = False
    for item in temp_pvs_list:
        if str(item).startswith(search):
            is_found = True
            break
    print(f"temp_pvs_list={temp_pvs_list} and substring={substring} and search={search} and isFound={is_found}")
    if not is_found:
        temp_pvs_list.append(i)

print(temp_pvs_list)




