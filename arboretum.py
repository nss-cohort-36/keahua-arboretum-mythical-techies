import os
from environments import River


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