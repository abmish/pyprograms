"""
The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. The ten numbers not exceeding 100 having exactly eight
divisors are 24, 30, 40, 42, 54, 56, 66, 70, 78 and 88. Let f(n) be the count of numbers not exceeding n with exactly
eight divisors.
You are given f(100) = 10, f(1000) = 180 and f(10^6) = 224427.
Find f(10^12).
"""

###### DRAFT not working yet ######

from collections import defaultdict
def are_8_divisors(num, limit=8):
    divisors = set()
    i = 1
    lim = num/2
    while i < lim:
        if num%i==0:
            divisors.add(i)
            n_lim = num/i
            divisors.add(n_lim)
            lim = n_lim
            if len(divisors)>8:
                return False
        i += 1
    if len(divisors)==8:
        return True
    return False

"""
max_num = 10**6
count = 0
for i in range(max_num+1):
    if are_8_divisors(i):
        count += 1

print count
"""

def is_prime(num):
    for i in range(2, num/2+1):
        if num%i==0:
            return False
    return True

def get_prime_factors(num):
    lim = num
    ddict = defaultdict()
    i = 2
    while not is_prime(lim) and i<=lim:
        while lim%i==0:
            n_lim = num/i
            ddict[i] += 1
            lim = n_lim
        i += 1
    return ddict

print get_prime_factors(60)