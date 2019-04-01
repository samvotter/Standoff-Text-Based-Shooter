# parent
import Character


class Heiress(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Heiress"
        self.upgrades.append("Laudanum:\n\t Gain +10 avoidance and 40 shields. Every turn your shields decay by -5.")
        self.upgrades.append("Aristocrat:\n\t Instead of taking damage,"
                             " you may choose to give 1 ammunition to your attacker.")
        self.upgrades.append("Outlast:\n\t Whenever a character dies, gain all of their unspent ammunition.")
        self.upgrades.append("Refinement:\n\t Gain +6% accuracy every turn.")
        self.upgrades.append("Cash Infusion:\n\t Choose to gain either 20 health, 2 bullets, 5 armor, or 15 shields.")
        self.upgrades.append("Classy:\n\t You may only be targeted by 1 person each turn.")

        self.laudanum_switch = False
        self.aristocrat_switch = False
        self.refinement_switch = False
        self.classy_switch = False

        self.upgrade_dict["Laudanum:\n\t Gain +10 avoidance and 40 shields. Every turn your shields decay by -5."] = 1
        self.upgrade_dict["Aristocrat:\n\t Instead of taking damage,"
                             " you may choose to give 1 ammunition to your attacker."] = 2
        self.upgrade_dict["Outlast:\n\t Whenever a character dies, gain all of their unspent ammunition."] = 3
        self.upgrade_dict["Refinement:\n\t Gain +6% accuracy every turn."] = 4
        self.upgrade_dict["Cash Infusion:\n\t Choose to gain either 20 health, 2 bullets, 5 armor, or 15 shields."] = 5
        self.upgrade_dict["Classy:\n\t You may only be targeted by 1 person each turn."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.laudanum(gamestate)
            return gamestate
        elif choice == 2:
            self.aristocrat(gamestate)
            return gamestate
        elif choice == 3:
            self.outlast(gamestate)
            return gamestate
        elif choice == 4:
            self.refinement(gamestate)
            return gamestate
        elif choice == 5:
            self.cash_infusion(gamestate)
            return gamestate
        elif choice == 6:
            self.classy(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def laudanum(self, gamestate):
        self.avoidance += 10
        self.shields += 40
        self.laudanum_switch = True
        return gamestate

    def aristocrat(self, gamestate):
        self.aristocrat_switch = True
        return gamestate

    def outlast(self):
        pass

    def refinement(self, gamestate):
        self.refinement_switch = True
        return gamestate

    def cash_infusion(self, gamestate):
        print("Select an option:",
              "\t 1. Heal for 20.\n",
              "\t 2. Gain 2 ammo.\n",
              "\t 3. Gain 5 armor.\n",
              "\t 4. Gain 15 shields.\n",)
        choice = input()
        if choice == 1:
            self.heal(20)
        elif choice == 2:
            self.ammo += 2
        elif choice == 3:
            self.armor += 5
        elif choice == 4:
            self.shields += 15
        return gamestate

    def classy(self, gamestate):
        self.classy_switch = True
        return gamestate

    def turn_start(self, gamestate):
        if self.laudanum_switch:
            self.shields -= 5
            if self.shields < 0:
                self.shields = 0
        if self.refinement_switch:
            self.accuracy += 6
        return gamestate

    def take_damage(self, result):
        if result[2] is None or result[1] == "Miss":
            print(self.get_name(), "took no damage.")
            return False
        else:
            if self.aristocrat_switch:
                choice = int(input("Do you want to take damage from this attack? '1' for yes '2' for no."))
                if choice == 2:
                    self.ammo -= 1
                    return False
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

    def check_targets(self, side_off):
        number = 0
        for character in side_off:
            if character.target == self:
                number += 1
        if number > 1:
            return True
        else:
            return False

    def before_combat(self, gamestate):
        if self.classy_switch:
            if self.side == "L":
                while self.check_targets(gamestate.right_side):
                    print("Too many characters are targeting:", self.get_name())
                    for character in gamestate.right_side:
                        character.set_target(gamestate.left_side)
            else:
                while self.check_targets(gamestate.left_side):
                    print("Too many characters are targeting:", self.get_name())
                    for character in gamestate.left_side:
                        character.set_target(gamestate.right_side)
        return gamestate
