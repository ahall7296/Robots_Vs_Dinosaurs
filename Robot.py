from Weapon import Weapon
class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon("Gun", 20)

    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacked {dinosaur.name}, HEALTH: {dinosaur.health}")