# parent
import Character


class Diplomat(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Diplomat"
        self.upgrades.append("Common Foe:\n\t Create a Common Foe minion with health equal to "
                             "the combined health of all characters. "
                             "All characters must target this minion if able.")
        self.upgrades.append("Cease Fire:\n\t The results of this turn will be applied after combat next turn.")
        self.upgrades.append("Productive Dialogue:\n\t If you and your target both miss, both of you heal for 50.")
        self.upgrades.append("Brinksmanship:\n\t Reduce your health and the health of your target to 1. "
                             "Cure all bleeding on yourself and your target.")
        self.upgrades.append("TBA: .")
        self.upgrades.append("Contractualism:\n\t If you would be healed, so is target.")

        self.upgrade_dict["Common Foe:\n\t Create a Common Foe minion with health equal to "
                             "the combined health of all characters. "
                             "All characters must target this minion if able."] = 1
        self.upgrade_dict["Cease Fire:\n\t The results of this turn will be applied after combat next turn."] = 2
        self.upgrade_dict["Productive Dialogue:\n\t If you and your target both miss, both of you heal for 50."] = 3
        self.upgrade_dict["Brinksmanship:\n\t Reduce your health and the health of your target to 1. "
                             "Cure all bleeding on yourself and your target."] = 4
        self.upgrade_dict["TBA: ."] = 5
        self.upgrade_dict["Contractualism:\n\t If you would be healed, so is target."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.common_foe(gamestate)
            return gamestate
        elif choice == 2:
            self.cease_fire(gamestate)
            return gamestate
        elif choice == 3:
            self.productive_dialogue(gamestate)
            return gamestate
        elif choice == 4:
            self.brinksmanship(gamestate)
            return gamestate
        elif choice == 5:
            self.understanding(gamestate)
            return gamestate
        elif choice == 6:
            self.contractualism(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def common_foe(self, gamestate):
        return gamestate

    def cease_fire(self, gamestate):
        return gamestate

    def productive_dialogue(self, gamestate):
        return gamestate

    def brinksmanship(self, gamestate):
        self.health = 1
        self.bleed = 0
        self.target.health = 1
        self.target.bleed = 0
        return gamestate

    def understanding(self, gamestate):
        return gamestate

    def contractualism(self, gamestate):
        return gamestate
