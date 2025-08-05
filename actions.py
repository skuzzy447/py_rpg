import os
import sys
levels_path = os.path.abspath("./levels")
sys.path.append(levels_path)
from level_1 import *
from items import *
import library

def take(player, level, room, keys, item):
    container, container_inventory = "", []
    if level == 1:
        if room == 1:
            chest_opened = keys[0]
            rat_killed = keys[1]
            door_unlocked = keys[2]
            chest_inventory = keys[3]
            #print(chest_opened, rat_killed, door_unlocked, chest_inventory)
            if chest_opened:
                if item == "shortsword":
                    shortsword = Shortsword("1 d6", 1.0, "shortsword")
                    player.inventory.append(shortsword)
                    chest_inventory.remove("shortsword")
                    container, container_inventory = "chest_inventory", chest_inventory
                    library.message("took shortsword")
                if item == "l1r1_key":
                    L1R1_key = Key("L1R1_Door", "L1R1_key")
                    player.inventory.append(L1R1_key)
                    chest_inventory.remove("L1R1_Key")
                    container, container_inventory = "chest_inventory", chest_inventory
                    library.message("took L1R1_key")
    return(container, container_inventory)

def open(player, level, room, keys, container):
    if level == 1:
        if room == 1:
            chest_opened = keys[0]
            rat_killed = keys[1]
            door_unlocked = keys[2]
            chest_inventory = keys[3]
            if container == "chest":
                if chest_opened:
                    library.message("chest already open")
                else:
                    library.message("chest opened")                
                return ["chest_opened", True]

def show_inventory(player):
    pass