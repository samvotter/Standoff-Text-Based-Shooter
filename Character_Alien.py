# parent
import Character


class Alien(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Alien"
        self.upgrades.append("Reactive Design:\n\t If you take damage on a specific body part, the next time that "
                             "spot would take damage, ignore that damage.")
        self.upgrades.append("Slow Shield:\n\t Gain 100 shields.")
        self.upgrades.append("Abduct:\n\t You and target character leave the battlefield for 3 turns.")
        self.upgrades.append("Probe:\n\t TBA.")
        self.upgrades.append("Set to Stun:\n\t your hits cause enemies to lose their next turn. "
                             "This cannot happen twice in a row.")
        self.upgrades.append("Future Tech:\n\t Your successful attacks always do 10 more damage "
                             "than they otherwise would.")

        self.upgrade_dict["Reactive Design:\n\t If you take damage on a specific body part, the next time that "
                             "spot would take damage, ignore that damage."] = 1
        self.upgrade_dict["Slow Shield:\n\t Gain 100 shields."] = 2
        self.upgrade_dict["Abduct:\n\t You and target character leave the battlefield for 3 turns."] = 3
        self.upgrade_dict["Probe:\n\t TBA."] = 4
        self.upgrade_dict["Set to Stun:\n\t your hits cause enemies to lose their next turn. "
                             "This cannot happen twice in a row."] = 5
        self.upgrade_dict["Future Tech:\n\t Your successful attacks always do 10 more damage "
                             "than they otherwise would."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.reactive_design(gamestate)
            return gamestate
        elif choice == 2:
            self.slow_shield(gamestate)
            return gamestate
        elif choice == 3:
            self.abduct(gamestate)
            return gamestate
        elif choice == 4:
            self.probe(gamestate)
            return gamestate
        elif choice == 5:
            self.set_to_stun(gamestate)
            return gamestate
        elif choice == 6:
            self.future_tech(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def reactive_design(self, gamestate):
        return gamestate

    def slow_shield(self, gamestate):
        if self.side == "L":
            gamestate.left_side[self.id].shields = 100
        elif self.side == "R":
            gamestate.right_side[self.id].shields = 100
        return gamestate

    def abduct(self, gamestate):
        return gamestate

    def probe(self, gamestate):
        return gamestate

    def set_to_stun(self, gamestate):
        return gamestate

    def future_tech(self, gamestate):
        return gamestate