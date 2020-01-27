from interfaces import IAquatic

class IFreshwater(IAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "hypertonic"
