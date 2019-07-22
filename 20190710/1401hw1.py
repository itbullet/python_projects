class Square():

    square_list = []

    def __init__(self, side):

        self.side = side
        self.square_list.append(self.side)

    def calculate_perimeter(self):

        return self.side*4

    def change_size(self, value):

        self.side += value


square1 = Square(5)
square2 = Square(3)
square3 = Square(7)

print(Square.square_list)
print(square1)
print(square2)
print(square3)
