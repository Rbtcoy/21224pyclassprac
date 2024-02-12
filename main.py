from character import *
from weapon import *

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Villain", health=70, weapon=short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    hero.health_bar.draw()
    enemy.health_bar.draw()
    
    input()