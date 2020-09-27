'''
Challenge: Write a python function to determine if a given string is a palindrome
Input: String to evaluate
Output: Boolean Value

Constraints: Consider only letters
Ignore case (For example 'A == 'a')
'''

import re

def is_StringPalindrome(s):
    forward = ''.join(re.findall(r'[a-z]+', s.lower()))
    backward = forward[::-1]
    return forward == backward


def main():
    test = raw_input("Enter a string you want to test for bieng palindrom: ")
    print("The test string is {0} Is a palindrom: {1}".format(test, is_StringPalindrome(test)))


main()