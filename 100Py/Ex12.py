"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number.  The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

output = []
for counter in range(1000, 3001):
    input_str = str(counter)
    if (int(input_str[0])%2==0) and (int(input_str[1])%2==0) and (int(input_str[2])%2==0) and (int(input_str[3])%2==0):
        output.append(input_str)
print ",".join(output)