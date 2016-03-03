"""
Define a function which can generate and print a list where the values are square of numbers between 1 and 20
(both included).
"""

def num_square_list(num):
    sq_list = list()
    for i in range(1, num+1):
        sq_list.append(i ** 2)
    print sq_list

num_square_list(20)