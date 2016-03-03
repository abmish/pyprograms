"""
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0)
"""

def custom_func(num):
    if num == 0:
        return 0
    else:
        return custom_func(num - 1) +100

user_in = int(raw_input("Input an integer :"))
print custom_func(user_in)