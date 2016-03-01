"""
Write a program which can compute the factorial of a given list of comma-separated numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8,5
Then, the output should be:
40320,120
"""

def factorial(num):
    if num ==0:
        return 1
    return num * factorial(num - 1)

output = []
user_in = raw_input("Please input a comma-separated list of integers").split(",")
for element in user_in:
    output.append(str(factorial(int(element))))

print ",".join(output)