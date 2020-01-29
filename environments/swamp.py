import sys
from interfaces import IAquatic
from interfaces import ISwimming
from interfaces import Identifiable
from .habitat import Habitat
from interfaces import IStagnant
from interfaces.animal import IFreshwater
from interfaces import ISunlight

# from interfaces import ISunlight


sys.path.append('../')

class Swamp(Habitat, Identifiable) : 
     def __init__(self):
        Habitat.__init__(self)
        Identifiable.__init__(self)
        self.plant_limit = 12
        self.animal_limit = 8

    #  def __init__(self, name):
    #   self.name = name
    #   self.inhabitants = []

     def animal_count(self):
        return "This place has a bunch of animals in it"

     def add_animal(self, animal):
        try:
            if (animal.aquatic or animal.stagnant):
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-freshwater, or non stagnant animals to a swamp")

     def add_plant(self, plant):
        self.plants.append(plant)
        # try:
            # if plant.freshwater:
        # except AttributeError:
            # raise AttributeError("Cannot add plants that require brackish water or stagnant water to a swamp biome")

     # def __str__(self):
     #    return self.name
