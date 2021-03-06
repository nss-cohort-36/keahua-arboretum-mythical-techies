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

        choice = input("\nChoose what you want to annex \n>")

        if choice == "1":
            habitat = Mountain()
        
        elif choice == "2":
            habitat = Swamp()
        
        elif choice == "3":
            habitat = Grassland()
        
        elif choice == "4":
            habitat = Forest()
        
        elif choice == "5":
            habitat = River()

        elif choice == "6":
            habitat = Coastline()

        else:
            print("That is not a valid choice")
            return

        self.habitats_dict[type(habitat).__name__].append(habitat)

    def release_animal(self, choice):

        if choice == "1":
            animal_to_add = GoldDustDayGecko()
            potentialHabitatsForAddedAnimal = [forest for forest in self.habitats_dict["Forest"]]

        elif choice == "2":
            animal_to_add = RiverDolphin()
            potentialHabitatsForAddedAnimal = [river for river in self.habitats_dict["River"]] + [coastline for coastline in self.habitats_dict["Coastline"]]

        elif choice == "3":
            animal_to_add = NeneGoose()
            potentialHabitatsForAddedAnimal = [grassland for grassland in self.habitats_dict["Grassland"]]

        elif choice == "4":
            animal_to_add = Kikakapu()
            potentialHabitatsForAddedAnimal = [river for river in self.habitats_dict["River"]] + [swamp for swamp in self.habitats_dict["Swamp"]]

        elif choice == "5":
            animal_to_add = Pueo()
            potentialHabitatsForAddedAnimal = [grassland for grassland in self.habitats_dict["Grassland"]] + [forest for forest in self.habitats_dict["Forest"]]

        elif choice == "6":
            animal_to_add = Ulae()
            potentialHabitatsForAddedAnimal = [coastline for coastline in self.habitats_dict["Coastline"]]

        elif choice == "7":
            animal_to_add = Opeapea()
            potentialHabitatsForAddedAnimal = [forest for forest in self.habitats_dict["Forest"]] + [mountain for mountain in self.habitats_dict["Mountain"]]

        elif choice == "8":
            animal_to_add = HappyFaceSpider()
            potentialHabitatsForAddedAnimal = [swamp for swamp in self.habitats_dict["Swamp"]]

        else:
            print("That is not a valid choice.")
            return

        for i, v in enumerate(potentialHabitatsForAddedAnimal):

            valid_habitat = len(v.animals) < v.animal_limit
            
            if not valid_habitat:
                print('')
            else:
                print(f'{i + 1}. {type(v).__name__} ({len(v.animals)} animals)')

        # Prompts the user to select a habitat
        print(f"\nWhere would you like to release the {animal_to_add.species}")
        choice = input("> ")

        if int(choice) > len(potentialHabitatsForAddedAnimal):
            print("That is not a valid choice.")
            return

        targetHabitat = potentialHabitatsForAddedAnimal[int(choice)-1]

        habitatTargetList = self.habitats_dict[type(targetHabitat).__name__]
        object_class_animal_to_add = habitatTargetList[habitatTargetList.index(targetHabitat)]

        if len(object_class_animal_to_add.animals) < object_class_animal_to_add.animal_limit: 
            object_class_animal_to_add.add_animal(animal_to_add)
            print(f"You have added an {animal_to_add.species} to {type(targetHabitat).__name__}")

        else:
            print("That habitat is already at it's max for animals. Please choose another habitat")


    def cultivate_plant(self, choice):
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == "1":
            plant_to_add = MountainAppleTree()
            potentialHabitatsForAddedPlant = [mountain for mountain in self.habitats_dict["Mountain"]]

        elif choice == "2":
            plant_to_add = Silversword()
            potentialHabitatsForAddedPlant = [grassland for grassland in self.habitats_dict["Grassland"]]

        elif choice == "3":
            plant_to_add = RainbowEucalyptus()
            potentialHabitatsForAddedPlant = [forest for forest in self.habitats_dict["Forest"]]

        elif choice == "4":
            plant_to_add = BlueJadeVine()
            potentialHabitatsForAddedPlant = [grassland for grassland in self.habitats_dict["Grassland"]] + [swamp for swamp in self.habitats_dict["Swamp"]]

        else:
            print("That is not a valid choice.")
            return

        for i, v in enumerate(potentialHabitatsForAddedPlant):
            print(f'{i + 1}. {type(v).__name__} ({len(v.plants)} plants)')

        print(f"Where would you like to plant the {plant_to_add.species}?")
        choice = input("> ")

        if int(choice) > len(potentialHabitatsForAddedPlant):
            print("That is not a valid choice.")
            return

        targetHabitat = potentialHabitatsForAddedPlant[int(choice)-1]

        habitatTargetList = self.habitats_dict[type(targetHabitat).__name__]
        object_class_plant_to_add = habitatTargetList[habitatTargetList.index(targetHabitat)]

        if len(object_class_plant_to_add.plants) < object_class_plant_to_add.plant_limit: 
            object_class_plant_to_add.add_plant(plant_to_add)

            print(f"You have added an {plant_to_add.species} to {type(targetHabitat).__name__}")

        else:
            print("That habitat is already at it's max for animals. Please choose another habitat")


    def feed_animal(self, choice):
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == "1":
            animal_to_feed = GoldDustDayGecko()

        elif choice == "2":
            animal_to_feed = RiverDolphin()

        elif choice == "3":
            animal_to_feed = NeneGoose()

        elif choice == "4":
            animal_to_feed = Kikakapu()

        elif choice == "5":
            animal_to_feed = Pueo()

        elif choice == "6":
            animal_to_feed = Ulae()

        elif choice == "7":
            animal_to_feed = Opeapea()

        elif choice == "8":
            animal_to_feed = HappyFaceSpider()

        else:
            print("No no. Feed something else.")
            return

        for i, v in enumerate(animal_to_feed.prey):
                print(f'{i + 1}. {v}')

        print("Which prey do you want to feed the animal?")
        choice = input("> ")

        targetPrey = animal_to_feed.prey[int(choice)-1]
        animal_to_feed.feed(targetPrey)

        
    # Create the build facility report...
    def build_facility_report(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for key in self.habitats_dict:
            for habitat in self.habitats_dict[key]:
                print(f'{type(habitat).__name__} [{str(habitat.id)[0:8]}]')
                
                for animal in habitat.animals:
                    print(f'    -- {animal.species} ({str(animal.id)[0:8]})')
                    
                for plant in habitat.plants:
                    print(f'    -- {plant.species} ({str(plant.id)[0:8]})')
                print('')
        input("\n\nPress any key to continue...")
    
