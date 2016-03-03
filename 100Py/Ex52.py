"""
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
"""

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 *3.14

one_circle = Circle(2)
print one_circle.area()