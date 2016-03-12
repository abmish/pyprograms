"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

tdict = {}
def fibo(num):
    tdict[num] = tdict.get(num, 0) or (num <= 1 and 1 or fibo(num-1) + fibo(num-2))
    return tdict[num]

total = 0
count = 0
while fibo(count) <= 4000000:
    if not fibo(count) % 2: total = total + fibo(count)
    count += 1

print total