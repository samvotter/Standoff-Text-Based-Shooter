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
        self.upgrades.append("Snip:\n\t Target opponent gains bleeding "
                             "equal to the amount of damage you receive this turn.")
        self.upgrades.append("TBA:\n\t TBA")
        self.upgrades.append("TBA:\n\t TBA.")

        self.pole_switch = False

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
        if self.side == "L":
            gamestate.left_side[self.id].pole_switch = True
        elif self.side == "R":
            gamestate.right_side[self.id].pole_switch = True
        return gamestate

    def turn_start(self, gamestate):
        if self.side == "L":
            for character in gamestate.right_side:
                character.bleed += 1
        elif self.side == "R":
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
        elif self.side == "R":
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
        return gamestate