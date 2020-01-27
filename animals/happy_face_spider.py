from animals import Animal
# from interfaces import IStagnant
from interfaces import Identifiable


class HappyFaceSpider(Animal):

    def __init__(self):
        Animal.__init__(self, "Happy-Face Spider")
        # IStagnant.__init__(self)
        Identifiable.__init__(self)
        self.__prey = {"Grasshopper", "Fruit fly"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The {self.species} ate {prey} for a meal')
        else:
            print(f'The {self.species} rejects the {prey}')

    def __str__(self):
        return f'{self.species} {self.id}. I am joy.'
