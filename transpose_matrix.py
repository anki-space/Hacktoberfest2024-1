#Program to find transpose of a matrix


def transpose(A, B):
    for i in range(N):
        for j in range(N):
            B[i][j] = A[j][i]

# Order of Matrix
N = 4

A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]

# To store result
B = [[0 for x in range(N)] for y in range(N)]

# Function call
transpose(A, B)

print("Result matrix is")
for i in range(N):
    for j in range(N):
        print(B[i][j], " ", end='')
    print()
