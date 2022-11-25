class Hero:
    def __init__(self, agility=0, speed=0, attack=0, power=0):
        self.__agility = agility
        self.__speed = speed
        self.__attack = attack
        self.__power = power

    def setglty(self, agility):
        self.__agility = agility

    def getglty(self):
        return self.__agility

    def setspd(self, speed):
        self.__speed = speed

    def getspd(self):
        return self.__speed

    def setttck(self, attack):
        self.__attack = attack

    def getttck(self):
        return self.__attack

    def setpwr(self, power):
        self.__power = power

    def getpwr(self):
        return self.__power


superhero = Hero()
superhero.setglty(65)
superhero.setspd(100)
superhero.setttck(30)
superhero.setpwr(50)
print(f'Ловкость {superhero.getglty()}\n'
      f'Скорость {superhero.getspd()}\n'
      f'Атака {superhero.getttck()}\n'
      f'Сила {superhero.getpwr()}\n')
