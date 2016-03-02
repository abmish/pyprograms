"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

user_in = raw_input("Input a sentence: ")
output = {"DIGITS":0, "LETTERS":0}
for symbol in user_in:
    if symbol.isdigit():
        output["DIGITS"] += 1
    elif symbol.isalpha():
        output["LETTERS"] += 1
    else:
        pass

print "LETTERS", output["LETTERS"]
print "DIGITS", output["DIGITS"]
