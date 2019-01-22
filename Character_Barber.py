# parent
import Character


class Barber(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Barber"
        self.upgrades.append("Swirly Pole:\n\t Every turn all opponents gain 1 stack of bleeding.")
        self.upgrades.append("Shave:\n\t Target friendly character gains 25 avoidance.")
        self.upgrades.append("Mob Doctor:\n\t Reverse up to 40 damage from a single attack"
                             " for target friendly character.")
        self.upgrades.append("Snip:\n\t The next time you take damage, "
                             "target opponent gains that many stacks of bleeding")
        self.upgrades.append("Chivalry:\n\t Give one of your bullets to every friendly character.")
        self.upgrades.append("Squire:\n\t Resupply yourself with another 6 ammo before combat 3 turns from now.")

        self.longsword_stun = False
        self.longsword_switch = False
        self.empty_switch = False
        self.squire_wait_end = 0

        self.upgrade_dict["Longsword:\n\t If you run out of ammo: "
                             "after waiting 1 turn, your attacks no longer cost ammo. "
                             "Gain +15 damage and +20% accuracy."] = 1
        self.upgrade_dict["Empty The Chamber:\n\t Fire all of your remaining ammunition for 2/7 base damage."] = 2
        self.upgrade_dict["Raise Shields:\n\t Trade the maximum of up to 2 bullets for 25 shields each."] = 3
        self.upgrade_dict["Suit of Armor:\n\t Trade the maximum of up to 3 bullets: "
                             "1 bullet gives 5 armor. 2 bullets gives 9 armor. 3 bullets gives 12 armor."] = 4
        self.upgrade_dict["Chivalry:\n\t Give one of your bullets to every friendly character."] = 5
        self.upgrade_dict["Squire:\n\t Resupply yourself with another 6 ammo before combat 3 turns from now."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.longsword(gamestate)
            return gamestate
        elif choice == 2:
            self.empty_the_chamber(gamestate)
            return gamestate
        elif choice == 3:
            self.raise_shield(gamestate)
            return gamestate
        elif choice == 4:
            self.suit_of_armor(gamestate)
            return gamestate
        elif choice == 5:
            self.chivalry(gamestate)
            return gamestate
        elif choice == 6:
            self.squire(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def longsword(self, gamestate):
        # if you run out of ammo:
        # your attacks no longer cost ammo. Gain +15 damage and +20% accuracy.
        # You must wait at least 1 turn before this takes effect.
        if self.side == "L":
            gamestate.left_side[self.id].longsword_switch = True
            gamestate.left_side[self.id].longsword_stun = True
        elif self.side == "R":
            gamestate.right_side[self.id].longsword_switch = True
            gamestate.right_side[self.id].longsword_stun = True
        return gamestate