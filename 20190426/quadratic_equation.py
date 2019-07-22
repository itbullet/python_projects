import math
a = float(input("Enter a number:")) #input of A constant
b = float(input("Enter b number:")) #input of B constant
c = float(input("Enter c number:")) #input of C constand
d =	b * b - 4 * a * c #calculating discriminant
if d >= 0:
	x1 = float((-b + math.sqrt(d))/(2 * a))
	x2 = float((-b - math.sqrt(d))/(2 * a))
	print("x1 = ", x1, "x2 = ", x2)
else:
	print("This quadratic equation doesn't have square roots!")
input()