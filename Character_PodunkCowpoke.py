# parent
import Character


# 5 abilities left
class Podunk_Cowpoke(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Podunk-Cowpoke"
        self.upgrades.append("Bigger Gun:\n\t increase accuracy by +15% and +30% damage.")
        self.upgrades.append("PA!:\n\t TBA")
        self.upgrades.append("Dumb Luck:\n\t Anytime an opponent attacks you and misses, you hit.")
        self.upgrades.append("TBA:\n\t TBA")
        self.upgrades.append("Grapple:\n\t TBA")
        self.upgrades.append("Spread:\n\t All targets have a separate 20% chance of being hit by your attack.")

        self.upgrade_dict["Bigger Gun:\n\t increase accuracy by +15% and +30% damage."] = 1
        self.upgrade_dict["PA!:\n\t TBA"] = 2
        self.upgrade_dict["Dumb Luck:\n\t Anytime an opponent attacks you and misses, you hit."] = 3
        self.upgrade_dict["TBA:\n\t TBA"] = 4
        self.upgrade_dict["Grapple:\n\t TBA"] = 5
        self.upgrade_dict["Spread:\n\t All targets have a separate 20% chance of being hit by your attack."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.bigger_gun(gamestate)
        elif choice == 2:
            self.pa(gamestate)
        elif choice == 3:
            self.dumb_luck(gamestate)
        elif choice == 4:
            self.liquid_courage(gamestate)
        elif choice == 5:
            self.grapple(gamestate)
        elif choice == 6:
            self.spread(gamestate)
        else:
            print("ERROR APPLYING UPGRADE")

    def bigger_gun(self, gamestate):
        # increase accuracy by +15% and +30% damage."
        if self.side == "L":
            gamestate.left_side[self.id].change_damage('*', 1.3)
            gamestate.left_side[self.id].change_accuracy('+', 15)
        elif self.side == "R":
            gamestate.right_side[self.id].change_damage('*', 1.3)
            gamestate.right_side[self.id].change_accuracy('+', 15)
        return gamestate

    def pa(self, gamestate):
        # create 1 minion. It must be die before your character can be attacked
        pass

    def dumb_luck(self, gamestate):
        # Anytime your opponent misses, you hit
        pass

    def liquid_courage(self, gamestate):
        pass

    def grapple(self, gamestate):
        # You deal half damage to target opponent, then you and your target lose all ammo.
        pass

    def spread(self, gamestate):
        # all targets have a separate 20% chance of being hit by your attacks
        pass