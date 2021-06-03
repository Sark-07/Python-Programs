from array import *

arr = array('i', [])
n = int(input("Enter the size:\n"))
print("Enter the elements:\n")
for i in range(n):
    val = int(input())
    arr.append(val)
maxx = arr[0]
for i in range(n):
    if arr[i] > maxx:
        maxx = arr[i]
print("The maximum value of the array is=>")
print(maxx)
