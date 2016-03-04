"""
Define a class Person and its two child classes: Male and Female. All classes have a method "get_gender" which can print
"Male" for Male class and "Female" for Female class.
"""

class Person(object):
    def get_gender(self):
        return "not defined"

class Male(Person):
    def get_gender(self):
        return "Male"

class Female(Person):
    def get_gender(self):
        return "Female"