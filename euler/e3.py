"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

num = 600851475143
pri = 2
while pri * pri < num:
    while num % pri ==0:
        num = num / pri
    pri = pri + 1

print num