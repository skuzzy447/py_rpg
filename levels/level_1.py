import os
import sys
path = os.path.abspath(os.getcwd())
sys.path.append(path)
#from actions import *
from library import *

def level_1_start(player, room):
    os.system('clear')
    while True:
        if room == 1:
            room = room_1(player)
        else:
            return

def room_1(player):
    var_list = [["chest_opened", False],["rat_killed", False],["door_unlocked", False], ["chest_inventory", ["L1R1_Key", "shortsword"]]]
    while True:
        var_keys = return_list_values(var_list)
        chest_opened = var_keys[0]
        rat_killed = var_keys[1]
        door_unlocked = var_keys[2]
        chest_inventory = var_keys[3]
        if chest_opened:
            print(f"chest contains: {chest_inventory}")
        print("\nYou stand in a dusty stone room lit dimly by your torch.") 
        print("In the center sits a lone wooden chest.")
        print("A dark oak door rests on one side,")
        print("while on the opposite wall, a wide crack stretches from floor to ceiling,")
        #print(var_list)
        var_list = take_input(player, 1, 1,var_list, var_keys)
        
