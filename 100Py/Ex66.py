"""
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
"""

def fibo(num):
    if num == 0: return 0
    if num == 1: return 1
    return fibo(num -1) + fibo (num - 2)

user_in = int(raw_input("Which Fibonacci member do you want :"))
print fibo(user_in)