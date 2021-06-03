# def factor(x):
#     fact = 1
#     for i in range(1, x + 1):
#         fact = fact * i
#     return fact
#
#
# n = int(input("Enter the number:\n"))
# factor(n)
# print("The factorial of {} is=>".format(n), factor(n))
factorial = lambda f=int(input("Enter the number:\n")): 1 if f == 0 else f * factorial(f - 1)
print(factorial())
