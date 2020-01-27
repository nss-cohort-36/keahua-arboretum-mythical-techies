from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Habitat(IContainsAnimals, IContainsPlants):
    def __init__(self):
        IContainsPlants.__init__(self)
        IContainsAnimals.__init__(self)
        self.plant_limit = 0
        self.animal_limit = 0

    def __str__(self):
        return f'\nThis is a test: Your animal limit is {self.animal_limit}, and your plant_limit is {self.plant_limit}'
