"""
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""

even_nums = filter(lambda e : e%2 == 0, range(1,21))
print even_nums