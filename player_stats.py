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