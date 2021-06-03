from numpy import *

a = []
b = []
c = []

n = int(input("Enter the size of the first array:\n"))
print("Enter the elements of the first array:\n")
for i in range(n):
    val = int(input())
    a.append(val)
    c.append(a[i])
m = int(input("Enter the size of the second array:\n"))
print("Enter the elements of the second array:\n")
for j in range(m):
    val1 = int(input())
    b.append(val1)
    c.append(b[j])

for i in c:
    print(i)
