

class Weapon:
    def __init__(self,name,weapon_type):
        self.__name = name
        self.__weapon_type = weapon_type
        self.__level = 1
    def getName(self):
        return self.__name

    def getWeapon_type(self):
        return self.__weapon_type


class Character:
    def __init__(self, name, vision, weapon_type):
        default_weapon = Weapon('None', 'None')

        self.__character_name = name
        self.__vision = vision
        self.__level = 1
        self.__weapon_type = weapon_type
        self.__weapon = default_weapon
        # constructor


    def levelup(self):
        self.__level += 1

    def display(self):
        print(self.__character_name + ' ' + self.__vision + ' Level:' + str(self.__level))

    def display2(self):
        return self.__character_name + ' ' + self.__vision + ' Level:' + str(self.__level)

    def display3(self):
        return self.__character_name + ' ' + self.__vision + ' Level:' + str(self.__level) + ' ' + self.getWeapon().getName()
    def setCharacterName(self, new_name):
        self.__character_name = new_name

    def setWeapon(self, weapon):
        #print (self.__weapon_type)
        #print (weapon.getWeapon_type())
        if self.__weapon_type == weapon.getWeapon_type():
            self.__weapon = weapon
            return True
        else:
            print (self.__character_name + ' cannot hold the ' + weapon.getName())
            return False

    def getWeapon(self):
        return self.__weapon

def run():

    print('Python class')
    barbatos = Character('Venti','Anemo','Bow')
    # create instance 'barbatos' from class 'Character'
    amos_bow = Weapon('Amos Bow', 'Bow')
    barbatos.setWeapon(amos_bow)
    print(barbatos.display3())

    beelzebub = Character('Ei','Electro','Polearm')
    beelzebub.setWeapon(amos_bow)

    engulfing_lightning = Weapon('Engulfing Lightning','Polearm')
    beelzebub.setWeapon(engulfing_lightning)

    print(beelzebub.display3())
