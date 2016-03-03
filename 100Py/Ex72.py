"""
Please write a binary search function which searches an item in a sorted list. The function should return the index of
element to be searched in the list.
"""

import math
def binary_search(tlist, element):
    start = 0
    end = len(tlist) - 1
    index = -1
    while end >= start and index == -1:
        mid = int(math.floor((start+end)/2.0))
        if tlist[mid] == element:
            index = mid
        elif tlist[mid] > element:
            end = mid - 1
        else:
            start = mid + 1
    return index

user_list = [3,9,14,88,122,177]
print binary_search(user_list, 14)
print binary_search(user_list, 15)