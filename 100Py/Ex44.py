"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise
print "No".
"""

input_str = raw_input("input yes variation:")
if input_str=="yes" or input_str=="YES" or input_str=="Yes":
    print "Yes"
else:
    print "No"
