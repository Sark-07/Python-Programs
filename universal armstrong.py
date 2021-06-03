from math import *

n = int(input("Enter the number:\n"))
rem = 0
rem2 = 0
sum = 0
count = 0
m = p = n
while n != 0:
    rem = n % 10
    count += 1
    n = floor(n / 10)
while p != 0:
    rem2 = p % 10
    sum += pow(rem2, count)
    p = floor(p / 10)
if sum == m:
    print("The number is a armstrong number!!")
else:
    print("The number is not a armstrong number!!")
