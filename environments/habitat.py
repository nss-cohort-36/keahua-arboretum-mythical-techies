from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces import Identifiable

class Habitat(IContainsAnimals, IContainsPlants, Identifiable):
    def __init__(self):
        IContainsPlants.__init__(self)
        IContainsAnimals.__init__(self)
        Identifiable.__init__(self)
        self.plant_limit = 1
        self.animal_limit = 1

    def release_animal(self, animal):
        if len(self.animals) < self.animal_limit:
            self.add_animal(animal)
            print(f'You added a {animal}')
        else:
            print(f'That biome is full. Please select another biome')

    def __str__(self):
        return f'\nThis is a test: Your animal limit is {self.animal_limit}, and your plant_limit is {self.plant_limit}'
    
