# parent
import Character


# 6 abilities left
class Ninja(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Ninja"
        self.upgrades.append("Throwing Stars:\n\t Instead of firing, throw two ninja stars for half damage.")
        self.upgrades.append("Hobble:\n\t If your attacks hit your opponents feet twice, they die.")
        self.upgrades.append("Focused Attacks:\n\t All future attacks hit where your next attack lands."
                             " If you miss ignore this effect.")
        self.upgrades.append("Fatal Mistake:\n\t Every other time your opponent misses, strike them for 50 damage.")
        self.upgrades.append("Illusion:\n\t Create 7 Illusion minions. They die in one hit, you die in one hit."
                             "Attacks against you have an equal chance of hitting minions as hitting you.")
        self.upgrades.append("Assassinate:\n\t Attacks against targets with more than 75 health do 50% more damage.")

        self.stars_switch = False
        self.feet_hits = 0
        self.feet_switch = False
        self.focused_switch = False
        self.focused_part = None
        self.assassin_switch = False

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
            self.throwing_stars(gamestate)
            return gamestate
        elif choice == 2:
            self.hobble(gamestate)
            return gamestate
        elif choice == 3:
            self.focused_attacks(gamestate)
            return gamestate
        elif choice == 4:
            self.fatal_mistake(gamestate)
            return gamestate
        elif choice == 5:
            self.illusion(gamestate)
            return gamestate
        elif choice == 6:
            self.assassinate(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def throwing_stars(self, gamestate):
        # fire twice each turn
        self.ammo *= 2
        self.stars_switch = True
        return gamestate

    def hobble(self, gamestate):
        # if your attacks hit your opponents feet twice, you win
        self.feet_switch = True
        return gamestate

    def focused_attacks(self, gamestate):
        # all future attacks hit where your next attack lands.
        # if you miss ignore this effect
        self.focused_switch = True
        return gamestate

    def fatal_mistake(self):
        # every other time your opponent misses, strike them for 50 damage.
        pass

    def illusion(self):
        # Create 7 Illusion minions. They die in one hit, you die in one hit.
        # Attacks against you have an equal chance of hitting minions as hitting you.
        pass

    def assassinate(self, gamestate):
        # attacks against targets with more than 75 health do 50% more damage
        self.assassin_switch = True
        return gamestate

    def attack(self, gamestate):
        if self.assassin_switch and self.target.health > self.target.maxhp*(3 / 4):
            damage = self.damage*1.5
        else:
            damage = self.damage
        result = []
        if self.wait > 0:
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            result = [self.target, None, None, None]
            return result
        # if fire returns true
        if self.fire() is True:
            print('*BANG!*', end='')
            if self.stars_switch:
                for i in range(0, 2):
                    if self.hits(self.target) is True:
                        if self.focused_switch and self.focused_part:
                            part = self.focused_part
                        elif self.focused_switch:
                            part = self.pick_bodypart()
                            self.focused_part = part
                        else:
                            part = self.pick_bodypart()
                        if self.feet_switch and part == "Feet":
                            self.feet_hits += 1
                        print("- The shot hit!")
                        result.append([self.target, part, damage/2, self.bleed_dmg])
                    else:
                        result.append([self.target, "Miss", None, None])
                        print("- The shot missed!")
                return result
            if self.hits(self.target) is True:
                if self.focused_switch and self.focused_part:
                    part = self.focused_part
                elif self.focused_switch:
                    part = self.pick_bodypart()
                    self.focused_part = part
                else:
                    part = self.pick_bodypart()
                if self.feet_switch and part == "Feet":
                    self.feet_hits += 1
                print("- The shot hit!")
                result.append([self.target, part, damage, self.bleed_dmg])
                return result
            else:
                result.append([self.target, "Miss", None, None])
                print("- The shot missed!")
                return result
        else:
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            result = [self.target, None, None, None]
            return result