from math import *
n = int(input("Enter the number:\n"))
rem = 0
sum = 0
m = n
while n != 0:
    rem = n % 10
    sum += pow(rem, 3)
    n = floor(n/10)
if sum == m:
    print("The number is a armstrong number!!")
else:
    print("The number is not a armstrong number!!")
