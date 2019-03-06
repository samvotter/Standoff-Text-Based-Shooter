# libraries
import random
import copy


class Character:

    def __init__(self, last, health, armor, shields):
        # Player Stats
        with open('FirstNameAdjectives.txt', 'r') as a:
            fnames = a.read().splitlines()
        self.first = fnames[random.randint(0, len(fnames))]
        self.last = last
        self.health = health
        self.armor = armor
        self.shields = shields
        self.wait = 0

        self.maxhp = 100
        self.avoidance = 0
        self.bleed = 0
        self.alive = True
        self.upgrades = []
        self.upgrade_dict = {}

        # Gun Stats
        self.accuracy = 60
        self.damage = 35
        self.ammo = 6
        self.bleed_dmg = 1

        # Identifier
        self.side = ""
        self.target = None

    # Player Getters
    def get_name(self):
        return self.first + " " + self.last

    def get_alive(self):
        if self.health > 0:
            self.alive = True
        else:
            self.health = 0
            self.alive = False
        return self.alive

    def choose_upgrade(self):
        print(self.get_name(), "upgrades:")
        i = 1
        for option in self.upgrades:
            print(str(i)+". ", option)
            i += 1
        choice = 0
        while choice < 1 or choice > len(self.upgrades):
            choice = int(input("Pick an upgrade by typing the number"))
        chosen = copy.deepcopy(self.upgrades[choice-1])
        self.upgrades.remove(self.upgrades[choice-1])
        return chosen

    def apply_upgrade(self, choice, gamestate):
        pass

    def lower_armor(self, amount):
        if amount < 0:
            amount = -amount
        if amount > self.armor:
            self.armor = 0
            return True
        else:
            self.armor -= amount
        return True

    def take_damage(self, result):
        if result[2] is None:
            print(self.get_name(), "took no damage.")
            return False
        else:
            if result[1] == "Chest":
                damage = result[2]
            elif result[1] == "Arms":
                damage = result[2]*(3 / 5)
                self.accuracy *= (9 / 10)
            elif result[1] == "Hands":
                damage = result[2] * (1 / 5)
                self.accuracy /= 2
            elif result[1] == "Legs":
                damage = result[2] * (3 / 5)
            elif result[1] == "Feet":
                damage = result[2] * (1 / 5)
            elif result[1] == "Head":
                damage = result[2] * 2
            else:
                damage = result[2]
            # if the target is alive . . .
            reduce = damage
            if self.alive is True:
                # and they have shields . . .
                if self.shields > 0:
                    # shields reduce incoming damage by a percentage.
                    damage *= (100-self.shields)/100
                    self.shields -= reduce
                    if self.shields < 0:
                        self.shields = 0
                # and if they have armor
                if self.armor > 0:
                    # armor reduces incoming damage by a flat amount.
                    damage -= self.armor
                # and not all of it was blocked
                if damage > 0:
                    self.health -= damage
                    self.bleed += result[3]
                    print(result[0].get_name(), "was hit in the", result[1], "for", damage)
                    return True
                else:
                    print(self.get_name(), "All damage was blocked!")
                    return False
            # if the target is dead
            else:
                print(self.get_name(), "was dead.")
                return False

    def bleeds(self):
        # if the target is alive . . .
        if self.alive is True:
            # and bleeding . . .
            if self.bleed > 0:
                # then they take damage
                self.health -= self.bleed
                return True
            else:
                return False
        else:
            return False

    def heal(self, heal):
        # target recieves some amount of healing
        if self.health + heal > self.maxhp:
            self.health = self.maxhp
            return True
        else:
            self.health += heal
            return True

    def change_accuracy(self, symbol, amount):
        if symbol == "+":
            self.accuracy += amount
        else:
            self.accuracy *= amount
        if self.accuracy >= 100:
            self.accuracy = 100
        elif self.accuracy <= 0:
            self.accuracy = 0

    # Gun Functions
    def fire(self):
        # is there ammo to fire
        if self.ammo > 0:
            # fire!
            self.ammo -= 1
            return True
        else:
            return False

    def hits(self, victim):
        # do you hit?
        if random.randint(0, 100) <= self.accuracy - victim.avoidance:
            return True
        # if not then miss
        else:
            return False

    def pick_bodypart(self):
        roll = random.randint(1, 6)
        if roll == 1:
            return "Chest"
        elif roll == 2:
            return "Arms"
        elif roll == 3:
            return "Hands"
        elif roll == 4:
            return "Legs"
        elif roll == 5:
            return "Feet"
        elif roll == 6:
            return "Head"
        else:
            "ERROR - could not pick a body part."

    # Meta function serving as the default attack sequence
    def attack(self, victim):
        result = []
        if self.wait > 0:
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            return result
        # if fire returns true
        if self.fire() is True:
            print('*BANG!*', end='')
            if self.hits(victim) is True:
                print("- The shot hit!")
                result.append([self.target, self.pick_bodypart(), self.damage, self.bleed_dmg])
                return result
            else:
                result.append([self.target, "Miss"])
                print("- The shot missed!")
                return result
        else:
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            return result

    def before_combat(self, gamestate):
        return gamestate

    def after_combat(self, gamestate):
        return gamestate

    def turn_start(self, gamestate):
        return gamestate

    # Game Functions

    def set_target(self,side):
        i = 1
        for character in side:
            print(i, end=' ')
            print(character.get_name())
            i += 1
        choice = -1
        while choice > len(side) or choice < 0:
            choice = int(input("Type the number of the character you wish to attack."))
        self.target = side[choice-1]

    def set_side(self, side):
        self.side = side

