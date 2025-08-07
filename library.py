from actions import *
import os
#Takes player input and sends to appropriate function in actions.py
def take_input(player, level, room, var_list, keys):
    return_list = var_list
    print("")
    print(f"{WHITE}what do you do?\n")
    response = input(">:").lower()
    #Checks if input is exactly 2 words and if not sends error message to player
    words = response.split()
    if len(words) > 2 or len(words) < 2:
        message("Improper command. Every comand should be exactly 2 words")
        return return_list
    else:
        #sends to take() item
        if words[0] == "take" or words[0] == "grab" or words[0] == "pickup":
            container, inventory = "", []
            container, inventory = take(player, 1, 1, keys, words[1])
            for each in return_list:
                if each[0] == container:
                    each[1] = inventory
        #sends to open() container
        elif words[0] == "open":
            return_list = open(player, 1, 1, keys, words[1], var_list)
        #sends to show() UI    
        elif words[0] == "show":
            show(player, words[1])
        elif words[0] == "equip":
            equip(player, words[1])
        else:
            message(f"No command named: {RED}{words[0]}")
    #updates room variables
    return return_list

def return_list_values(var_list):
    keys = []
    for each in var_list:
        keys.append(each[1])
    return keys

def message(message):
    os.system('clear')
    print(message)
    input("")
    os.system('clear')