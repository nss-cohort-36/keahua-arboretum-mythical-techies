from animals import Animal
from interfaces.flying import IFlying
from interfaces.terrestrial import ITerrestrial
from interfaces import Identifiable

class NeneGoose(Animal, IFlying, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IFlying.__init__(self)
        ITerrestrial.__init__(self)        
        Identifiable.__init__(self)
        self.__prey = { "Grass", "Weeds", "Berries" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Nene Goose ate {prey} for a meal')
        else:
            print(f'The Nene Goose rejects the {prey}')


    def __str__(self):
        return f'Nene Goose {self.id}. Soaring, Flying' 
