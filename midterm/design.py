import datetime

class Weapon:
    def __init__(self, name, type):
        self.__weapon_name = name
        self.__type = type
        self.__level = 1
        # constructor

    def levelup(self):
        self.__level += 1

    def display(self):
        print(self.__weapon_name + ' ' + self.__type + ' Level:' + str(self.__level))

def q01():
    skyward_harp = Weapon('Skyward Harp', 'Bow')
    # Your code here
    # Example
    # weapon
      # name: Skyward Harp
      # type: Bow
      # level: 1

    return 0


class Equipment: #Q2
    def __init__(self, name, price):
        # Protected member
        self.__price = price
        self.__name = name

    def show(self):
        return self.__name + ' ' + self.__price


def q03():
    mylist = [65, 34, 31, 4, 39, 6, 18, 12]
    # Your code here
    return max(mylist)
    #print the maximum value without using for/while loop


def q04(n):
    # Your code here - expected print out 7 Aug 2566
    today = datetime.datetime.now()
    buddhist_year = today.year + 543
    print(today.strftime("%d %b ") + str(buddhist_year))
    return 0 #Buddhist year

def q05():
    # Your code here
    nums = range(1422, 1456)
    return sum(nums)
    # sum of 1422, 1433 , 1424 ... 1454, 1455

def q06(nation):
    mydict = {
        "Mondstadt":"From amongst mountains and wide-open plains, carefree breezes carry the scent of dandelions - a gift from the Anemo God, Barbatos.",
        "Liyue":"Mountains stand tall and proud alongside the stone forest, that, together with the open plains and lively rivers.",
        "Inazuma":"On winding shores and towering cliffs, and in forests and mountains full of secrets, witness the Eternity pursued by Her Excellency, the Almighty Narukami Ogosho."
    }
    return mydict[nation]

"""
Mondstadt	

From amongst mountains and wide-open plains, carefree breezes carry the scent of dandelions - a gift from the Anemo God, Barbatos.

Liyue	

Mountains stand tall and proud alongside the stone forest, that, together with the open plains and lively rivers.

Inazuma	

On winding shores and towering cliffs, and in forests and mountains full of secrets, witness the Eternity pursued by Her Excellency, the Almighty Narukami Ogosho.

"""