class Square():

    def __init__(self, side):

        self.side = side

    def compare_squares(self, other):

        if self is other:

            return True

        else:

            return False

square1 = Square(5)
square2 = Square(12)

square3 = square1

print(square1.compare_squares(square3))
print(square1.compare_squares(square2))

def compare(obj1, obj2):

    return obj1 is obj2

print(compare(square1, square2))
print(compare(square1, square3))
print(compare(square1, square1))
print(compare("a","b"))
print(compare("a","a"))