import os
from environments import River
from animals import RiverDolphin


class Arboretum:
    # def __init__(self, name, address):
        # self.name = name
        # self.address = address
    #     self.grasslands = []
    #     self.grasslands = []

    #  add other biome types

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

    # Add other biomes

        if choice == "5":
            river = River()

            self.habitats_dict["River"].append(river)
            print(self.habitats_dict["River"][0].id)
        if choice == "2":
            pass 

    def release_animal(self, choice):
        if choice == "1":
            gecko = Gecko()

            habitats_arr = [ forest for forest in self.habitats_dict["Forest"] ]

            for i, v in enumerate(habitats_arr):
                print(f'{i + 1}. Forest {v}')

        if choice == "2":
            dolphin = RiverDolphin()

            habitats_arr = [ river for river in self.habitats_dict["River"] ] + [ river for river in self.habitats_dict["River"] ]

            for i, v in enumerate(habitats_arr):
                print(f'{i + 1}. River {v}')

        if choice == "3":
            goose = Goose()

            for grassland in self.habitats_dict["Grassland"]:
                print(f'{index + 1}. Grassland {grassland.id}')
                index += 1

        if choice == "4":
            kikakapu = Kikakapu()

            for river in self.habitats_dict["River"]:
                print(f'{index + 1}. River {river.id}')
                index += 1

            for swamp in self.habitats_dict["Swamp"]:
                print(f'{index + 1}. Swamp {swamp.id}')
                index += 1

        if choice == "5":
            pueo = Pueo()

            for grassland in self.habitats_dict["Grassland"]:
                print(f'{index + 1}. Grassland {grassland.id}')
                index += 1

            for forest in self.habitats_dict["Forest"]:
                print(f'{index + 1}. Forest {forest.id}')
                index += 1

        if choice == "6":
            ulae = Ulae()

            for coastline in self.habitats_dict["Coastline"]:
                print(f'{index + 1}. Coastline {coastline.id}')
                index += 1

        if choice == "7":
            opeapea = Opeapea()

            for forest in self.habitats_dict["Forest"]:
                print(f'{index + 1}. Forest {forest.id}')
                index += 1

            for mountain in self.habitats_dict["Mountain"]:
                print(f'{index + 1}. Mountain {mountain.id}')
                index += 1

        if choice == "8":
            spider = Spider()

            for swamp in self.habitats_dict["Swamp"]:
                print(f'{index + 1}. Swamp {swamp.id}')
                index += 1

        print("Release the animal into which biome?")
        choice = input("> ")

        # arboretum.rivers[int(choice) - 1].animals.append(animal)