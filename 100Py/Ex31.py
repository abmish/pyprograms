"""
Define a function that can accept two strings as input and print the string with maximum length in console. If two
strings have the same length, then the function should print all strings line by line.
"""

def print_longer_string(str1, str2):
    str_len1 = len(str1)
    str_len2 = len(str2)

    if str_len1 > str_len2:
        print str1
    elif str_len1 < str_len2:
        print str2
    else:
        print str1
        print str2

print_longer_string("one", "two")
print_longer_string("two", "three")
print_longer_string("three", "four")