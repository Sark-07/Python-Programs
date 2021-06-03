a = []
count = 0
n = int(input("Enter how many names you want to enter:\n"))
print("Enter the values:\n")
for i in range(n):
    val = input()
    a.append(val)
for i in a:
    if len(i) == 5:
        count += 1
print("The numbers of names which have 5 letters is=> ", count, "and the names are:-")
for i in a:
    if len(i) == 5:
        count += 1
        print(i, "= 5")
