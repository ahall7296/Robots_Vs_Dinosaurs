from Dinosaur import Dinosaur
from Robot import Robot
from Weapon import Weapon
class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Gargantuis", 100)
        self.robot = Robot("Alexios")
        pass
    
    def run_game(self):
        self.battle_phase()
        pass

    def battle_phase(self):
        while self.dinosaur.health> 0 and self.robot.health> 0:
            self.dinosaur.attack(self.robot)
            print(f"\n{self.dinosaur.name} attacks {self.robot.name} for {self.dinosaur.attack_power} damage! \n {self.robot.name} has {self.robot.health} health remaining!")
            if self.robot.health> 0:
                self.robot.attack(self.dinosaur)
                print(f"\n{self.robot.name} attacks {self.dinosaur.name} for {self.robot.active_weapon.attack_power} damage! \n {self.dinosaur.name} has {self.dinosaur.health} health remaining!")
        if self.dinosaur.health<= 0:
            self.winner= self.robot.name
            self.loser= self.dinosaur.name
            print(f"{self.winner} Anihilated {self.loser}")
        else:
            self.winner= self.dinosaur.name
            self.loser= self.robot.name
            print(f"{self.winner} Anihilated {self.loser}")
        pass