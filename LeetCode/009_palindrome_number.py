"""
url: https://leetcode.com/problems/palindrome-number

Determine whether an integer is a palindrome. Do this without extra space.

"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    num = str(x)
    return True if num == num[::-1] else False
