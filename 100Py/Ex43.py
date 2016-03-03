"""
Write a program to generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10)
"""

this_tuple = (1,2,3,4,5,6,7,8,9,10)
tlist = list()
for elem in this_tuple:
    if elem%2 == 0:
        tlist.append(elem)

print tuple(tlist)