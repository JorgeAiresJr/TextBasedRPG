import sys
import os
import random
import pickle

weapons = {"Great Sword": 40}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.luck = 1
        self.gold = 50;
        self.pots = 0;
        self.weap = ["Rust Sword"]
        self.curweap = ["Rust Sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 5
        if self.curweap == "Great Sword":
            attack += 15

        return attack

class Goblin:
          
     def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10;

class Zombie:
          
     def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 15;

def main():
          
    print("----------------------------------------------------------------------------")
    print("                       Welcome to the Old World")
    print("----------------------------------------------------------------------------")
    print("1) Start")
    print("2) Load")
    print("3) Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        load()
    elif option == "3":
        sys.exit()
    else:
        main()

def inventory():
          
    print("What do you want to do")
    print("1) Equip Weapon")
    print("b) Back")
    option = input("-> ")
    if option == "1":
        equip()
    elif option == "Back" or option == "b":
        startGame()
    else:
        main()

def equip():

    print("What do you want to equip")
    for weapon in PlayerIG.weap:
        print(weapon)
    print("b) Back")         
    option = input("-> ")
    if option == PlayerIG.curweap:
       print("You already have that weapon equipped")
       option = input(" ")
       equip()
    elif option == "Back" or option == "b":
        inventory()
    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print("You have equipped %s." % option)
        option = input(" ")
        equip()
    else:
        print("You don't have %s in your inventory" % option)
        option = input(" ")
        equip()

def start():
          
    print("Hello, what is your name?")
    option = input("-> ")
    global PlayerIG
    PlayerIG = Player(option)
    startGame()

def startGame():

    print("----------------------------------------------------------------------------")
    print("                                 Status")
    print("----------------------------------------------------------------------------")    
    print("Name: %s" % PlayerIG.name)
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Attack: %i" % PlayerIG.attack)
    print("Luck: %i" % PlayerIG.luck)
    print("Gold: %d" % PlayerIG.gold)
    print("Current Weapon: %s" % PlayerIG.curweap)
    print("Potions: %i" % PlayerIG.pots)     
    print("----------------------------------------------------------------------------")
    print("                                 Actions")
    print("----------------------------------------------------------------------------") 
    print("1) Fight")
    print("2) Inventory")
    print("3) Store")
    print("4) Save")
    print("5) Exit")
    option = input("-> ")
    if option == "1":
        prefight()
    elif option == "2":
        inventory()
    elif option == "3":
        store()
    elif option == "4":
        save()
    elif option == "5":
        sys.exit()
    else:
        startGame()

def save():

    with open("savefile", "wb") as f:
        pickle.dump(PlayerIG, f)
        print("Game has been saved")
    option = input(" ")
    startGame()

def load():
    if os.path.exists("savefile") == True:
 
        with open("savefile", "rb") as f:
            global PlayerIG
            PlayerIG = pickle.load(f)
        print("Loaded Save State...")
        option = input(" ")
        startGame()
    else:
        print("You have no save file for this game.")
        option = input(" ")
        main()

def prefight():
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = Goblin("Goblin")
    else:
        enemy = Zombie("Zombie")
    fight()


def fight():

    print("----------------------------------------------------------------------------")
    print("                               %s     vs    %s" % (PlayerIG.name, enemy.name))
    print("----------------------------------------------------------------------------")
    print("%s's Health: %d/%d %s's Health: %i/%i" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print("Potions: %i" % PlayerIG.pots)
    print("1) Attack")
    print("2) Drink Potion")
    print("3) Run")
    option = input("-> ")
    if option == "1":
        attack()
    elif option == "2":
        drinkPot()
    elif option == "3":
        run()
    elif option == "4":
        sys.exit()
    else:
        fight()

def attack():

    PAttack = random.uniform(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.uniform(enemy.attack / 2, enemy.attack)
    if PAttack == PlayerIG.attack / 2:
        print("You miss!");
    else:
        enemy.health -= PAttack
        print("You deal %i damage!" % PAttack)
    option = input(" ")
    if enemy.health <= 0:
        win();

    if EAttack == enemy.attack/2:
        print("Enemy miss!");
    else:
        PlayerIG.health -= EAttack
        print("The enemy deals %i damage!" % EAttack)
    option = input(" ")
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()

def drinkPot():

    if PlayerIG.pots == 0:
        print("You don't have any potions!")
    else:
        PlayerIG.health += 50
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print("You drunk a potion!")
    option = input(" ")
    fight()              

def run():

    runnum = random.randint(1, 3)
    if runnum == 1:
       print("You have successfully ran away!")       
       option = input(" ")
       startGame()
    else:
        print("You failed to get away!")
        option = input(" ")
        cls()

        EAttack = random.uniform(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack/2:
            print("Enemy miss!");
        else:
            PlayerIG.health -= EAttack
            print("The enemy deals %i damage!" % EAttack)
        option = input(" ")
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()
              
def win():

    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldgain
    print("You have defeated the %s" % enemy.name)
    print("You found %i gold!" % enemy.goldgain)          
    option = input(" ")
    startGame()
              
def dead():

    print("You have died")
    option = input(" ")
    start()
              
def store():

    print("----------------------------------------------------------------------------")
    print("                       Welcome to the shop!")
    print("                      You have %i golds!" % PlayerIG.gold)
    print("----------------------------------------------------------------------------")     
    print("What would you live to buy?")
    print("1) Great Sword: %i golds" % weapons["Great Sword"])
    print("b) Back")
    option = input(" ")

    if option in weapons:
        if PlayerIG.gold >= weapons[option]:

            print("You have bought %s" % option)
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            option = input(" ")
            store()
        else:

            print("You don't have enough gold!")
            option = input(" ")
            store()
    elif option == "Back" or option == "b":
        startGame()
    else:

        print("That item does not exist")
        option = input(" ")
        store()

    
main()
