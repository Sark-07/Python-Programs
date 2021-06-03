st = 'ABCD'
st1 = "PQR"
for i in range(len(st)):
    for j in range(i + 1):
        print(st[j], end="")
    for k in range(i, len(st1)):
        print(st1[k], end="")
    print("\n")
# for i in range(0, len(st)):
#     for j in range(len(st)):
#         if i < j:
#             print(chr(65+14+j), end="")
#         else:
#             print(chr(65+j), end="")
#     print("\n")
