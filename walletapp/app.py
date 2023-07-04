
class Character:
    def __init__(self, name, vision):
        self.__character_name = name
        self.__vision = vision
        self.__level = 1
        # constructor

    def levelup(self):
        self.__level += 1

    def display(self):
        print(self.__character_name + ' ' + self.__vision + ' Level:' + str(self.__level))

    def display2(self):
        return self.__character_name + ' ' + self.__vision + ' Level:' + str(self.__level)

    def setCharacterName(self, new_name):
        self.__character_name = new_name


def run():

    print('Python class')
    barbatos = Character('Venti','Anemo')
    # create instance 'barbatos' from class 'Character'
    print(barbatos.character_name)

    beelzebub = Character('Ei','Electro')
    print(beelzebub.character_name)
    beelzebub.display()
    beelzebub.setCharacterName('Raiden Shogun')
    print(beelzebub.display2())

    #barbatos.level = 20 Logic error

    beelzebub.levelup()
    print(beelzebub.display2())
