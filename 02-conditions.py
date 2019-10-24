#!/usr/bin/python3.7

# Largest number
# x = int(input("enter x: "))
# y = int(input("enter y: "))
# z = int(input("enter z: "))
#
# print (x, y, z)
#
# if x > y > z:
#     print(x)
# elif y > z:
#     print(y)
# else:
#     print(z)

# Assign biggest number to first var
# x = int(input("enter x: "))
# y = int(input("enter y: "))
#
# if x < y:
#     t = x
#     x = y
#     y = t
#     print(x, y)
# else:
#     print(x, y)

# Which century
# year = int(input("enter year: "))
# c = (year // 100) + 1
# print(c)

# Arithmetic progression
# progress = True
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# c = int(input("enter c: "))
# if ((a + c) * 3 / 2 == a + b + c):
# # if (a + b == 2 * c):
#     progress = True
# else:
#     progress = False
# print(progress)

# Leap year
leap = True
year = int(input("enter year: "))
if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    leap = True
else:
    leap = False
print(leap)
