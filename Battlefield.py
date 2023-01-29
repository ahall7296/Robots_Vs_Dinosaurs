from Dinosaur import Dinosaur
from Robot import Robot
from Weapon import Weapon

class Battlefield:
    def __init__ (self):
        self.dinosaur = Dinosaur("Gargantuis", 20)
        self.weapon = Weapon("Gun", 20)
        self.robot = Robot("Alexios", Weapon, 100)

    def attack_robot(self):
        print(self.robot.health)
        self.robot.health -= self.dinosaur.attack_power
        print(self.robot.health)
        
    def attack_dinosaur(self):
        print(self.dinosaur.health)
        self.dinosaur.health -= self.robot.weapon.attack_power
        print(self.dinosaur.health)

    def battle (self):
        self.robot_attacks = 0
        self.dinosaur_attacks = 0    
        while self.dinosaur.health and self.robot.health > 0:
            self.robot.health -= self.dinosaur.attack_power
            self.dinosaur_attacks +=1
            print("Gargantuis attacked Alexios")
            self.dinosaur.health -= self.robot.weapon.attack_power
            self.dinosaur.health -= self.robot.weapon.attack_power
            print("Alexios attacked Gargantuis")
            self.robot_attacks +=2
            print(self.robot_attacks)
            print(self.dinosaur_attacks)

            if self.dinosaur.health == 0:
                print(f"Alexios won, remaining health is {self.robot.health}")
            elif self.robot.health == 0:
                print(f"Gargantuis won, remaining health is {self.dinosaur.health}")