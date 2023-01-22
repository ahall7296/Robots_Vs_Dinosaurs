from Weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = "Alexios"
        self.health = 100
        self.active_weapon = "Spear_of_Leonidas"

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.active_weapon.attack_power
        pass