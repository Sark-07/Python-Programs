n = int(input("Enter the term:\n"))
flag = 0
print("The prime numbers are:\n")
for i in range(0, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
