"""
Please write a program to output a random even number between 0 and 10 inclusive using random module and list
comprehension.
"""

import random
print random.choice([num for num in range(11) if num%2 == 0])