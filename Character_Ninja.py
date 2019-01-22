# parent
import Character


# 6 abilities left
class Ninja(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Ninja"
        self.upgrades.append("Throwing Stars:\n\t Instead of firing, throw two ninja stars for half damage.")
        self.upgrades.append("Hobble:\n\t If your attacks hit your opponents feet twice, they die.")
        self.upgrades.append("Focused Attacks:\n\t All future attacks hit where your next attack lands."
                             " If you miss ignore this effect.")
        self.upgrades.append("Fatal Mistake:\n\t Every other time your opponent misses, strike them for 50 damage.")
        self.upgrades.append("Illusion:\n\t Create 7 Illusion minions. They die in one hit, you die in one hit."
                             "Attacks against you have an equal chance of hitting minions as hitting you.")
        self.upgrades.append("Assassinate:\n\t Attacks against targets with more than 75 health do 50% more damage.")

        self.upgrade_dict["Throwing Stars:\n\t Instead of firing, throw two ninja stars for half damage."] = 1
        self.upgrade_dict["Hobble:\n\t If your attacks hit your opponents feet twice, they die."] = 2
        self.upgrade_dict["Focused Attacks:\n\t All future attacks hit where your next attack lands."
                             " If you miss ignore this effect."] = 3
        self.upgrade_dict["Fatal Mistake:\n\t Every other time your opponent misses, strike them for 50 damage."] = 4
        self.upgrade_dict["Illusion:\n\t Create 7 Illusion minions. They die in one hit, you die in one hit."
                             "Attacks against you have an equal chance of hitting minions as hitting you."] = 5
        self.upgrade_dict["Assassinate:\n\t Attacks against targets with more than 75 health do 50% more damage."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.throwing_stars()
        elif choice == 2:
            self.hobble()
        elif choice == 3:
            self.focused_attacks()
        elif choice == 4:
            self.fatal_mistake()
        elif choice == 5:
            self.illusion()
        elif choice == 6:
            self.assassinate()
        else:
            print("ERROR APPLYING UPGRADE")

    def throwing_stars(self):
        self.damage /= 2
        self.ammo *= 2
        # fire twice each turn

    def hobble(self):
        # if your attacks hit your opponents feet twice, you win
        pass

    def focused_attacks(self):
        # all future attacks hit where your next attack lands.
        # if you miss ignore this effect
        pass

    def fatal_mistake(self):
        # every other time your opponent misses, strike them for 50 damage.
        pass

    def illusion(self):
        # Create 7 Illusion minions. They die in one hit, you die in one hit.
        # Attacks against you have an equal chance of hitting minions as hitting you.
        pass

    def assassinate(self):
        # attacks against targets with more than 75 health do 50% more damage
        pass