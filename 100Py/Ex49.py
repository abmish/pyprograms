"""
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""

sq_nums = map(lambda e : e ** 2, range(1, 21))
print sq_nums