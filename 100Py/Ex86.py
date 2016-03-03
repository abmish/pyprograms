"""
By using list comprehension, please write a program to print the list after removing  numbers which are divisible
by 5 and 7 in [12,24,35,70,88,120,155]
"""

tlist = [12,24,35,70,88,120,155]
print [num for num in tlist if num%5 == 0 and num%7 == 0]