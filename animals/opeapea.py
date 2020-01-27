from animals import Animal
from interfaces.flying import IFlying
from interfaces.terrestrial import ITerrestrial
from interfaces import Identifiable

class Opeapea(Animal, IFlying, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Opeapea")
        IFlying.__init__(self)
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Moth", "Beetle", "Termite" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The opeapea ate {prey} for a meal')
        else:
            print(f'The opeapea rejects the {prey}')


    def __str__(self):
        return f'Opeapea {self.id}. doing bat stuff' 
