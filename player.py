class Player:
    def __init__(self, name, job, race, strength, dexterity, endurance, intelligence, skills):
        self.name = name
        self.job = job
        self.race = race

        self.strength = strength
        self.dexterity = dexterity
        self.endurance = endurance
        self.intelligence = intelligence
        self.skills = skills
        self.xp = 0
        self.level = 1
        self.armor = 0
        self.prof_bonus = 1

        self.in_combat = False

        self.inventory = []
        #0 = helmet, 1 = armor, 2 = boots, 3 = right hand, 4 = left hand
        self.equipment = ["none", "none", "none", "none", "none"]

    def describe(player):
        print(player.name, player.job, player.race, player.strength, player.dexterity, player.endurance, player.intelligence, player.skills)
    
    def skill_has_prof(player, skill):
        for each in range(0, len(player.skills)-1):
            new_skill = player.skills[each]
            has = False
            if skill == new_skill[0]:
                has = True
                return has
        return has
    
    def add_xp(self, xp):
        self.xp += xp
        if self.xp > 300:
            self.level = 2
        if self.xp > 900:
            self.level = 3
        if self.xp > 2700:
            self.level = 4
        if self.xp > 6500:
            self.level = 5
        if self.xp > 14000:
            self.level = 6
        if self.xp > 23000:
            self.level = 7
        if self.xp > 34000:
            self.level = 8
        if self.xp > 48000:
            self.level = 9
        if self.xp > 64000:
            self.level = 10
        if self.xp > 85000:
            self.level = 11
        if self.xp > 100000:
            self.level = 12
        if self.xp > 120000:
            self.level = 13
        if self.xp > 140000:
            self.level = 14
        if self.xp > 165000:
            self.level = 15
        if self.xp > 195000:
            self.level = 16
        if self.xp > 225000:
            self.level = 17
        if self.xp > 265000:
            self.level = 18
        if self.xp > 305000:
            self.level = 19
        if self.xp > 355000:
            self.level = 20