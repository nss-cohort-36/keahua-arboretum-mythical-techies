from plants import Plant
from interfaces import Identifiable

class RainbowEucalyptus(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus")
        Identifiable.__init__(self)

    def __str__(self):
        return f"Rainbow Eucalyptus {self.id}"
