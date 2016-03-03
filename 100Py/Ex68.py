"""
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n
is input by console.
"""

def even_gen(num):
    while num%2 != 0:
        num -= 1
    while num >= 0:
        yield num
        num -= 2

output = []
user_in = int(raw_input("input an integer :"))
for elem in even_gen(user_in):
    output.append(str(elem))

print ",".join(reversed(output))