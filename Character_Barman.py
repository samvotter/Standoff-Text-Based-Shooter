# parent
import Character

# 6 abilities left
class Barman(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Barman"
        self.upgrades.append("Insurance Money:\n\t All characters including yourself gain 4 stacks of burning. "
                             "In three turns, you heal for 10.")
        self.upgrades.append("Real Power:\n\t The next time an opponent character dies. "
                             "You may choose an other target to die instead.")
        self.upgrades.append("Under the Table:\n\t Take a free shot at any target"
                             " before any other upgrade cards are revealed.")
        self.upgrades.append("Drinking Contest:\n\t every shot lowers the accuracy of the shooter by -10%.")
        self.upgrades.append("Pound of Flesh:\n\t When an opponent misses, you gain 5 of their health.")
        self.upgrades.append("Water Down:\n\t Everyone's damage is reduced by 10.")

        self.insurance = 0

        self.upgrade_dict["Insurance Money:\n\t All characters including yourself gain 4 stacks of burning."
                             " In three turns, you heal for 10."] = 1
        self.upgrade_dict["Real Power:\n\t The next time an opponent character dies. "
                             "You may choose an other target to die instead."] = 2
        self.upgrade_dict["Under the Table:\n\t Take a free shot at any target"
                             " before any other upgrade cards are revealed."] = 3
        self.upgrade_dict["Drinking Contest:\n\t every shot lowers the accuracy of the shooter by -10%."] = 4
        self.upgrade_dict["Pound of Flesh:\n\t When an opponent misses, you gain 5 of their health."] = 5
        self.upgrade_dict["Water Down:\n\t Everyone's damage is reduced by 10."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.insurance_money(gamestate)
            return gamestate
        elif choice == 2:
            self.real_power(gamestate)
            return gamestate
        elif choice == 3:
            self.under_the_table(gamestate)
            return gamestate
        elif choice == 4:
            self.drinking_contest(gamestate)
            return gamestate
        elif choice == 5:
            self.pound_of_flesh(gamestate)
            return gamestate
        elif choice == 6:
            self.water_down(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def insurance_money(self, gamestate):
        for character in gamestate.left_side:
            character.burn += 4
        for character in gamestate.right_side:
            character.burn += 4
        self.insurance = gamestate.turn + 3
        return gamestate

    def real_power(self, gamestate):
        return gamestate

    def under_the_table(self, gamestate):
        self.attack(self.target)
        return gamestate

    def drinking_contest(self, gamestate):
        return gamestate

    def pound_of_flesh(self, gamestate):
        return gamestate

    def water_down(self, gamestate):
        for character in gamestate.left_side:
            character.damage -= 10
        for character in gamestate.right_side:
            character.damage -= 10
        return gamestate

    def turn_start(self, gamestate):
        if gamestate.turn == self.insurance:
            self.health += 10
        return gamestate