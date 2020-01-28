from animals import Animal
from interfaces.terrestrial import ITerrestrial
from interfaces import Identifiable

class GoldDustDayGecko(Animal, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        ITerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = ["Ant", "Beetle", "Termite"]

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Gold Dust Day Gecko ate {prey} for a meal')
        else:
            print(f'The Gold Dust Day Gecko rejects the {prey}')


    def __str__(self):
        return f'Gold Dust Day Gecko {self.id}. doing gecko stuff' 
