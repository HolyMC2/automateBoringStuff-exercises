#!/usr/bin/env python3


def is_phone_number(text):
    """
    Function to test if the string if a phone number
    """
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 1):
        if not text[i].isdecimal():
            return False
    return True


print("415-555-4242 is a phone number:")
print(is_phone_number("415-555-4242"))
print("Moshi moshi is a phone number:")
print(is_phone_number("Moshi moshi"))

a = [
    "bill",
    "samantha",
    "ray",
    "ronald",
    "mo",
    "harry",
    "susan",
    "ted",
    "timothy",
    "bob",
    "wolverine",
    "cat",
    "lion",
    "alfred",
    "batman",
    "linus",
]

print(a)
