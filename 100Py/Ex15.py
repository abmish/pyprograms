"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

user_in = raw_input("Input a signle digit number: ")
print int("%s" % user_in) + \
      int("%s%s" % (user_in, user_in)) + \
      int("%s%s%s" % (user_in,user_in,user_in)) + \
      int("%s%s%s%s" % (user_in,user_in,user_in,user_in))
