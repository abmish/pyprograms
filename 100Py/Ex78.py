"""
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
"""

import random
print random.sample([num for num in range(100, 200) if num%2 == 0], 5)