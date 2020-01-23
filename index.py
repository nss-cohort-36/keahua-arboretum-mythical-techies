import os
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report
from environments import Habitat

avail_animals = ["Gold Dust Day Gecko", "River Dolphin", "Nene Goose", "Kīkākapu", "Pueo", "'Ulae", "Ope'ape'a", "Happy-Face Spider"]
avail_plants = ["Mountain Apple Tree", "Silversword", "Rainbow Eucalyptus Tree", "Blue Jade Vine"]
avail_habitats = ["Mountain", "Swamp", "Grassland", "Forest", "River", "Coastline"]

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane", avail_animals, avail_plants, avail_habitats)


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

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        pass

    if choice == "4":
        pass

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

main_menu()
