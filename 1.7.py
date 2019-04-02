def replace(mat, m, n):
    row = set()
    col = set()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                col.add(i)
                row.add(j)
    
    for s in row:
        for i in range(m):
            mat[i][s] = 0
    
    for s in col:
        for j in range(n):
            mat[s][j] = 0

def printMat(matrix):
    for i in matrix:
        for j in i:
            print("%2s" % j, end=" ")
        print()


mat = [[0, 1, 2], [4, 5, 6], [1, 9, 10], [12, 1, 0]]
printMat(mat)
print()
replace(mat, 4, 3)
printMat(mat)
