# import os
from arboretum import Arboretum
# from actions.release_animal import release_animal
# from actions.report import build_facility_report
# from environments import Habitat

avail_animals = ["Gold Dust Day Gecko", "River Dolphin", "Nene Goose", "Kikakapu", "Pueo", "'Ulae", "Ope'ape'a", "Happy-Face Spider"]
avail_plants = ["Mountain Apple Tree", "Silversword", "Rainbow Eucalyptus Tree", "Blue Jade Vine"]
avail_habitats = ["Mountain", "Swamp", "Grassland", "Forest", "River", "Coastline"]

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane", avail_animals, avail_plants, avail_habitats)

print(keahua.habitats_dict)


def animal_menu():
    for animal in avail_animals:
        print(f"{avail_animals.index(animal) + 1}. {animal}")

    choice = input(">> ")
    return choice


def plant_menu():
    for plant in avail_plants:
        print(f"{avail_plants.index(plant) + 1}. {plant}")

    choice = input(">> ")
    return choice


def build_menu():
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        keahua.annex_habitat()
        print(keahua.habitats_dict)

    if choice == "2":
        animal_choice = animal_menu()
        keahua.release_animal(animal_choice)

    if choice == "3":
        animal_choice = animal_menu()
        keahua.feed_animal(animal_choice)

    if choice == "4":
        plant_choice = plant_menu()
        keahua.cultivate_plant(plant_choice)

    if choice == "5":
        keahua.build_facility_report()
        

    if choice != "6":
        main_menu()


main_menu()
