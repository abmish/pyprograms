"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate
values with original order reserved.
"""

def remove_duplicate_in_list(temp_list):
    olist = []
    for elem in temp_list:
        if elem not in olist:
            olist.append(elem)
    return olist

tlist = [12,24,35,24,88,120,155,88,120,155]
print remove_duplicate_in_list(tlist)
