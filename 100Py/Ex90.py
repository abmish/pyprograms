"""
By using list comprehension, please write a program to print the list after removing the value 24 in
[12,24,35,24,88,120,155].
"""

tlist = [12,24,35,24,88,120,155]
print [num for num in tlist if num != 24]