import array as ar

marks = ar.array('i',[10,20,30,40,50,60,70,80,90,100])
print(marks)

copy_marks = ar.array(marks.typecode, (a*2 for a in marks))

y = marks[0:]
print(y)
y.insert(3,0)
y.reverse()
print(y)
print(y.itemsize)