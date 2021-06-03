def selection_sort(a, n):
    j = 0
    for i in range(n):
        min = i
        for j in range(i, n):
            if a[j] < a[min]:
                min = j

        if i != j:
            temp = a[i]
            a[i] = a[min]
            a[min] = temp


a = []
n = int(input("Enter the size of the array:\n"))
print("Enter the values of the array:\n")
for k in range(n):
    val = int(input())
    a.append(val)
selection_sort(a, n)
print(a)
