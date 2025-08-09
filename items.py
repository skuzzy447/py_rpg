class Item:
    def __init__(self, name, weight, equipable):
        self.name = name
        self.weight = weight
        self.equipable = equipable
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other

class Equipment(Item):
    def __init__(self, name, weight, slot):
        super().__init__(name, weight, True)
        self.condition = 1.0
        self.equiped = False
        self.slot = slot

class weapon(Equipment):
    def __init__(self, damage, name, weight):
        super().__init__(name, weight, 3)
        self.damage = damage
    def attack(self):
        pass
    def __str__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other

class Shortsword(weapon):
    def __init__(self, damage, name):
        super().__init__(damage, name, 1.0)
    
    def bonus_attack():
        self.attack()

class Key(Item):
    def __init__(self, unlocks, name):
        super().__init__(name, 0.1, False)
        self.unlocks = unlocks

class Torch(Equipment):
    def __init__(self):
        super().__init__("torch", 1.0, 4)