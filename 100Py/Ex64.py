"""
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
"""

user_in = int(raw_input("Input an integer :"))
total = 0.0
for i in range(1, user_in + 1):
    total += float(float(i)/(i+1))

print total