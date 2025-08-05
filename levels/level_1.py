import os
import sys
path = os.path.abspath(os.getcwd())
sys.path.append(path)
from actions import *
from items import *
from library import *

def level_1_start(player, room):
    while True:
        if room == 1:
            room = room_1(player)
        else:
            return

def room_1(player):
    var_list = [["chest_opened", False],["rat_killed", False],["door_unlocked", False], ["chest_inventory", ["L1R1 Door Key", "shortsword"]]]
    while True:
        var_keys = return_list_values(var_list)
        #os.system('clear')
        print("You enter a dusty stone room lit dimly by your torch.") 
        print("In the center sits a lone wooden chest.")
        print("A heavy oak door rests on one side,")
        print("while on the opposite wall, a narrow crack stretches from floor to ceiling,")
        response = take_input()
        if response[0] == "take":
            container, inventory = "", []
            container, inventory = take(player, 1, 1, var_keys, response[1])
            for each in var_list:
                if each[0] == container:
                    print(each)
                    each[1] = inventory
                    print(each)
