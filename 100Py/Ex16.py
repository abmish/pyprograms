"""
Use a list comprehension to extract each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""

user_in = raw_input("Input list of numbers: ")
output = [num for num in user_in.split(",") if int(num)%2 != 0]
print ",".join(output)