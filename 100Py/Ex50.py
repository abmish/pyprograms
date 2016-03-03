"""
Define a class named American which has a static method called printNationality.
"""

class American(object):
    @staticmethod
    def print_nationality():
        print "America"

oneAmerican = American()
oneAmerican.print_nationality()
American.print_nationality()