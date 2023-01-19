class Robot:
    def __init__(self):
        self.name = "Alexios"
        self.health = 100
        self.active_weapon = "Spear_of_Leonidas"

    def attack (self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        pass