import random

class Weapon:
    def __init__(self, name: str, weapon_type: str, max_damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.max_damage = max_damage
        self.value = value
        
iron_sword = Weapon(name="Iron Sword",
                    weapon_type="sharp",
                    max_damage=5,
                    value=10)

short_bow = Weapon(name="Short Bow",
                   weapon_type="ranged",
                   max_damage=3,
                   value=8)

fists = Weapon(name="Fists",
               weapon_type="blunt",
               max_damage=2,
               value=0)