from numpy import *

n = int(input("Enter the rows of the first matrix:\n"))
m = int(input("Enter the col of the first matrix:\n"))
matrix1 = [[0] * m for i in range(n)]
print("Enter the values:\n")
for i in range(n):
    for j in range(m):
        matrix1[i][j] = int(input())

p = int(input("Enter the rows of the second matrix:\n"))
q = int(input("Enter the col of the second matrix:\n"))
matrix2 = [[0] * q for i in range(p)]
print("Enter the values:\n")
for i in range(p):
    for j in range(q):
        matrix2[i][j] = int(input())

print("The first matrix is:-")
for i in range(n):
    for j in range(m):
        print(matrix1[i][j], end=" ")
    print()
print("The second matrix is:-")
for i in range(p):
    for j in range(q):
        print(matrix2[i][j], end=" ")
    print()

# multiplication part
if n != q:
    print("Multiplication can not possible!!")
else:
    mul = [[0] * q for i in range(p)]
    for i in range(n):
        for j in range(q):
            for k in range(m):
                mul[i][j] += matrix1[i][k] * matrix2[k][j]
    print("The multiplication is:-")
    for i in range(n):
        for j in range(q):
            print(mul[i][j], end=" ")
        print()
# matrix1 = asmatrix(matrix1)
# matrix2 = asmatrix(matrix2)
# print(matrix1 * matrix2)