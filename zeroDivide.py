#!/usr/bin/env python3


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")


def spam2(divideBy):
    return 42 / divideBy


try:
    print(spam2(2))
    print(spam2(12))
    print(spam2(0))
    print(spam2(1))  # this is never executed, because once the execution
except ZeroDivisionError:  # jumps to the except clouse, it does not return to the try clause
    print("Error: Invalid argument.")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
