class weapon:
    def __init__(self, damage, condition, name):
        self.damage = damage
        self.condition = condition
        self.name = name
    def attack(self):
        pass
    def __str__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other

class Shortsword(weapon):
    def __init__(self, damage, condition, name):
        super().__init__(damage, condition, name)
    
    def bonus_attack():
        self.attack()
    