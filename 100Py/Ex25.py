"""
Define a class, which have a class parameter and have a same instance parameter.
"""

class Car:
    # Define the class parameter "name"
    name = "Car"

    def __init__(self, name = None):
    # self.name is the instance parameter
        self.name = name

honda = Car("Honda")
print "%s make is %s." % (Car.name, honda.name)

hyundai = Car()
hyundai.name = "Hyundai"
print "%s make is %s." % (Car.name, hyundai.name)