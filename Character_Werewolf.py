# parent
import Character


# 6 abilities left
class Werewolf(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Werewolf"
        self.upgrades.append("Moon Cycles:\n\t On even turns, heal for 5. On odd turns, you do +10 damage.")
        self.upgrades.append("Bloodthirsty:\n\t Attacks heal you for three times the target's amount of bleeding.")
        self.upgrades.append("Ferocity:\n\t Every successful attack increases your damage by 5.")
        self.upgrades.append("Claws:\n\t On odd turns, you do not spend ammo to attack.")
        self.upgrades.append("Rage:\n\t On odd turns, you have 25 shields and 5 armor. Lose these benefits on even turns.")
        self.upgrades.append("Blood God:\n\t Your attacks inflict bleeding equal to the amount you are bleeding.")

        self.moon_switch = False
        self.blood_switch = False
        self.ferocity_switch = False
        self.claws_switch = False
        self.rage_switch = False

        self.upgrade_dict["Moon Cycles:\n\t On even turns, heal for 5. On odd turns, you do +10 damage."] = 1
        self.upgrade_dict["Bloodthirsty:\n\t Attacks heal you for three times the target's amount of bleeding."] = 2
        self.upgrade_dict["Ferocity:\n\t Every successful attack increases your damage by 5."] = 3
        self.upgrade_dict["Claws:\n\t On odd turns, you do not spend ammo to attack."] = 4
        self.upgrade_dict["Rage:\n\t On odd turns, you have 25 shields and 5 armor. Lose these benefits on even turns."] = 5
        self.upgrade_dict["Blood God:\n\t Your attacks inflict bleeding equal to the amount you are bleeding."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.moon_cycles(gamestate)
            return gamestate
        elif choice == 2:
            self.bloodthirsty(gamestate)
            return gamestate
        elif choice == 3:
            self.ferocity(gamestate)
            return gamestate
        elif choice == 4:
            self.claws(gamestate)
            return gamestate
        elif choice == 5:
            self.rage(gamestate)
            return gamestate
        elif choice == 6:
            self.blood_god(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def moon_cycles(self, gamestate):
        # on even turns, heal for 5. On odd turns, you do +10 damage.
        self.moon_switch = True
        return gamestate

    def bloodthirsty(self, gamestate):
        # Attacks heal you for three times the target's amount of bleeding.
        self.blood_switch = True
        return gamestate

    def ferocity(self, gamestate):
        # Every successful attack increases your damage by 5.
        self.ferocity_switch = True
        return gamestate

    def claws(self, gamestate):
        # On odd turns, you do not spend ammo to attack.
        self.claws_switch = True
        return gamestate

    def rage(self, gamestate):
        # On odd turns, you have 25 shields and 5 armor. Lose these benefits on even turns.
        self.rage_switch = True
        return gamestate

    def blood_god(self, gamestate):
        # Your attacks inflict bleeding equal to the amount you are bleeding.
        self.bleed_dmg = self.bleed
        return gamestate

    def turn_start(self, gamestate):
        if self.moon_switch is True:
            if gamestate.turn % 2 == 0:
                self.heal(5)
                self.damage += 5
            else:
                self.damage -= 5

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
                if self.ferocity_switch is True:
                    self.damage += 5
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