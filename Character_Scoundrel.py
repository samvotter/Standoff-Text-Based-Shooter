# parent
import Character

# child
import Minion_Scoundrel as m

# 4 abilities left
class Scoundrel(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Scoundrel"
        self.upgrades.append("Flee:\n\t Your attacks, as well as attacks made against you, have a -20% chance to hit.")
        self.upgrades.append("Wanton Cruelty:\n\t Your accuracy is reduced by 50%. Damage is increased by 30%.")
        self.upgrades.append("Cannot Lose:\n\t Your misses create an Innocent minion and hit it instead.")
        self.upgrades.append("Disregard:\n\t Attacks which strike minions also strike target character.")
        self.upgrades.append("Coward:\n\t Create three Innocent minions. Attacks are as likely to hit them as you.")
        self.upgrades.append("Chaos:\n\t If six or more minions die, you win.")

        self.minion_deaths = 0
        self.cannot_lose_switch = False
        self.disregard_switch = False
        self.win_switch = False

        self.upgrade_dict["Flee:\n\t Your attacks, as well as attacks made against you, have a -20% chance to hit."] = 1
        self.upgrade_dict["Wanton Cruelty:\n\t Your accuracy is reduced by 50%. Damage is increased by 30%."] = 2
        self.upgrade_dict["Cannot Lose:\n\t Your misses create an Innocent minion and hit it instead."] = 3
        self.upgrade_dict["Disregard:\n\t Attacks which strike minions also strike target character."] = 4
        self.upgrade_dict["Coward:\n\t Create three Innocent minions. Attacks are as likely to hit them as you."] = 5
        self.upgrade_dict["Chaos:\n\t If six or more minions die, you win."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.flee(gamestate)
        elif choice == 2:
            self.wanton_cruelty(gamestate)
        elif choice == 3:
            self.cannot_lose(gamestate)
        elif choice == 4:
            self.disregard(gamestate)
        elif choice == 5:
            self.coward(gamestate)
        elif choice == 6:
            self.chaos(gamestate)
        else:
            print("ERROR APPLYING UPGRADE")

    def flee(self, gamestate):
        # +20% chance attacks made against you will miss, your own accuracy also decreases by -20%
        self.avoidance = 20
        self.accuracy -= 20
        return gamestate

    def wanton_cruelty(self, gamestate):
        # Your accuracy is reduced by 50%. Damage is increased by 30%."
        self.accuracy /= 2
        self.damage *= (4/3)
        return gamestate

    def cannot_lose(self, gamestate):
        # your misses create an Innocent minion and hit it instead.
        self.cannot_lose_switch = True
        return gamestate

    def disregard(self, gamestate):
        # attacks which strike minions also strike target character
        self.disregard_switch = True
        return gamestate

    def coward(self, gamestate):
        # create three Innocent minions. Attacks are as likely to hit them as you
        # append temp
        for i in range(0,3):
            self.minions.append(m.Innocent(self, origin=self))
        return gamestate

    def chaos(self, gamestate):
        # if six or more minions die, you win.
        self.win_switch = True
        return gamestate

    def attack(self, gamestate):
        result = []
        if self.wait > 0:
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            result = [self.target, None, None, None]
            return result
        # if fire returns true
        if self.fire() is True:
            print('*BANG!*', end='')
            # and this upgrade has been selected
            if self.disregard_switch:
                # and the target is a minion
                if self.target.is_minion:
                    # and you hit that target
                    if self.hits(self.target):
                        print("- The shot hit!")
                        result.append([self.target, self.pick_bodypart(), self.damage, self.bleed_dmg])
                        result.append([self.target.parent, self.pick_bodypart(), self.damage, self.bleed_dmg])
                        return result
                    else:
                        result.append([self.target, "Miss", None, None])
                        print("- The shot missed!")
                        return result
            # the target is not a minion
            if self.hits(self.target):
                print("- The shot hit!")
                result.append([self.target, self.pick_bodypart(), self.damage, self.bleed_dmg])
                return result
            else:
                if self.cannot_lose_switch:
                    self.target.minions.append(m.Innocent(self.target, origin=self))
                    if self.hits(self.target.minions[0]):
                        result.append([self.target.minions[0], self.pick_bodypart(), self.damage, self.bleed_dmg])
                result.append([self.target, "Miss", None, None])
                print("- The shot missed!")
                return result
        else:
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            result = [self.target, None, None, None]
            return result

    def end_turn(self, gamestate):
        if self.minion_deaths >= 6 and self.win_switch:
            if self.side == "L":
                gamestate.right_side.clear()
            else:
                gamestate.left_side.clear()
        return gamestate