class Item:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other

class weapon(Item):
    def __init__(self, damage, condition, name):
        super().__init__(name)
        self.damage = damage
        self.condition = condition
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

class Key(Item):
    def __init__(self, unlocks, name):
        super().__init__(name)
        self.unlocks = unlocks
    
