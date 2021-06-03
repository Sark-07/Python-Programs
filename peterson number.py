n = int(input("Enter the number:\n"))
rem = 0
m = n
sum1 = 0
while n != 0:
    rem = n % 10
    factr = 1
    for i in range(1, rem + 1):
        factr *= i
    sum1 += factr
    n //= 10
if sum1 == m:
    print("The number {} is a peterson number!!".format(m))
else:
    print("The number {} is not a peterson number!!".format(m))
