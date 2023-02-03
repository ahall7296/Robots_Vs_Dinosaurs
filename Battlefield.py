from Dinosaur import Dinosaur
from Robot import Robot
from Weapon import Weapon

class Battlefield:
    def __init__ (self):
        self.dinosaur = Dinosaur("Gargantuis", 20)
        self.robot = Robot("Alexios", 100)

    def battle (self):
  
        while self.dinosaur.health and self.robot.health > 0:
            self.dinosaur.attack_robot(self.robot)
            self.robot.attack_dinosaur(self.dinosaur)
            if self.dinosaur.health == 0:
                print(f"Alexios won, remaining health is {self.robot.health}")
            elif self.robot.health == 0:
                print(f"Gargantuis won, remaining health is {self.dinosaur.health}")