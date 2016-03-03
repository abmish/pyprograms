"""
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some
books. But Python has a built-in document function for every built-in functions. Please write a program to print some
Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
"""

print abs.__doc__
print int.__doc__
print raw_input.__doc__

def square(num):
    '''
    Return the square value of the input int
    :param num: integer
    :return: integer, square of num
    '''
    return num ** 2

user_in = int(raw_input("Input an integer :"))
print square(user_in)
print square.__doc__
