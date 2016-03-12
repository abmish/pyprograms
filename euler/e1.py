"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

total = 0
for count in xrange(1, 1000):
    if not count%5 or not count%3:
        total += count

print total