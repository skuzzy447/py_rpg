from actions import *
import os

def take_input(player, level, room, var_list, keys):
    return_list = var_list
    print("")
    print("what do you do?")
    response = input(":").lower()
    words = response.split()
    if len(words) > 2 or len(words) < 2:
        return "error"
    else:
        if words[0] == "take":
            container, inventory = "", []
            container, inventory = take(player, 1, 1, keys, words[1])
            for each in return_list:
                if each[0] == container:
                    each[1] = inventory
        elif words[0] == "open":
            opened = []
            opened = open(player, 1, 1, keys, words[1])
            for each in return_list:              
                if each[0] == opened[0]:
                    each[1] = opened[1]
                    
    return return_list

def return_list_values(var_list):
    keys = []
    for each in var_list:
        keys.append(each[1])
    return keys

def message(message):
    os.system('clear')
    print(message)
    input(":")
    os.system('clear')