from animals import Animal
from interfaces.animal import IFreshwater
from interfaces import Identifiable, IAquatic, ISwimming 


class Pueo(Animal, IFlying, Identifiable):
    
    def __init__(self):
        Animal.__init__(self, "Kikakapu") # Inherit props from Animal parent class
        # Inherit interface props
        IFreshwater.__init__(self) 
        IAquatic.__init__(self) 
        ISwimming.__init__(self) 
        Identifiable.__init__(self)
        self.__prey = {"Mackrel","Tuna", "Clownfish"}
    
    @property
    def prey(self):
        return self.__prey
    
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Kikakapu ate {prey}')
        else:
            print(f'The Kikakapu does not want to eat the {prey}')
    
    def __str__(self):
        return f'Kikakapu ID :: {self.id}'