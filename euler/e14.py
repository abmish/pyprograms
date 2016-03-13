"""
The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

store = {1:1}
def chain(store, num):
    if not store.get(num, 0):
        if num % 2:
            store[num] = 1 + chain(store, 3*num +1)
        else:
            store[num] = 1 + chain(store, num/2)
    return store[num]

num1, num2 = 0, 0
for count in xrange(1, 1000000):
    check = chain(store, count)
    if check > num1: num1, num2 = check, count

print num2