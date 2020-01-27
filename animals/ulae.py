from animals import Animal
from interfaces.saltwater import ISaltwater
from interfaces.aquatic import IAquatic
from interfaces import Identifiable

class Ulae(Animal, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Minnow", "Sardine", "Reef Fish" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The ulae ate {prey} for a meal')
        else:
            print(f'The ulae rejects the {prey}')


    def __str__(self):
        return f'Ulae {self.id}. Swimming swimming swimming' 
