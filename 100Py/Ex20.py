"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""
def get_7_multiplier_le_n(temp):
    while temp%7!=0:
        temp -= 1
    while temp > 0:
        yield temp
        temp -= 7

n = int(raw_input("Input n :"))
outgen = get_7_multiplier_le_n(n)
print sorted([elem for elem in outgen])
