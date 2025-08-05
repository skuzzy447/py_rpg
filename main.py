from char_create import new_character
from main_menu import main_menu
import os
import sys

levels_path = os.path.abspath("./levels")
sys.path.append(levels_path)
from level_1 import *

def main():
    menu_selection = main_menu()
    if menu_selection == "new":
        player = new_character()
        print(player.describe())
        test(player)


if __name__ == "__main__":
    main()