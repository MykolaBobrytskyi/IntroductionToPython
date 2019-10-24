#!/usr/bin/python3.7

# average function
# m = int(input("enter m: "))
# n = int(input("enter n: "))
#
# def avg(a, b):
#     avg = (a + b) / 2
#     return(avg)
#
# x = avg(m, n)
# print(x)

# Largest number
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# c = int(input("enter c: "))
#
# def max(x, y, z):
#     if x > y > z:
#         return(x)
#     elif y > z:
#         return(y)
#     else:
#         return(z)
#
# x = max(a, b, c)
# print(x)

# Largest number
a = int(input("enter a: "))
b = int(input("enter b: "))

def max(x, y, z):
    if x > y > z:
        return(x)
    elif y > z:
        return(y)
    else:
        return(z)

x = max(a, b, c)
print(x)
