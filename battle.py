"""
RPG Battle System - Starter Code
Fill in the TODOs to complete the classes benchmark.
"""


class Character:
    def __init__(self, name, health, attack_power):
        #Character Info
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        
        #Character starts with no weapon
        self.weapon = None

    def is_alive(self):
        #Return true if character is alive
        return self.health > 0

    def take_damage(self, amount):
        #Damage subtracted from health
        self.health -= amount
        
        #Health can't go below 0
        if self.health < 0:
            self.health = 0

    def attack(self, other):
        #Attack a character
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
        other.take_damage(self.attack_power)

    def heal(self, amount):
        #Increase Health
        self.health += amount
        #Health can't go above max
        if self.health > self.max_health:
            self.health = self.max_health

    def equip(self, weapon):
        #Equip Weapon
        self.weapon = weapon
        #Increase Attack
        self.attack_power += weapon.bonus_damage

        print(f"{self.name} equpis {weapon.name} Attack power is now {self.attack_power}.")
class Weapon:
    def __init__(self, name, bonus_damage):
        #Weapon Info
        self.name = name
        self.bonus_damage = bonus_damage

class Battle:
    def __init__(self, fighter_one, fighter_two):
        #Fighters Info
        self.fighter_one = fighter_one
        self.fighter_two = fighter_two

        


    def run(self):
        #Fighter one attacks first
        attacker = self.fighter_one
        defender = self.fighter_two

        while attacker.is_alive() and defender.is_alive():

            attacker.attack(defender)

            if not defender.is_alive():
                print(f"{attacker.name} wins the battle!")
                break

            #Switch turns
            attacker, defender = defender, attacker


if __name__ == "__main__":
    
    #Characters
    hero = Character("Witcher", 100, 15)
    monster = Character("Werewolf", 90, 12)

    #Weapon
    sword = Weapon("Silver Sword", 8)

    #Equip the hero
    hero.equip(sword)

    #Battle Start
    battle = Battle(hero, monster)
    battle.run()