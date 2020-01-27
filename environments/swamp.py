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

class Swamp(Habitat, ISwimming, Identifiable, IStagnant, IFreshwater) : 
     def __init__(self):
        Habitat.__init__(self)
        Identifiable.__init__(self)
        IStagnant.__init__(self)
        IFreshwater.__init__(self)
        ISunlight.__init__(self)
        Habitat.plant_limit = 12
        Habitat.animal_limit = 18
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
