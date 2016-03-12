"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def gcd(num1, num2):
    return num2 and gcd(num2, num1 % num2) or num1

def lcm(num1, num2):
    return num1 * num2/ gcd(num1, num2)

num = 1
for count in xrange(1, 21):
    num = lcm(num, count)

print num