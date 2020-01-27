from plants import Plant
from interfaces import Identifiable

class MountainAppleTree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree")
        Identifiable.__init__(self)

    def __str__(self):
        return f"Mountain Apple Tree {self.id}"
 