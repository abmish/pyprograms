"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
Find the largest palindrome made from the product of two 3-digit numbers
"""
num = 0
for a in xrange(999, 100, -1):
    for b in xrange(a, 100, -1):
        prod = a * b
        if prod > num:
            pal = str(prod)
            if pal == pal[::-1]:
                num = prod

print num