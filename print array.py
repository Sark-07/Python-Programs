from array import *

arr = array('i', [])
n = int(input("enter the size of the array:\n"))
print("Enter the elements:\n")
for i in range(n):
    val = int(input())
    arr.append(val)
arr1 = array(arr.typecode, (j for j in arr))
print("The new array is:\n")
for k in range(len(arr1)):
    print(arr1[k])

# arr = array('i', [])
# n = int(input("enter the size of the array:\n"))
# print("Enter the elements:\n")
# for i in range(n):
#     val = int(input())
#     arr.append(val)
# for i in range(n):
#     print(arr[i])
"""from numpy import *
arr = array([])
n = int(input("Enter the number of values you want:  "))

for i in range(n):
    v = input("Element:  ")
    arr = append(arr, v)
print(arr)"""