class Weapon:
    def __init__(self, name, type):
        self.__name = name
        self.__type = type
        self.__level = 1

    def upgrade(self):
        return 0

    def display(self):
        print (self.__name + ' ' + self.__type + ' ' + str(self.__level))

def run():
    the_catch = Weapon('The Catch','Polearm')
    cool_steel = Weapon('Cool Steel','Sword')

    the_catch.display()
    cool_steel.display()