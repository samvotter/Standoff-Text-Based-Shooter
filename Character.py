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
        self.target = 0
        self.strike = False
        self.accuracy = 60
        self.damage = 35
        self.ammo = 6
        self.bleed_dmg = 1

        # Identifier
        self.id = 0
        self.side = ""

    # Player Getters
    def get_name(self):
        return self.first + " " + self.last

    def get_health(self):
        return self.health

    def get_armor(self):
        return self.armor

    def get_shields(self):
        return self.shields

    def get_wait(self):
        return self.wait

    def get_maxhp(self):
        return self.maxhp

    def get_avoidance(self):
        return self.avoidance

    def get_bleed(self):
        return self.bleed

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

    def change_bleed(self, amount):
        self.bleed += amount

    def take_damage(self, damage):
        # if the target is alive . . .
        if self.alive is True:
            # and they have shields . . .
            if self.shields > 0:
                # shields reduce incoming damage by a percentage.
                damage *= self.shields/100
                self.shields -= damage
                if self.shields < 0:
                    self.shields = 0
            # and if they have armor
            if self.armor > 0:
                # armor reduces incoming damage by a flat amount.
                damage -= self.armor
            # and not all of it was blocked
            if damage > 0:
                self.health -= damage
                return True
            else:
                return False
        # if the target is dead
        else:
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

    # Gun Getters
    def get_strike(self):
        return self.strike

    def get_accuracy(self):
        return self.accuracy

    def get_damage(self):
        return self.damage

    def get_ammo(self):
        return self.ammo

    def get_bleed_dmg(self):
        return self.bleed_dmg

    def get_target(self):
        return self.target

    def change_accuracy(self, symbol, amount):
        if symbol == "+":
            self.accuracy += amount
        else:
            self.accuracy *= amount
        if self.accuracy >= 100:
            self.accuracy = 100
        elif self.accuracy <= 0:
            self.accuracy = 0

    def set_accuracy(self, amount):
        self.accuracy = amount

    def set_ammo(self, amount):
        self.ammo = amount

    def set_wait(self, amount):
        self.wait = amount

    def change_bleed_dmg(self, symbol, amount):
        if symbol == "+":
            self.bleed_dmg += amount
        else:
            self.bleed_dmg *= amount

    def change_damage(self, symbol, amount):
        if symbol == "+":
            self.damage += amount
        else:
            self.damage *= amount

    def set_bleed_dmg(self, amount):
        self.bleed_dmg = amount

    def set_target(self, id):
        self.target = id

    def set_shields(self, amount):
        self.shields = amount

    def change_shields(self, symbol, amount):
        if symbol == "+":
            self.shields += amount
        else:
            self.shields *= amount

    # Gun Functions
    def fire(self, victim):
        # is there ammo to fire
        if self.ammo > 0:
            # fire!
            self.ammo -= 1
            return True
        else:
            return False

    def hits(self, victim):
        # do you hit?
        if random.randint(0, 100) <= self.accuracy - victim.get_avoidance():
            self.strike = True
        # if not then miss
        else:
            self.strike = False
        return self.strike

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
            result.append([self.get_id(), None, None, None])
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            return result
        # if fire returns true
        if self.fire(victim) is True:
            print('*BANG!*', end='')
            if self.hits(victim) is True:
                print("- The shot hit!")
                result.append([self.get_id(), self.pick_bodypart(), self.get_damage(), self.get_target()])
                return result
            else:
                result.append([self.get_id(), None, None, self.get_target()])
                print("- The shot missed!")
                return result
        else:
            result.append([self.get_id(), None, None, self.get_target()])
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            return result

    def before_combat(self, gamestate):
        return gamestate

    # Game Getter
    def get_id(self):
        return self.id

    def get_side(self):
        return self.side

    # Game Functions
    def set_id(self, identity):
        self.id = identity

    def set_side(self, side):
        self.side = side
