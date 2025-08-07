import os
import sys
levels_path = os.path.abspath("./levels")
sys.path.append(levels_path)
from level_1 import *
from items import *
import library
from constants import *
#Takes an object from a container and adds it to the players inventory
def take(player, level, room, keys, item):
    container, container_inventory = "", []
    found = False
    #Finds player location
    if level == 1:
        if room == 1:
            #Room Variables
            chest_opened = keys[0]
            rat_killed = keys[1]
            door_unlocked = keys[2]
            chest_inventory = keys[3]
            #If the container is opened and the second typed word is the same as an object it contains than it adds the object to the players inventory
            if chest_opened:
                has_sword = False
                has_key = False
                for each in chest_inventory:
                        if str(each) == "shortsword":
                            has_sword = True
                        if str(each) == "L1R1_Key":
                            has_key = True
                if (item == "shortsword" or item == "sword") and has_sword:
                    found = True
                    shortsword = Shortsword("1 d6", "shortsword")
                    player.inventory.append(shortsword)
                    chest_inventory.remove("shortsword")
                    container, container_inventory = "chest_inventory", chest_inventory
                    library.message("took shortsword")
                elif (item == "l1r1_key" or item == "key") and has_key:
                    found = True
                    L1R1_key = Key("L1R1_Door", f"{GREEN}L1R1_Key")
                    player.inventory.append(L1R1_key)
                    chest_inventory.remove("L1R1_Key")
                    container, container_inventory = "chest_inventory", chest_inventory
                    library.message("took L1R1_key")
    if not found:
        if item == "chest" or item == "door" or item == "wall" or item == "ground" or item == "floor" or item == "crack" or item == "ceiling" or item == "roof":
            library.message(f"{WHITE}Cannot pick up: {RED}{item}")
        else:
            library.message(f"{WHITE}Could not find: {RED}{item}")
    return(container, container_inventory)
#Opens a container
def open(player, level, room, keys, container, var_list):
    return_list = var_list
    #Finds player location
    if level == 1:
        if room == 1:
            #Room variables
            chest_opened = keys[0]
            rat_killed = keys[1]
            door_unlocked = keys[2]
            chest_inventory = keys[3]
            #If the second typed word is the same as a container in the room than open the container. always returns true in the case but has a different message
            found = False
            if container == "chest":
                if chest_opened:
                    library.message("chest already open")
                else:
                    library.message("chest opened")
                found = True
                for each in return_list:              
                    if each[0] == "chest_opened":
                        each[1] = True                
                return return_list
            elif container == "door":
                pass
            if not found:
                if container == "sword" or container == "shortsword" or container == "key" or container == "l1r1_key" or container == "torch" or container == "crack" or container == "wall" or container == "ground" or container == "floor":
                    library.message(f"{WHITE}Cannot open: {RED}{container}")
                library.message(f"{WHITE}Could not find: {RED}{container}")
                return var_list 
#Shows UI element ie. Inventory, Stats
def show(player, menu):
    return_string = ""
    #prints the name of each object in players inventory on a new line
    if menu == "inv" or menu == "inventory" or menu == "i":
        for each in range(0,len(player.inventory)):
            item = player.inventory[each]
            equiped = False
            if item.equipable:
                equiped = item.equiped
            return_string += f"{RED}{each + 1} {WHITE}| {BLUE}{str(item)}{WHITE} | {GREEN}{equiped}\n"
        library.message(f"Slot | Name | Equiped \n{return_string}")
    elif menu == "equip" or menu == "equipment" or menu == "e":
        for each in range(0, len(player.equipment)):
            slot = ""
            if each == 0:
                slot = "Helmet"
            if each == 1:
                slot = "Armor"
            if each == 2:
                slot = "Boots"
            if each == 3:
                slot = "Right Hand"
            if each == 4:
                slot = "Left Hand"
            return_string += f"{RED}{slot} | {BLUE}{player.equipment[each]}\n"
        library.message(f"Slot | Name\n{return_string}")
    else:
        library.message(f"{WHITE}No menu named: {RED}{menu}")

def equip(player, item):
    found = False
    for each in player.inventory:
        if str(each) == item:
            if each.equipable and not each.equiped:
                each.equiped = True
                player.equipment[each.slot] = each
                found = True
                library.message(f"{WHITE}Equiped: {BLUE}Shortsword")
    if not found:
        library.message(f"{WHITE}Cannot equip: {RED}{item}")