from array import *

arr = array('i', [])
n = int(input("Enter the size:\n"))
print("Enter the elements:\n")
for i in range(n):
    val = int(input())
    arr.append(val)
a = sorted(arr)
print("The sorted array is:\n")
for i in a:
    print(i)
