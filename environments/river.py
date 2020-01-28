from .habitat import Habitat
from interfaces import Identifiable


class River(Habitat, Identifiable):

    def __init__(self):
        Habitat.__init__(self)
        Identifiable.__init__(self)
        self.plant_limit = 6
        self.animal_limit = 12

    def add_animal(self, animal):
        try:
            if animal.aquatic:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        # try:
        #     if plant.freshwater:
        #         self.plants.append(plant)
        # except AttributeError:
        #     raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
        self.plants.append(plant)
