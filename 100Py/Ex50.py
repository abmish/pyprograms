"""
Define a class named American which has a static method called printNationality.
"""

class American(object):
    @staticmethod
    def print_nationality():
        print "America"

one_american = American()
one_american.print_nationality()
American.print_nationality()