# parent
import Character


# all incomplete
class Judge(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Judge"
        self.upgrades.append("Jury:\n\t Gain 12 Jury minions. Each one has a 50% chance of voting innocent or guilty."
                             " Innocent heals the target for 5, guilty damages the target for 10.")
        self.upgrades.append("Overrule:\n\t For the next attack,"
                             " you may swap the damage you take with the damage you deal.")
        self.upgrades.append("Bias:\n\t Jury minions now have a 75% chance of voting in the direction you choose.")

        self.upgrade_dict["Jury:\n\t Gain 12 Jury minions. Each one has a 50% chance of voting innocent or guilty."
                             " Innocent heals the target for 5, guilty damages the target for 10."] = 1
        self.upgrade_dict["Overrule:\n\t For the next attack,"
                             " you may swap the damage you take with the damage you deal."] = 2
        self.upgrade_dict["Bias:\n\t Jury minions now have a 75% chance of voting in the direction you choose."] = 3

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.jury()
        elif choice == 2:
            self.overrule()
        elif choice == 3:
            self.bias()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        else:
            print("ERROR APPLYING UPGRADE")

    def jury(self):
        # gain 12 minions. Each one has a 50% chance of voting
        # innocent or guilty. Innocent heals the target for 5
        # guilty damages the target for 10
        pass

    def overrule(self):
        # for the next attack, you may swap
        # the damage you take with the damage you deal
        pass

    def bias(self):
        # Jury minions now have a 75% chance of voting in the direction you choose.
        pass