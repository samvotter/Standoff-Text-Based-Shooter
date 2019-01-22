# parent
import Character

# 6 abilities left
class Barman(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Barman"
        self.upgrades.append("Insurance Money:\n\t All characters including yourself gain 4 stacks of burning. "
                             "In three turns, you heal for 10.")
        self.upgrades.append("Real Power:\n\t The next time an opponent character dies. "
                             "You may choose an other target to die instead.")
        self.upgrades.append("Under the Table:\n\t Take a free shot at any target"
                             " before any other upgrade cards are revealed.")
        self.upgrades.append("Drinking Contest:\n\t every shot lowers the accuracy of target shooter by -10%.")
        self.upgrades.append("Pound of Flesh:\n\t When an opponent misses, you gain 5 of their health.")
        self.upgrades.append("Water Down:\n\t Everyone's damage is reduced by 10.")

        self.upgrade_dict["Insurance Money:\n\t All characters including yourself gain 4 stacks of burning."
                             " In three turns, you heal for 10."] = 1
        self.upgrade_dict["Real Power:\n\t The next time an opponent character dies. "
                             "You may choose an other target to die instead."] = 2
        self.upgrade_dict["Under the Table:\n\t Take a free shot at any target"
                             " before any other upgrade cards are revealed."] = 3
        self.upgrade_dict["Drinking Contest:\n\t every shot lowers the accuracy of target shooter by -10%."] = 4
        self.upgrade_dict["Pound of Flesh:\n\t When an opponent misses, you gain 5 of their health."] = 5
        self.upgrade_dict["Water Down:\n\t Everyone's damage is reduced by 10."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.insurance_money()
        elif choice == 2:
            self.real_power()
        elif choice == 3:
            self.under_the_table()
        elif choice == 4:
            self.drinking_contest()
        elif choice == 5:
            self.pound_of_flesh()
        elif choice == 6:
            self.water_down()
        else:
            print("ERROR APPLYING UPGRADE")

    def insurance_money(self):
        # all characters including yourself gain 4 stacks of burning.
        # in three turns, you heal for 10.
        pass

    def real_power(self):
        # the next time an opponent character dies
        # you may choose an other target to die instead.
        pass

    def under_the_table(self):
        # take a free shot at any target before any other upgrade cards are revealed.
        pass

    def drinking_contest(self):
        # every shot lowers the accuracy of target shooter by -10%
        pass

    def pound_of_flesh(self):
        # when an opponent misses, you gain 5 of their health
        pass

    def water_down(self):
        # everyone's damage is reduced by 10.
        pass