"""
Define a function that can convert a integer into a string and print it in console.
"""

def print_as_str(num):
    print str(num)

user_in = raw_input("Input a number")
print_as_str(int(user_in))