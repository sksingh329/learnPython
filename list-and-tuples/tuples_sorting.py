tup = (5,40,100,20,0,13,7,1)

print(f"Tuple: {tup} and After sorting: {sorted(tup)}")
print(tup)

emp = ((5,"Emp1",100),(1,"Emp2",1000),(4,"Emp3",500),(3,"Emp4",50),(2,"Emp5",800))

print(sorted(emp))
print(sorted(emp, key=lambda x:x[1]))