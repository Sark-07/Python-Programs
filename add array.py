from array import *

arr1 = array('i', [])
arr2 = array('i', [])
arr = array('i', [])
n = int(input("Enter the size of the first array:\n"))
print("Enter the elements of the first array:\n")
for i in range(n):
    val1 = int(input())
    arr1.append(val1)
m = int(input("Enter the size nof the second array:\n"))
print("Enter the elements of the second array:\n")
for j in range(m):
    val2 = int(input())
    arr2.append(val2)
if n == m:
    p = n
    for i in range(p):
        arr.append(arr1[i] + arr2[i])
    print("The addition of two arrays is:\n")
    for k in arr:
        print(k)
else:
    print("The size of the both arrays should be same!!")
