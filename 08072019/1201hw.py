class Apple():

    def __init__ (self, c, w, t, m):
        self.color = c
        self.weight = w
        self.taste = t
        self.mold = m

apple = Apple("green", 100, "sour", False)

print(apple.mold)