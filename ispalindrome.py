#!/usr/bin/env python3


get_input = str(input("Provide u r string:"))


def ispalindrome(s):

    print(f'will check string {s} is plaindrome or not')
    
    rev_str = ""

    for char in s:

        rev_str = char + rev_str

    return rev_str


new_str = ispalindrome(get_input)
print(new_str)

if get_input  == new_str:

    print(f"{new_str} is plaindrome of {get_input}")

else:
    print("Not a Palindrome")


