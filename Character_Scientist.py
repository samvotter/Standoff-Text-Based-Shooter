# parent
import Character


# 6 abilities left
class Scientist(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Scientist"
        self.upgrades.append("Cure Disease:\n\t Remove all debuffs placed on you by opponents.")
        self.upgrades.append("Work Smarter:\n\t If you miss, you hit your target's feet. "
                             "If you would hit your target's legs, you hit your target's chest.")
        self.upgrades.append("Technocracy:\n\t Instead of causing damage, all attacks now heal one another. "
                             "They still cause bleeding.")
        self.upgrades.append("Collaborate:\n\t Create 2 Graduate Assistant minions, each provide 10 shields every turn.")
        self.upgrades.append("Dedication:\n\t Select any upgrade, except this one, again.")
        self.upgrades.append("Research:\n\t Gain one of your opponent's upgrades.")

        self.upgrade_dict["Cure Disease:\n\t Remove all debuffs placed on you by opponents."] = 1
        self.upgrade_dict["Work Smarter:\n\t If you miss, you hit your target's feet. "
                             "If you would hit your target's legs, you hit your target's chest."] = 2
        self.upgrade_dict["Technocracy:\n\t Instead of causing damage, all attacks now heal one another. "
                             "They still cause bleeding."] = 3
        self.upgrade_dict["Collaborate:\n\t Create 2 Graduate Assistant minions, each provide 10 shields every turn."] = 4
        self.upgrade_dict["Dedication:\n\t Select any upgrade, except this one, again."] = 5
        self.upgrade_dict["Research:\n\t Gain one of your opponent's upgrades."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.cure_disease()
        elif choice == 2:
            self.work_smarter()
        elif choice == 3:
            self.technocracy()
        elif choice == 4:
            self.collaborate()
        elif choice == 5:
            self.dedication()
        elif choice == 6:
            self.research()
        else:
            print("ERROR APPLYING UPGRADE")

    def cure_disease(self):
        # remove all debuffs placed on you by opponents.
        pass

    def work_smarter(self):
        # if you miss, you hit your target's feet
        # if you would hit your target's legs, you hit your target's chest
        pass

    def technocracy(self):
        # instead of causing damage, all shots now heal one another.
        # shots still cause bleeding
        pass

    def collaborate(self):
        # create to Graduate Assistant minions, each provide 10 shields
        # per turn.
        pass

    def dedication(self):
        # select any upgrade, except this one, again.
        pass

    def research(self):
        # gain one of your opponent's upgrades
        pass
