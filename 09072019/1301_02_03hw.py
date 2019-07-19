class Shape():

    def what_am_i(self):

        return "I am a shape"


class Rectangle(Shape):

    def __init__(self, side1, side2):

        self.side1 = side1
        self.side2 = side2

    def calculate_perimeter(self):

        return 2*self.side1 + 2*self.side2

class Square(Shape):

    def __init__(self, side):

        self.side = side

    def calculate_perimeter(self):

        return self.side*4

    def change_size(self, value):

        self.side += value


rectangle1 = Rectangle(5, 10)
print("Rectangle's perimeter is {}.".format(rectangle1.calculate_perimeter()))

square1 = Square(5)
print("Square's perimeter is {}.".format(square1.calculate_perimeter()))

square1.change_size(1)
print("Square's side is {} and perimeter is {}.".format(square1.side, square1.calculate_perimeter()))

square1.change_size(-3)
print("Square's side is {} and perimeter is {}.".format(square1.side, square1.calculate_perimeter()))

print(rectangle1.what_am_i())

print(square1.what_am_i())
