import os
from constants import *
from library import *

def main_menu():
    os.system('clear')
    while True:
        print(f"{WHITE}-----------------{BLUE}Main Menu{WHITE}----------------- \n")
        print(f"{RED}     ____            ____  ____   ____ ")
        print(f"{RED}    |  _ \ _   _    |  _ \|  _ \ / ___|")
        print(f"{RED}    | |_) | | | |   | |_) | |_) | |  _ ")
        print(f"{RED}    |  __/| |_| |   |  _ <|  __/| |_| |")
        print(f"{RED}    |_|    \__, |___|_| \_\_|    \____|")
        print(f"{RED}           |___/_____|                 \n")
        print(f"{WHITE}---{GREEN}1: {BLUE}New Game{WHITE}---{GREEN}2: {BLUE}Continue{WHITE}---{GREEN}3: {BLUE}Options{WHITE}--- \n")
        response = input(f"{WHITE}>:")
        if response == "1":
            os.system('clear')
            return "new"
        elif response == "2":
            pass
        elif response == "3":
            pass
        else:
            message("Incompatible response")
