import player_stats
import os

os.system('clear')
name = ""
strength = 10
dexterity = 10
endurance = 10
intelligence = 10

def main():
    race = create_race()
    job = create_job()
    skills = create_skills()

    player = player_stats.Player(name, job, race, strength, dexterity, endurance, intelligence, skills)
    player.describe()


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
            loop2()
        if to_add1 == to_add2:
            os.system('clear')
            print("cant be the same as first pick")
        else:
            done = True
    os.system('clear')

    new_list = []
    for each in range(0, len(skills)):
        skill_string = skills[each]
        if skill_string[0] == to_add1 or skill_string[0] == to_add2:
            new_list.append([skill_string[0], True])
        else:
            new_list.append([skill_string[0], False])
    return new_list


main()
