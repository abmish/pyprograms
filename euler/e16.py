"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def sum_of_digits(num):
    total = 0
    while num >= 1:
        total = total + num%10
        num = num/10
    return total

print sum_of_digits(pow(2, 1000))