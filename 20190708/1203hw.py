import math

class Triangle():

    def __init__(self, a, b, c):

        self.aside = a
        self.bside = b
        self.cside = c

    def area(self):
        s = (self.aside + self.bside + self.cside)/2
        area = math.sqrt(s*(s-self.aside)*(s-self.bside)*(s-self.cside))
        return(area)

triange = Triangle(5, 10, 12)

print(triange.area())