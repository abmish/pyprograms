"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world
"""

user_in = raw_input("Input space separated words: ")
split_into_words = user_in.split(" ")
print " ".join(sorted(list(set(split_into_words))))