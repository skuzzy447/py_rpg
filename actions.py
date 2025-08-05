import os
import sys
levels_path = os.path.abspath("./levels")
sys.path.append(levels_path)
from level_1 import *

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
                    player.inventory.append("shortsword")
                    chest_inventory.remove("shortsword")
                    container, container_inventory = "chest_inventory", chest_inventory
    return(container, container_inventory)