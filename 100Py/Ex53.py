"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which
can compute the area.
"""

class Rectange(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

a_rect = Rectange(5, 10)
print a_rect.area()
