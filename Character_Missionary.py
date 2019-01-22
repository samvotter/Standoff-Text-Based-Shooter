# parent
import Character

# 6 abilities left
class Missionary(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Missionary"
        self.upgrades.append("Come to Jesus:\n\t If you are not being targeted, deal twice as much damage.")
        self.upgrades.append("Martyrdom:\n\t Friendly characters heal equal to the damage you take.")
        self.upgrades.append("Guilt:\n\t Opponents you have already hit gain 6 stacks of bleeding.")
        self.upgrades.append("Sermonize:\n\t Until next turm, all players gain 30 avoidance.")
        self.upgrades.append("Tithe:\n\t All opponents give you one bullet or 10% of their maximum health.")
        self.upgrades.append("Pray:\n\t If your next attack hits, the target dies. If it misses, you die.")

        self.upgrade_dict["Come to Jesus:\n\t If you are not being targeted, deal twice as much damage."] = 1
        self.upgrade_dict["Martyrdom:\n\t Friendly characters heal equal to the damage you take."] = 2
        self.upgrade_dict["Guilt:\n\t Opponents you have already hit gain 6 stacks of bleeding."] = 3
        self.upgrade_dict["Sermonize:\n\t Until next turm, all players gain 30 avoidance."] = 4
        self.upgrade_dict["Tithe:\n\t All opponents give you one bullet or 10% of their maximum health."] = 5
        self.upgrade_dict["Pray:\n\t If your next attack hits, the target dies. If it misses, you die."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.come_to_jesus()
        elif choice == 2:
            self.martyrdom()
        elif choice == 3:
            self.guilt()
        elif choice == 4:
            self.sermonize()
        elif choice == 5:
            self.tithe()
        elif choice == 6:
            self.pray()
        else:
            print("ERROR APPLYING UPGRADE")

    def come_to_jesus(self):
        pass

    def martyrdom(self):
        pass

    def guilt(self):
        pass

    def sermonize(self):
        pass

    def tithe(self):
        pass

    def pray(self):
        pass