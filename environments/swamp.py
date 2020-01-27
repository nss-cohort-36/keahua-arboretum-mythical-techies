import sys
from interfaces import Identifiable
from .habitat import Habitat
#from interfaces.habitats import IStagnant

sys.path.append('../')

class Swamp(Habitat, Identifiable):
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

     def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

     # def __str__(self):
     #    return self.name
