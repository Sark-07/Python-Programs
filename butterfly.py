n = int(input("Enter the rows:\n"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
        for k in range(2 * n + 1):
            p = 2 * n
            while p <= k:
                print("*", end=" ")
                p -= 1
    print("\n")