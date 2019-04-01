# parent
import Character


class Barber(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Barber"
        self.upgrades.append("Swirly Pole:\n\t Every turn all opponents gain 1 stack of bleeding.")
        self.upgrades.append("Shave:\n\t Target friendly character gains 25 avoidance.")
        self.upgrades.append("Mob Doctor:\n\t Reverse up to 40 damage from a single attack"
                             " for target friendly character.")
        self.upgrades.append("Snip:\n\t Target opponent gains bleeding "
                             "equal to the amount of damage you receive this turn.")
        self.upgrades.append("TBA:\n\t TBA")
        self.upgrades.append("TBA:\n\t TBA.")

        self.pole_switch = False
        self.snip_switch = False

        self.upgrade_dict["Swirly Pole:\n\t Every turn all opponents gain 1 stack of bleeding."] = 1
        self.upgrade_dict["Shave:\n\t Target friendly character gains 25 avoidance."] = 2
        self.upgrade_dict["Mob Doctor:\n\t Reverse up to 40 damage from a single attack"
                             " for target friendly character."] = 3
        self.upgrade_dict["Snip:\n\t Target opponent gains bleeding "
                             "equal to the amount of damage you receive this turn."] = 4
        self.upgrade_dict["TBA:\n\t TBA"] = 5
        self.upgrade_dict["TBA:\n\t TBA."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.swirly_pole(gamestate)
            return gamestate
        elif choice == 2:
            self.shave(gamestate)
            return gamestate
        elif choice == 3:
            self.mob_doctor(gamestate)
            return gamestate
        elif choice == 4:
            self.snip(gamestate)
            return gamestate
        elif choice == 5:
            return gamestate
        elif choice == 6:
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def swirly_pole(self, gamestate):
        self.pole_switch = True
        return gamestate

    def turn_start(self, gamestate):
        if self.side == "L":
            for character in gamestate.right_side:
                character.bleed += 1
        else:
            for character in gamestate.left_side:
                character.bleed += 1
        return gamestate

    def shave(self, gamestate):
        num = 0
        if self.side == "L":
            for character in gamestate.left_side:
                print(str(num) + ". " + character.get_name())
                num += 1
            choice = float(input("Give 25 avoidance to the character of your choice."))
            while choice > len(gamestate.left_side):
                choice = float(input("Invalid selection."
                                     "\n Give 25 avoidance to the character of your choice."))
            gamestate.left_side[choice].avoidance += 25
        else:
            for character in gamestate.right_side:
                print(str(num) + ". " + character.get_name())
                num += 1
            choice = float(input("Give 25 avoidance to the character of your choice."))
            while choice > len(gamestate.right_side):
                choice = float(input("Invalid selection."
                                     "\n Give 25 avoidance to the character of your choice."))
            gamestate.right_side[choice].avoidance += 25
        return gamestate

    def mob_doctor(self, gamestate):
        return gamestate

    def snip(self, gamestate):
        self.snip_switch = True
        return gamestate

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
            if self.alive:
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
                    if self.snip_switch:
                        self.target.bleed += damage
                        self.snip_switch = False
                        print(self.target.get_name(), "was cut for", damage, "bleed damage.")
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
