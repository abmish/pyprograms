"""
Optimisation:
Access Time
dict = 0
generators > list
function > array > local var
"""

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]   # Ensure that this is initialised with at least 1 prime
prime_dict = dict.fromkeys(prime_list, 1)
last_n = prime_list[-1]

def _isprime(n):
    """
    Raw check to see if n is prime. Assumes that prime_list is already populated
    """
    isprime = n >= 2 and 1 or 0
    for prime in prime_list:                    # Check for factors with all primes
        if prime * prime > n : break             # ... up to sqrt(n)
        if not n % prime:
            isprime = 0
            break
    if isprime : prime_dict[n] = 1               # Maintain a dictionary for fast lookup
    return isprime

def _refresh(x):
    """
    Refreshes primes up to x
    """
    global last_n
    while last_n <= x:                           # Keep working until we've got up to x
        last_n = last_n + 1                      # Check the next number
        if _isprime(last_n):
            prime_list.append(last_n)            # Maintain a list for sequential access

def prime(x):
    """
    Returns the xth prime
    """
    global last_n
    while len(prime_list) <= x:                 # Keep working until we've got the xth prime
        last_n = last_n + 1                     # Check the next number
        if _isprime(last_n):
            prime_list.append(last_n)            # Maintain a list for sequential access
    return prime_list[x]

def isprime(x):
    """
    Returns 1 if x is prime, 0 if not. Uses a pre-computed dictionary '''
    """
    _refresh(x)                                 # Compute primes up to x (which is a bit wasteful)
    return prime_dict.get(x, 0)                 # Check if x is in the list

def factors(n):
    """
    Returns a prime factors of n as a list
    """
    _refresh(n)
    x, xp, f = 0, prime_list[0], []
    while xp <= n:
        if not n % xp:
            f.append(xp)
            n = n / xp
        else:
            x = x + 1
            xp = prime_list[x]
    return f

def all_factors(n):
   """
   Returns all factors of n, including 1 and n
   """
   f = factors(n)
   elts = sorted(set(f))
   numelts = len(elts)
   def gen_inner(i):
       if i >= numelts:
           yield 1
           return
       thiselt = elts[i]
       thismax = f.count(thiselt)
       powers = [1]
       for j in xrange(thismax):
           powers.append(powers[-1] * thiselt)
       for d in gen_inner(i+1):
           for prime_power in powers:
               yield prime_power * d
   for d in gen_inner(0):
       yield d

def num_factors(n):
    """
    param n:
    return: number of factors of n, including 1 and n
    """
    div = 1
    x = 0
    while n > 1:
        c = 1
        while not n % prime(x):
            c = c + 1
            n = n / prime(x)
        x = x + 1
        div = div * c
    return div