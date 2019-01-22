# parent
import Character


# Character should take Health on a rollercoaster of ups n downs
class Banker(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Banker"
        self.upgrades.append("Loan:\n\t Give as much Health as you choose to target. At the beginning of each turn, "
                             "gain 25% of the lost health as interest from the target.")
        self.upgrades.append("Print Money:\n\t All characters gain 30 Health. All attacks do +10 damage.")
        self.upgrades.append("TBA:\n\t TBA.")
        self.upgrades.append("TBA:\n\t TBA.")
        self.upgrades.append("TBA:\n\t TBA.")
        self.upgrades.append("TBA:\n\t TBA.")

        self.silver_bullets_switch = False
        self.ricochet_switch = False

        self.upgrade_dict["Deadshot:\n\t Set your accuracy to 100%"] = 1
        self.upgrade_dict["TBA:\n\t "] = 2
        self.upgrade_dict["Posse:\n\t Create 2 Posse minions."
                          "They attack for 5 damage and fire whenever you attack."] = 3
        self.upgrade_dict["Silver Bullet:\n\t Your next attack does double damage."] = 4
        self.upgrade_dict["Ricochet:\n\t Your next attack may hit any number of opponents"] = 5
        self.upgrade_dict["Lead Poisoning:\n\t Your attacks inflict 4 stacks of bleeding."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.deadshot(gamestate)
            return gamestate
        elif choice == 2:
            self.two_guns(gamestate)
            return gamestate
        elif choice == 3:
            self.posse(gamestate)
            return gamestate
        elif choice == 4:
            self.silver_bullet(gamestate)
            return gamestate
        elif choice == 5:
            self.ricochet(gamestate)
            return gamestate
        elif choice == 6:
            self.lead_poisoning(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def deadshot(self, gamestate):
        # You never miss
        if self.side == "L":
            gamestate.left_side[self.id].set_accuracy(100)
        elif self.side == "R":
            gamestate.right_side[self.id].set_accuracy(100)
        return gamestate