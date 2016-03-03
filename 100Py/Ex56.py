"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def raise_an_error():
    return 5/0

try:
    raise_an_error()
except ZeroDivisionError:
    print "dividing by zero"
except Exception, err:
    print "Catching an exception"
finally:
    print "Finally gets executed all the time"