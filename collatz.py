#!/usr/bin/env python3


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    elif number % 2 == 1:
        number = 3 * number + 1
        return number


print("Enter number:")
try:
    num = int(input())
except ValueError:
    print("Input must be an integer")

while collatz(num) != 1:
    num = collatz(num)
    print(num)
