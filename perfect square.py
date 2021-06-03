a = int(input("Enter the term:\n"))
print("The perfect square nos are:\n")
for i in range(0, a + 1):
    b = i * i
    if b > 100:
        break
    print(b)
