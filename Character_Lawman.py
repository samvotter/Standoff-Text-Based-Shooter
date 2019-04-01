# parent
import Character


# 6 abilities left
class Lawman(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Lawman"
        self.upgrades.append("Deputize:\n\t Target minion joins your side.")
        self.upgrades.append("Mount Up:\n\t TBA.")
        self.upgrades.append("Partner:\n\t TBA.")
        self.upgrades.append("Incorruptible:\n\t You are incapable of hitting anything other than your intended target.")
        self.upgrades.append("Sheriff's Privilege:\n\t Your attacks land first, then your opponent responds.")
        self.upgrades.append("Arrest:\n\t If your target has 25 health or less, they automatically surrender.")

        self.upgrade_dict["Deputize:\n\t Target minion joins your side."] = 1
        self.upgrade_dict["Mount Up:\n\t TBA."] = 2
        self.upgrade_dict["Partner:\n\t TBA."] = 3
        self.upgrade_dict["Incorruptible:\n\t You are incapable of hitting anything other than your intended target."] = 4
        self.upgrade_dict["Sheriff's Privilege:\n\t Your attacks land first, then your opponent responds."] = 5
        self.upgrade_dict["Arrest:\n\t If your target has 25 health or less, they automatically surrender."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.deputize(gamestate)
            return gamestate
        elif choice == 2:
            self.mount_up(gamestate)
            return gamestate
        elif choice == 3:
            self.partner(gamestate)
            return gamestate
        elif choice == 4:
            self.incorruptible(gamestate)
            return gamestate
        elif choice == 5:
            self.sheriffs_privilege(gamestate)
            return gamestate
        elif choice == 6:
            self.arrest(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def deputize(self, gamestate):
        # target minion joins your side.
        return gamestate

    def mount_up(self, gamestate):
        # undecided
        return gamestate

    def partner(self, gamestate):
        # undecided
        return gamestate

    def incorruptible(self, gamestate):
        # you are incapable of hitting anything other than your intended target
        return gamestate

    def sheriffs_privilege(self, gamestate):
        # your attacks land first, then your opponent responds.
        return gamestate

    def arrest(self, gamestate):
        # if your target has 25 health or less, they automatically surrender
        return gamestate