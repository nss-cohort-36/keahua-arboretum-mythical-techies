import os
from environments import River, Swamp, Coastline, Mountain, Forest, Grassland
from animals import RiverDolphin, HappyFaceSpider, GoldDustDayGecko, Opeapea, NeneGoose, Ulae, Pueo, Kikakapu
from plants import BlueJadeVine, MountainAppleTree, RainbowEucalyptus, Silversword

class Arboretum:
    def __init__(self, name, address, avail_animals, avail_plants, avail_habitats):
        self.name = name
        self.address = address
        self.avail_animals = avail_animals
        self.avail_plants = avail_plants
        self.avail_habitats = avail_habitats
        self.habitats_dict = {habitat: [] for habitat in avail_habitats}

    def annex_habitat(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        for habitat in self.avail_habitats:
            print(f"{self.avail_habitats.index(habitat) + 1}. {habitat}")

        choice = input("Choose your habitat > ")
        print(choice)

        if choice == "1":
            habitat = Mountain()
        
        if choice == "2":
            habitat = Swamp()
        
        if choice == "3":
            habitat = Grassland()
        
        if choice == "4":
            habitat = Forest()
        
        if choice == "5":
            habitat = River()

        if choice == "6":
            habitat = Coastline()

        # else:
        #     print("That is not a valid choice")
        #     return

        self.habitats_dict[type(habitat).__name__].append(habitat)
        print(self.habitats_dict[type(habitat).__name__][0].id)

    def release_animal(self, choice):
        if choice == "1":
            animal_to_add = GoldDustDayGecko()
            potentialHabitatsForAddedAnimal = [forest for forest in self.habitats_dict["Forest"]]

        if choice == "2":
            animal_to_add = RiverDolphin()
            potentialHabitatsForAddedAnimal = [river for river in self.habitats_dict["River"]] + [coastline for coastline in self.habitats_dict["Coastline"]]

        if choice == "3":
            animal_to_add = NeneGoose()
            potentialHabitatsForAddedAnimal = [grassland for grassland in self.habitats_dict["Grassland"]]

        if choice == "4":
            animal_to_add = Kikakapu()
            potentialHabitatsForAddedAnimal = [river for river in self.habitats_dict["River"]] + [swamp for swamp in self.habitats_dict["Swamp"]]

        if choice == "5":
            animal_to_add = Pueo()
            # print(f"I am an {animal_to_add} ")
            potentialHabitatsForAddedAnimal = [grassland for grassland in self.habitats_dict["Grassland"]] + [forest for forest in self.habitats_dict["Forest"]]

        if choice == "6":
            animal_to_add = Ulae()
            potentialHabitatsForAddedAnimal = [coastline for coastline in self.habitats_dict["Coastline"]]

        if choice == "7":
            animal_to_add = Opeapea()
            potentialHabitatsForAddedAnimal = [forest for forest in self.habitats_dict["Forest"]] + [mountain for mountain in self.habitats_dict["Mountain"]]

        if choice == "8":
            #animal_to_add = HappyFaceSpider()
            #for testing until the spider will be ready
            animal_to_add = RiverDolphin() 
            potentialHabitatsForAddedAnimal = [swamp for swamp in self.habitats_dict["Swamp"]]

        for i, v in enumerate(potentialHabitatsForAddedAnimal):
            print(f'{i + 1}. {type(v).__name__} {v.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        print(potentialHabitatsForAddedAnimal[int(choice)-1].id)

        targetHabitat = potentialHabitatsForAddedAnimal[int(choice)-1]

        habitatTargetList = self.habitats_dict[type(targetHabitat).__name__]
        object_class_animal_to_add = habitatTargetList[habitatTargetList.index(targetHabitat)]

        if len(object_class_animal_to_add.animals) < object_class_animal_to_add.animal_limit:
            object_class_animal_to_add.animals.append(animal_to_add)
            print(f"You have added an {type(animal_to_add).__name__} to {type(targetHabitat).__name__} {object_class_animal_to_add}")

        else:
            print("That habitat is already at it's max for animals. Please choose another habitat")

        print(object_class_animal_to_add.animals)
        # print(habitatTargetList[habitatTargetList.index(targetHabitat)].animals)

    def feed_animal(self, choice):
        if choice == "1":
            animal_to_feed = GoldDustDayGecko()

        if choice == "2":
            animal_to_feed = RiverDolphin()

        if choice == "3":
            animal_to_feed = NeneGoose()

        if choice == "4":
            animal_to_feed = Kikakapu()

        if choice == "5":
            animal_to_feed = Pueo()

        if choice == "6":
            animal_to_feed = Ulae()

        if choice == "7":
            animal_to_feed = Opeapea()

        if choice == "8":
            animal_to_feed = HappyFaceSpider()

        for i, v in enumerate(animal_to_feed.prey):
                print(f'{i + 1}. {v}')

        print("Which prey do you want to feed the animal?")
        choice = input("> ")

        targetPrey = animal_to_feed.prey[int(choice)-1]
        animal_to_feed.feed(targetPrey)
