"""
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
company name of a given email address. Both user names and company names are composed of letters only.
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
"""
import re
user_email = raw_input("input email id : ")
pattern = "(\w+)@(\w+)\.(com)"
check_match = re.match(pattern, user_email)

print check_match.group(2)
