def bubble_sort(a, n):
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

        print(a)


a = []
n = int(input("Enter the size of the array:\n"))
print("Enter the values of the array:\n")
for k in range(n):
    val = int(input())
    a.append(val)
bubble_sort(a, n)
print(a)
