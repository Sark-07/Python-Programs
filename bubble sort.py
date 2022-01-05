def bubble_sort(a, n):
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

    return a



n = int(input("Enter the size of the array:\n"))
if n > 0:
    a = []
    for k in range(n):
        val = int(input(f"Enter the value of position {k} of the array: "))
        a.append(val)
    print(bubble_sort(a, n))
else: print('Please enter a positive integer.')
