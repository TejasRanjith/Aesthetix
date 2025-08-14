def butterfly(n):
    size=2*n-1
    matrix=[[' 'for _ in range(size)] for _ in range(size)]
    for i in range(n):
        for j in range(i+1):
            matrix[i][j] = '*'
            matrix[i][size-j-1] = '*'
    for i in range(n,size):
        for j in range(size-i):
            matrix[i][j] = '*'
            matrix[i][size-j-1] = '*'
    for row in matrix:
        for elem in row:
            print(elem,end="")
        print()


butterfly(3)
