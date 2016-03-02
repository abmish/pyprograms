"""
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age
and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

from operator import itemgetter
output = []
user_in = raw_input("Input details as name,age,score :")
while True:
    str_in = raw_input("Input details as name,age,score or blank: ")
    if not str_in:
        break
    output.append(tuple(str_in.split(",")))

print sorted(output, key=itemgetter(0,1,2))
