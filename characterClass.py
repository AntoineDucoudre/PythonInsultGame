class Personality:

    def __init__(self, name, hp, weakness, strength, luck):
        self.name = name
        self.hp = hp
        self.weakness = weakness
        self.strength = strength
        self.luck = luck

    def __str__(self):
        return self.name