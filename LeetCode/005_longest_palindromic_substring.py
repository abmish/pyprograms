"""
url: https://leetcode.com/problems/longest-palindromic-substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):  # best solution on LeetCode : 68 ms
        """
        :type s: str
        :rtype: str
        """

        def is_palindrome(s):
            return True if s == s[::-1] else False

        if is_palindrome(s):
            return s

        max_len = 0
        start = 0
        str_len = len(s)
        for i in range(str_len):
            if i - max_len - 1 >= 0 and is_palindrome(s[i - max_len - 1: i + 1]):
                start = i - max_len - 1
                max_len = max_len + 2  # expanded assignment performs better than short hand increment
                continue

            if i - max_len >= 0 and is_palindrome(s[i - max_len: i + 1]):
                start = i - max_len
                max_len = max_len + 1
        return s[start: start + max_len]