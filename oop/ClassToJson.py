import json

class Student:
    def __init__(self, roll_no, name, batch):
        self.roll_no = roll_no
        self.name = name
        self.batch = batch

s1 = Student("85", "Swapnil", "IMT")
s2 = Student("124", "Akash", "IMT")

jsonstr1 = json.dumps(s1.__dict__)
jsonstr2 = json.dumps(s2.__dict__)

print(jsonstr1)
print(jsonstr2)