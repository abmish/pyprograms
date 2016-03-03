"""
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
"""

in_str = raw_input("Input a string :")
uni_str = unicode( in_str ,"utf-8")
print uni_str