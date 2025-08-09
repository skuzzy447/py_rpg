import os
import sys
path = os.path.abspath(os.getcwd())
sys.path.append(path)
import library
from actions import *
from constants import *
#Sends player to correct room
def level_1_start(player, room):
    os.system('clear')
    while True:
        if room == 1:
            room = room_1(player)
        else:
            return
#Room 1 game loop
def room_1(player):
    #room variables
    var_list = [["chest_opened", False],["rat_killed", False],["door_unlocked", False], ["chest_inventory", ["L1R1_Key", "shortsword"]], ["room_inventory", ["torch"]]]
    while True:
        #Makes a list of the values of all the variables in var_list and sets local variables. local variables are unnecessary but make the code more readable 
        var_keys = library.return_list_values(var_list)
        chest_opened = var_keys[0]
        rat_killed = var_keys[1]
        door_unlocked = var_keys[2]
        chest_inventory = var_keys[3]
        room_inventory = var_keys[4]
        has_torch = False
        for each in room_inventory:
            if each == "torch":
                has_torch = True

        #Prints the inventory of the chest each loop if its been opened and has items in it
        if chest_opened and len(chest_inventory) >= 1:
            print(f"{WHITE}chest contains: {BLUE}{chest_inventory}")
        #Room description
        print(f"\n{WHITE}You stand in a dusty stone room,")
        if has_torch:
            print(f"lit dimly by a {BLUE}torch {WHITE}beside a dark oak {BLUE}door{WHITE}.")
        else:
            print(f"across from a dark oak {BLUE}door{WHITE}.")
        print(f"In the center sits a lone wooden {BLUE}chest{WHITE}.")
        print(f"while on the wall, a wide {BLUE}crack{WHITE} stretches from floor to ceiling,")
        #runs a function that takes player input than sends to apropriate function in actions.py then updates and returns a new list of room variables
        var_list = library.take_input(player, 1, 1,var_list, var_keys)
        
