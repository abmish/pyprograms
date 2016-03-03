"""
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma
separated form while n is input by console.
"""
def num_7_5(num):
    counter = 0
    while counter <= num:
        if counter%5 == 0 and counter%7 == 0:
            yield counter
        counter += 1

output = []
user_in = int(raw_input("input an integer :"))
for elem in num_7_5(user_in):
    output.append(str(elem))

print ",".join(output)