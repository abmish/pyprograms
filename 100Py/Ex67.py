"""
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
"""

def fibo(num):
    if num == 0: return 0
    if num == 1: return 1
    return fibo(num -1) + fibo (num - 2)

user_in = int(raw_input("Which Fibonacci member do you want :"))
fibo_series = [str(fibo(i)) for i in range(0, user_in + 1)]
print ",".join(fibo_series)