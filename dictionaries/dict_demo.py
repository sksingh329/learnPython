
employee_dict = {'name':'Subodh','id':100,'salary':1000}

print(f"Employee Details\nName: {employee_dict['name']}, Id: {employee_dict['id']}, Salary: {employee_dict['salary']}")

employee_dict['salary'] = 1500
employee_dict['dept'] = 'it'

print(f"Employee Details\nName: {employee_dict['name']}, Id: {employee_dict['id']}, Salary: {employee_dict['salary']}, Dept: {employee_dict['dept']}")

#Check if key exist or not
print(f"{'gender' in employee_dict}")