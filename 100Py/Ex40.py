"""
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print all values except the first 5 elements in the list.
"""

def num_square_list(num, limit):
    sq_list = list()
    for i in range(1, num+1):
        sq_list.append(i ** 2)
    print sq_list[limit:]

num_square_list(20, 5)