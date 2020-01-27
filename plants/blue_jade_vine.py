from plants import Plant
from interfaces import Identifiable

class BlueJadeVine(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine")
        Identifiable.__init__(self)

    def __str__(self):
        return f"Blue Jade Vine {self.id}"
 