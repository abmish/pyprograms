"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

user_in = raw_input("Input a sentence: ")
output = {"UPPER CASE":0, "LOWER CASE":0}
for symbol in user_in:
    if symbol.isupper():
        output["UPPER CASE"] += 1
    elif symbol.islower():
        output["LOWER CASE"] += 1
    else:
        pass

print "UPPER CASE", output["UPPER CASE"]
print "LOWER CASE", output["LOWER CASE"]
