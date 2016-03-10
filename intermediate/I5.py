"""
PALPRIM - Palindromic Primes
A Palindromic number is a number without leading zeros that remains the same when its digits are reversed. For instance
5, 22, 12321, 101101 are Palindromic numbers where as 10, 34, 566, 123421 are not. A Prime number is a positive integer
greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 31, 97 are Prime numbers but 1, 10,
25, 119 are not. A Palindromic Prime number is both palindromic and prime at the same time. 2, 3, 131 are Palindromic
Prime numbers but 6, 17, 3333 are not. Given a positive integer N, output the largest palindromic prime number not greater
than N.

Input
The first line contains an integer T denoting the number of test cases.
Each of the subsequent T lines contain a single integer N without leading/trailing spaces.

Output
Print T lines.
For each test case, print a single integer denoting the largest palindromic prime number which does not exceed N.

Constraints
1 <= T <= 10^6
2 <= N <= 10^13
"""
from sys import stdin, stdout

def is_palindrome(num_str):
    for i in range(len(num_str)/2 +1):
        if num_str[i] != num_str[-i-1]:
            return False
    return True

def is_prime(num):
    for i in range(2, num/2+1):
        if num%i==0:
            return False
    return True

def get_max_floor(tlist, num):
    i = 0
    list_len = len(tlist)
    while tlist[i] <= num and i < list_len-1:
        i += 1
    return str(tlist[i-1])

if __name__ == '__main__':
    T = int(stdin.readline())
    N = list()
    palprim = list()
    for i in range(T):
        N.append(int(stdin.readline()))

    max_N = sorted(N)[-1]

    for i in range(max_N +1):
        if is_palindrome(str(i)):
            if is_prime(i):
                palprim.append(i)

    palprim.append(0)

    for each in N:
        print ""
        stdout.write(get_max_floor(palprim, each))
