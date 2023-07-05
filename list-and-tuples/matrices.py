mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

#Print matrices
print(mat)

#Print row by row
for r in mat:
    print(r)

#Print all element
for row in mat:
    for col in row:
        print(col,end=' ')

    print()

#Print all element
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j],end=' ')

    print()