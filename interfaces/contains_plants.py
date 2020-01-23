class IContainsPlants():

    def __init__(self):
        self.plants = []

    def add_plants(self, plant):
        self.plants.append(plant)
        print(f'You added a {plant}')