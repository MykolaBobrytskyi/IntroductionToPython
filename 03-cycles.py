#!/usr/bin/python3.7

# целые числа от a до b
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# while (a < b):
#     print(a)
#     a += 1

# четные числа от a до b
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# while (a < b):
#     a += 1
#     if (a % 2 == 0):
#         print(a)

# четные числа обратно от a до b
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# while (a < b):
#     b -= 1
#     if (b % 2 == 0):
#         print(b)
# # while a < b:
# #     b -= 1
# #     if b == 6:
# #         continue
# #     print(b)

# Вводить слова с клавиатуры и составлять из них предложение,
# пока не будет введена точка.
# Составленное предложение напечатать.
# sentence = ''
# while True:
#     word = input("next word: ")
#     sentence += ' ' + word
#     if word == '.':
#         break
# print(sentence)

# odd numbers factorial
# n = int(input("enter n: "))
# factorial = 1
# for i in range(1, n+1, 2):
#     factorial *= i
# print(factorial)

# summa stepeney dvoyki ot 0 ot n
# n = int(input("enter n: "))
# sum = 2 ** (n + 1) - 1
# print(sum)

# summa deliteley
m = int(input("enter m: "))
d = 0
for i in range(1, m+1):
    if m % i == 0:
        d += i
print(d)
