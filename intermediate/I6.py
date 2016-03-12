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
            #print '%d not prime' % num
            return False
    #print '%d prime' % num
    return True

def inc_prod(lst):
    prod = 1
    for each in lst:
        prod = prod * (each +1)
    return prod

def get_prime_factors(num):
    lim = n_lim = num
    ddict = defaultdict(int)
    i = 2
    while not is_prime(n_lim) and i<=n_lim and inc_prod(ddict.values())<=8:
        while n_lim%i==0:
            n_lim = n_lim/i
            #print 'n_lim %d' % n_lim
            ddict[i] = ddict[i]+1
            lim = n_lim
        i += 1
    if n_lim >= 2:
        ddict[n_lim] += 1

    if inc_prod(ddict.values())==8:
        return True
    return False

max_num = 100000
count = 0
for i in range(max_num+1):
    if get_prime_factors(i):
        count += 1

print count

#10,0
#100,10
#1000,180
#10000,2114
#100000,