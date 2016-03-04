"""
Ask the user for a string and print out whether this string is a palindrome or not.
"""

user_in = raw_input("Input a string to check palindrome :")
rev_string = user_in[::-1]
if user_in == rev_string:
    print "palindrome"
else:
    print "not palindrome"