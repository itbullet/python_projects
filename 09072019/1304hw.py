class Horse():

    def __init__(self, name, breed, rider):

        self.name = name
        self.breed = breed
        self.rider = rider

class Rider():

    def __init__(self, name):

        self.name = name

rider1 = Rider("John")
horse1 = Horse("Isabella", "Arabian horse", rider1)

print("Horse's name is {}, its breed is {} and rider's name is {}".format(horse1.name, horse1.breed, horse1.rider.name))