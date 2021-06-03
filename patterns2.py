st = [1, 2, 3, 4]
for i in range(0, len(st)):
    for j in range(0, i+1):
        print(st[j], end="")
    print("\n")
