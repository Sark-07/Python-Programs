from numpy import *

a = array([])
row1 = int(input("Enter the rows:\n"))
col1 = int(input("Enter the col:\n"))
print("Enter the values:\n")
for i in range(row1 * col1):
    val = int(input())
    a = append(a, val)
a = a.reshape(row1, col1)
a = asmatrix(a)
print(a)
"""import numpy as np

# Taking the number of rows and columns from user

n = int(input("Enter the number of Rows\n"))
m = int(input("Enter the number of Columns\n"))


 #You can either use this loop method for below list comprehension;

#a=[]
#for i in range(n):
   # a.append([0] * m )


# Creating a Empty matrix as as per the instruction of user;

a = [[0] * m for i in range(n)]

# Taking the element for a matrix from user;

for i in range(n):
    for j in range(m):
        print("Enter Element No:", i, j)
        a[i][j] = int(input())
print(np.asmatrix(a))"""
