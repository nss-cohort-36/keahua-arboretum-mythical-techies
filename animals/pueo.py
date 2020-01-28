from animals import Animal
from interfaces import IFlying, Identifiable, ITerrestrial 
class Pueo(Animal, IFlying, Identifiable, ITerrestrial):
    
    def __init__(self):
        Animal.__init__(self, "Pueo") # Inherit props from Animal parent class
        IFlying.__init__(self) # Inherit interface props
        Identifiable.__init__(self)
        ITerrestrial.__init__(self)
        self.__prey = ["Mouse", "Gerbil", "Hamster", "Rat"]
    
    @property
    def prey(self):
        return self.__prey
    
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Pueo ate {prey}')
        else:
            print(f'The Pueo does not want to eat the {prey}')
    
    def __str__(self):
        return f'Pueo ID :: {self.id}'