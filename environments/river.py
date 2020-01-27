from .habitat import Habitat
from interfaces import IAquatic
from interfaces import Identifiable
from animals import RiverDolphin


class River(Habitat, Identifiable):

    def __init__(self):
        Habitat.__init__(self)
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
