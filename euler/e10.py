"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

primes = [True] * 2000000

def check_prime(primes, num):
    for count in xrange(num + num, len(primes), num):
        primes[count] = False

for num in xrange(2, int(len(primes)/2)+1):
    if primes[num] : check_prime(primes, num)

print sum(num for num in xrange(2, len(primes)) if primes[num])