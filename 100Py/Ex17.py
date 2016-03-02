"""
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

import sys
net_amount = 0
while True:
    user_in = raw_input()
    if not user_in:
        break
    input_components = user_in.split(" ")
    action = input_components[0]
    amount = int(input_components[1])
    if action == "D":
        net_amount += amount
    elif action == "W":
        net_amount -= amount

print net_amount