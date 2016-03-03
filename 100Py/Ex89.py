"""
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in
[12,24,35,70,88,120,155].
"""

tlist = [12,24,35,70,88,120,155]
print [num for (counter, num) in enumerate(tlist) if counter not in (0,4,5)]