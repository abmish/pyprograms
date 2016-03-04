"""
Please write a program to count and print the number of times each character occurs in a string input by console.
"""

odict = {}
user_in = raw_input("Input a string sequence :")
for char in user_in:
    odict[char] = odict.get(char, 0)+1
print "\n".join(["%s : %s" % (key, val) for key, val in odict.items()])
