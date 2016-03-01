"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
"""

sequence_of_lines = []
while True:
    input_string = raw_input()
    if input_string:
        sequence_of_lines.append(input_string.upper())
    else:
        break

for line in sequence_of_lines:
    print line