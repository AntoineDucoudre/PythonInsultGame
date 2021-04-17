from characterClass import Personality

class Characters:
    def __init__(self, name):
        if name == "Lucas":
            self.name = "Lucas"
            self.hp = 100
            self.weakness = 12
            self.strength = 5
            self.luck = 2
        elif name == "Peter":
            self.name = "Peter"
            self.hp = 100
            self.weakness = 9
            self.strength = 7
            self.luck = 1
        elif name == "Itachi":
            self.name = "Itachi"
            self.hp = 100
            self.weakness = 12
            self.strength = 6
            self.luck = 2
        elif name == "Max":
            self.name = "Max"
            self.hp = 100
            self.weakness = 10
            self.strength = 8
            self.luck = 1
        elif name == "Sarah":
            self.name = "Sarah"
            self.hp = 100
            self.weakness = 8
            self.strength = 10
            self.luck = 2
    
    def __str__(self):
        return self.name
