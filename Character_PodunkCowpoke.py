# parent
import Character

# child
import Minion_PodunkCowPoke as m

# libraries
import random


# 5 abilities left
class Podunk_Cowpoke(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Podunk-Cowpoke"
        self.upgrades.append("Bigger Gun:\n\t increase accuracy by +15% and +30% damage.")
        self.upgrades.append("PA!:\n\t A Child minion leaps in front of you with 10 hp. "
                             "Attacks against you target the Child instead."
                             "If the Child dies, gain +10 damage.")
        self.upgrades.append("Dumb Luck:\n\t Anytime an opponent attacks you and misses, you hit.")
        self.upgrades.append("TBA:\n\t TBA")
        self.upgrades.append("Grapple:\n\t TBA")
        self.upgrades.append("Spread:\n\t All targets have a separate 20% chance of being hit by your attack.")

        self.spread_switch = False

        self.upgrade_dict["Bigger Gun:\n\t increase accuracy by +15% and +30% damage."] = 1
        self.upgrade_dict["PA!:\n\t A Child minion leaps in front of you with 10 hp. "
                             "Attacks against you target the Child instead."
                             "If the Child dies, gain +10 damage."] = 2
        self.upgrade_dict["Dumb Luck:\n\t Anytime an opponent attacks you and misses, you hit."] = 3
        self.upgrade_dict["TBA:\n\t TBA"] = 4
        self.upgrade_dict["Grapple:\n\t TBA"] = 5
        self.upgrade_dict["Spread:\n\t All targets have a separate 20% chance of being hit by your attack."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.bigger_gun(gamestate)
            return gamestate
        elif choice == 2:
            self.pa(gamestate)
            return gamestate
        elif choice == 3:
            self.dumb_luck(gamestate)
            return gamestate
        elif choice == 4:
            self.liquid_courage(gamestate)
            return gamestate
        elif choice == 5:
            self.grapple(gamestate)
            return gamestate
        elif choice == 6:
            self.spread(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def bigger_gun(self, gamestate):
        # increase accuracy by +15% and +30% damage."
        self.accuracy += 15
        self.damage *= 1.3
        return gamestate

    def pa(self, gamestate):
        # create 1 minion. It must be die before your character can be attacked. Causes RAGE.
        self.minions.append(m.Child(self, health=10))
        return gamestate

    def dumb_luck(self, gamestate):
        # Anytime your opponent misses, you hit
        pass

    def liquid_courage(self, gamestate):
        pass

    def grapple(self, gamestate):
        # You deal half damage to target opponent, then you and your target lose all ammo.
        pass

    def spread(self, gamestate):
        # all targets have a separate 20% chance of being hit by your attacks
        self.spread_switch = True
        return gamestate

    # Meta function serving as the default attack sequence
    def attack(self, gamestate):
        result = []
        if self.wait > 0:
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            result = [self.target, None, None, None]
            return result
        # if fire returns true
        if self.fire() is True:
            if self.spread_switch:
                if self.side == "L":
                    for character in gamestate.right_side:
                        print('*BANG!*', end='')
                        if self.hits(character) is True:
                            print("- The shot hit!")
                            result.append([character, self.pick_bodypart(), self.damage, self.bleed_dmg])
                        else:
                            result.append([self.target, "Miss", None, None])
                            print("- The shot missed!")
                    return result
                else:
                    for character in gamestate.left_side:
                        print('*BANG!*', end='')
                        if self.hits(character) is True:
                            print("- The shot hit!")
                            result.append([character, self.pick_bodypart(), self.damage, self.bleed_dmg])
                        else:
                            result.append([self.target, "Miss", None, None])
                            print("- The shot missed!")
                    return result
            print('*BANG!*', end='')
            if self.hits(self.target) is True:
                print("- The shot hit!")
                result.append([self.target, self.pick_bodypart(), self.damage, self.bleed_dmg])
                return result
            else:
                result.append([self.target, "Miss", None, None])
                print("- The shot missed!")
                return result
        else:
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            result = [self.target, None, None, None]
            return result

    def before_combat(self, gamestate):
        if len(self.minions) > 0:
            for minion in self.minions:
                minion.does_thing(gamestate)
        return gamestate

    def hits(self, victim):
        # do you have spread?
        if self.spread_switch is True and victim != self.target:
            if random.randint(0, 100) <= 20 - victim.avoidance:
                return True
        # do you hit?
        if random.randint(0, 100) <= self.accuracy - victim.avoidance:
            return True
        # if not then miss
        else:
            return False
