class IContainsAnimals():

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'You added a {animal}')

        # Add method to feed animals
