from Dinosaur import Dinosaur
from Robot import Robot
class Battlefield:
    def __init__ (self):
        self.dinosaur = Dinosaur("Gargantuis")
        pass

    def __init__(self):
        self.robot = Robot("Alexios")
        pass
    
    def run_game(self):
        self.battle_phase()
        self.display_winner()
        pass

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            print(f"\nLet the Games Begin! Dinosaur Health: {self.dinosaur.health} Robot Health: {self.robot.health}")
            self.dinosaur.attack(self.robot)
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
        pass

    def display_winner(self):
        if self.dinosaur.health > 0:
            print(f"{self.dinosaur.name} is the Winner of the Battlefield!")
        elif self.robot.health > 0:
            print(f"{self.robot.name} is the winner of the Battlefield!")
        pass