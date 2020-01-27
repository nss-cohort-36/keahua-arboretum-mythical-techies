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

    @property
    def rivers(self):
        return self.__rivers

    def annex_river(self, river):
        self.__rivers.append(river)

    @property
    def grasslands(self):
        return self.__grasslands

    def annex_grassland(self, grassland):
        self.__grasslands.append(grassland)

    @property
    def mountains(self):
        return self.__mountains

    def annex_mountain(self, mountain):
        self.__mountains.append(mountain)

    @property
    def swamps(self):
        return self.__swamps

    def annex_swamp(self, swamp):
        self.__swamps.append(swamp)

    @property
    def forests(self):
        return self.__forests

    def annex_forest(self, forest):
        self.__forests.append(forest)

    @property
    def coastlines(self):
        return self.__coastlines

    def annex_coastline(self, coastline):
        self.__coastlines.append(coastline)

    def annex_habitat(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        for habitat in self.avail_habitats:
            print(f"{self.avail_habitats.index(habitat) + 1}. {habitat}")

        choice = input("Choose your habitat > ")
        print(choice)

    # Add other biomes

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
            animal_to_add = HappyFaceSpider()
            potentialHabitatsForAddedAnimal = [swamp for swamp in self.habitats_dict["Swamp"]]

        for i, v in enumerate(potentialHabitatsForAddedAnimal):
            print(f'{i + 1}. {type(v).__name__} {v.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        print(potentialHabitatsForAddedAnimal[int(choice)-1].id)

        targetHabitat = potentialHabitatsForAddedAnimal[int(choice)-1]

        habitatTargetList = self.habitats_dict[type(targetHabitat).__name__] ## ?
        object_class_animal_to_add = habitatTargetList[habitatTargetList.index(targetHabitat)]

        if len(object_class_animal_to_add.animals) < object_class_animal_to_add.animal_limit: 
            object_class_animal_to_add.animals.append(animal_to_add)
            print(f"You have added an {type(animal_to_add).__name__} to {type(targetHabitat).__name__} {object_class_animal_to_add}")

        else:
            print("That habitat is already at it's max for animals. Please choose another habitat")

        print(object_class_animal_to_add.animals)

    def cultivate_plant(self, choice):
        if choice == "1":
            plant_to_add = MountainAppleTree()
            potentialHabitatsForAddedPlant = [mountain for mountain in self.habitats_dict["Mountain"]]

        if choice == "2":
            animal_to_add = Silversword()
            potentialHabitatsForAddedPlant = [grassland for grassland in self.habitats_dict["Grassland"]]

        if choice == "3":
            animal_to_add = RainbowEucalyptus()
            potentialHabitatsForAddedPlant = [forest for forest in self.habitats_dict["Forest"]]

        if choice == "4":
            animal_to_add = BlueJadeVine()
            potentialHabitatsForAddedPlant = [grassland for grassland in self.habitats_dict["Grassland"]] + [swamp for swamp in self.habitats_dict["Swamp"]]

        for i, v in enumerate(potentialHabitatsForAddedPlant):
            print(f'{i + 1}. {type(v).__name__} {v.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        print(potentialHabitatsForAddedPlant[int(choice)-1].id)

        targetHabitat = potentialHabitatsForAddedPlant[int(choice)-1]

        habitatTargetList = self.habitats_dict[type(targetHabitat).__name__] ## ?
        object_class_animal_to_add = habitatTargetList[habitatTargetList.index(targetHabitat)]

        if len(object_class_animal_to_add.animals) < object_class_animal_to_add.animal_limit: 
            object_class_animal_to_add.animals.append(animal_to_add)
            print(f"You have added an {type(animal_to_add).__name__} to {type(targetHabitat).__name__} {object_class_animal_to_add}")

        else:
            print("That habitat is already at it's max for animals. Please choose another habitat")

        print(object_class_animal_to_add.animals)