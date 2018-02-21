"""
url: https://leetcode.com/problems/reverse-integer/description/
help: https://stackoverflow.com/questions/44581339/reverse-32bit-integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x

        if -10 < x < 10:
            return x

        str_x = str(x)
        n_limit = -0x80000000
        p_limit = 0x7fffffff

        if x < 0:
            str_x = '-' + str_x[::-1][:-1]
            nx = int(str_x)
            return nx if (nx & n_limit == n_limit) else 0

        if x > 0:
            str_x = str_x[::-1]
            nx = int(str_x)
            return nx if (nx & p_limit == nx) else 0
