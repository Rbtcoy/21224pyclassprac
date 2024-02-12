from weapon import fists
from healthbar import HealthBar
import random

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists
        
    def attack(self, target) -> None:
        attack_roll = random.randint(1,self.weapon.max_damage)
        target.health -= attack_roll
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {attack_roll} damage to {target.name} with {self.weapon.name}")
        
class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")
        
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} has equipped a(n) {self.weapon.name}!")
        
    def drop(self)-> None:
        self.weapon = self.default_weapon
        print(f"{self.name} dropped the {self.weapon}")

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name, health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")