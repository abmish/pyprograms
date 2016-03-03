"""
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even,
otherwise print "It is an odd number".
"""

def even_or_odd(num):
    if num%2 == 0:
        print "%d is even number" % num
    else:
        print "%d is odd number" % num

even_or_odd(8)
even_or_odd(9)