import player_stats
import os

os.system('clear')

def new_character():
    race = create_race()
    job = create_job()
    skills = create_skills()
    strength, dexterity, endurance, intelligence = create_attributes()
    name = create_name()
    player = player_stats.Player(name, job, race, strength, dexterity, endurance, intelligence, skills)
    return player

def create_race():
    done = False
    while not done:
        print("what race are you? \n")
        print("1 = Human")
        print("2 = Elf")
        print("3 = Dwarf \n")
        response = input(":")
        done = True
        if response == "1":
            race = "human"
        elif response == "2":
            race = "elf"
        elif response == "3":
            race = "dwarf"
        else:
            os.system('clear')
            print("Incompatible response \n")
            done = False
    os.system('clear')
    return race

def create_job():
    done = False
    while not done:
        done = True
        print("what class are you? \n")
        print("1 = warrior")
        print("2 = rogue")
        print("3 = warlock")
        response = input(":")
        if response == "1":
            job = "warrior"
        elif response == "2":
            job = "rogue"
        elif response == "3":
            job = "warlock"
        else:
            os.system('clear')
            print("incompatible response")
            done = False   
    os.system('clear')
    return job

def create_skills():
    done1 = False
    to_add1 = ""
    done2 = False
    to_add2 = ""
    skills = [["arcana" , False], ["athletics" , False], ["investigation" , False], ["medicine" , False], ["stealth" , False]]


    while not done1:
        print("pick proficient skill 1/2 \n")
        print("1 = arcana")
        print("2 = athletics")
        print("3 = investigation")
        print("4 = medicine")
        print("5 = stealth")
        response = input(":")
        done1 = True
        if response == "1":
            to_add1 = "arcana"
        elif response == "2":
            to_add1 = "athletics"
        elif response == "3":
            to_add1 = "investigation"
        elif response == "4":
            to_add1 = "medicine"
        elif response == "5":
            to_add1 = "stealth"
        else:
            os.system('clear')
            print("incompatible response")
            done1 = False
    os.system('clear')

    while not done2:
        done2 = True
        print("pick proficient skill 2/2 \n")
        print("1 = arcana")
        print("2 = athletics")
        print("3 = investigation")
        print("4 = medicine")
        print("5 = stealth")

        response = input(":")
        
        if response == "1":
            to_add2 = "arcana"
        elif response == "2":
            to_add2 = "athletics"
        elif response == "3":
            to_add2 = "investigation"
        elif response == "4":
            to_add2 = "medicine"
        elif response == "5":
            to_add2 = "stealth"
        else:
            os.system('clear')
            print("incompatible response")
            done2 = False
        if to_add1 == to_add2:
            os.system('clear')
            print("cant be the same as first pick")
            done2 = False
        else:
            done2 = True
    os.system('clear')

    new_list = []
    for each in range(0, len(skills)):
        skill_string = skills[each]
        if skill_string[0] == to_add1 or skill_string[0] == to_add2:
            new_list.append([skill_string[0], True])
        else:
            new_list.append([skill_string[0], False])
    return new_list

def create_attributes():
    strength = 8
    dexterity = 8
    endurance = 8
    intelligence = 8
    done = False
    points = 12
    #while not done:
    def point_board():
        print(f"you have {points} points to distribute \n")
        print(f"strength = {strength}")
        print(f"dexterity = {dexterity}")
        print(f"endurance = {endurance}")
        print(f"intelligence = {intelligence} \n")
    current_attribute = "strength"
    done = False
    while not done:
        for each in range(0,4):
            os.system('clear')
            point_board()
            if each == 0:
                current_attribute = "strength"
            elif each == 1:
                current_attribute = "dexterity"
            elif each == 2:
                current_attribute = "endurance"
            elif each == 3:
                current_attribute = "intelligence"
            done2 = False
            while not done2:
                def too_low():
                    os.system('clear')
                    point_board()
                    print(f"{current_attribute} cannot be lower than 8")
                done2 = True
                print(f"how many points would you like to add to {current_attribute}?")
                response = input(":")
                int_response = int(response)
                if int_response > points:
                    os.system('clear')
                    point_board()
                    print("not enough points")
                    done2 = False
                elif current_attribute == "strength":
                    if strength + int_response < 8:
                        too_low()
                        done2 = False
                    else:
                        strength += int_response
                        points -= int_response
                elif current_attribute == "dexterity":
                    if dexterity + int_response < 8:
                        too_low()
                        done2 = False
                    else:
                        dexterity += int_response
                        points -= int_response
                elif current_attribute == "endurance":
                    if endurance + int_response < 8:
                        too_low()
                        done2 = False
                    else:
                        endurance += int_response
                        points -= int_response
                elif current_attribute == "intelligence":
                    if intelligence + int_response < 8:
                        too_low()
                        done2 = False
                    else:
                        intelligence += int_response
                        points -= int_response
        if points == 0:
            done = True
    os.system('clear')
    return strength, dexterity, endurance, intelligence

def create_name():
    print("what is your name? \n")
    response = input(':')
    os.system('clear')
    return response
