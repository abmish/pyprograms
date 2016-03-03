"""
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 200 inclusive using
random module and list comprehension.
"""

import random
print random.choice([num for num in range(201) if num%5 == 0 and num%7 == 0])