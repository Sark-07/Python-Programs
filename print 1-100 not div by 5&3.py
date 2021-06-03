a = int(input("Enter the term:\n"))
for i in range(0, a + 1, 1):
    if i % 5 == 0 or i % 3 == 0:
        continue
    print(i)
