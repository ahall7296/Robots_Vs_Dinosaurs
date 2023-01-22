class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = "Gargantuis"
        self.health = 100
        self.attack_power = 20

    def attack(self, robot):
        robot.health = robot.health - self.attack_power
        pass