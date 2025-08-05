import os
def main_menu():
    os.system('clear')
    while True:
        print("-----------------Main Menu----------------- \n")
        print("     ____            ____  ____   ____ ")
        print("    |  _ \ _   _    |  _ \|  _ \ / ___|")
        print("    | |_) | | | |   | |_) | |_) | |  _ ")
        print("    |  __/| |_| |   |  _ <|  __/| |_| |")
        print("    |_|    \__, |___|_| \_\_|    \____|")
        print("           |___/_____|                 \n")
        print("---1: New Game---2: Continue---3:Options--- \n")
        response = input(":")
        if response == "1":
            os.system('clear')
            return "new"
        elif response == "2":
            pass
        elif response == "3":
            pass
        else:
            os.system('clear')
            print("Incompatable Response")
