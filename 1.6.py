def rotate(m):
    n = len(m)
    for x in range(n // 2):
        for y in range(x, n - x - 1):
            top = m[x][y]
            m[x][y] = m[y][n - 1 - x]
            m[y][n - 1 - x] = m[n - 1 - x][n - 1 - y]
            m[n - 1 - x][n - 1 - y] = m[n - 1 - y][x]
            m[n - 1 - y][x] = top


def printMat(matrix):
    for i in matrix:
        for j in i:
            print("%2s" % j, end=" ")
        print()


mat = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
printMat(mat)
print()
rotate(mat)
printMat(mat)
