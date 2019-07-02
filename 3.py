class Cat:
    legs = 4
    hunger = 6 # out of 10
    loneliness = 5 # out of 10
    happiness = 3 # out of 10
    tiredness = 7

    def feed(self):
        self.hunger = self.hunger-1
    def pet(self):
        self.happiness = self.happiness +1
        self.loneliness = self.loneliness-1
    def sleep(self):
        self.tiredness = self.tiredness-1


tom =  Cat()
print ('Cat status before feed, pet and sleep')
print ('hunger {0}'.format(tom.hunger))
print ('happiness {0}'.format(tom.happiness))
print ('loneliness {0}'.format(tom.loneliness))
print ('tiredness {0}'.format(tom.tiredness))
tom.feed()
tom.pet()
tom.sleep()
print ('Cat status after feed, pet and sleep')
print ('hunger {0}'.format(tom.hunger))
print ('happiness {0}'.format(tom.happiness))
print ('loneliness {0}'.format(tom.loneliness))
print ('tiredness {0}'.format(tom.tiredness))

class Cat:
    legs = 4
    hunger = 6 # out of 10
    loneliness = 5 # out of 10
    happiness = 3 # out of 10
    tiredness = 7

    def __init__(self, givenName):
        self.name = givenName

    def showName(self):
        print('The cat name is: {0}'.format(self.name))

    def feed(self):
        self.hunger = self.hunger-1

    def pet(self):
        self.happiness = self.happiness +1
        self.loneliness = self.loneliness-1

    def sleep(self):
        self.tiredness = self.tiredness-1


tom =  Cat('Tom')
tom.showName()

jerry = Cat('Jerry')
jerry.showName()

