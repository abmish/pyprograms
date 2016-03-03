"""
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""

tlist = [1,2,3,4,5,6,7,8,9,10]
sq_nums = map(lambda elem: elem ** 2, tlist)
print sq_nums