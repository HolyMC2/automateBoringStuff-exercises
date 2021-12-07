#!/usr/bin/env python3


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid]
        print("low is :" + str(low))
        print("high is :" + str(high))
        print("mid is :" + str(mid))
        print("guess is :" + str(guess))
        print("\n")
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
# print(binary_search(my_list, 9))
