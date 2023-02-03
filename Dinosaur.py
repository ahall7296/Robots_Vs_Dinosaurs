class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack_robot(self, robot):
        if self.health > 0:
            robot.health -= self.attack_power
            print(f"{self.name} attacked {robot.name}, HEALTH: {robot.health}")
        