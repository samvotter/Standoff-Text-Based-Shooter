# parent
import Character


class Diplomat(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Diplomat"
        self.upgrades[0] = "Common Foe: Create a Common Foe minion with health equal to" \
                           " the combined health of all characters. " \
                           "All characters must target this minion if able."
        self.upgrades[1] = "Cease Fie: The results of this turn will be applied after combat next turn."
        self.upgrades[2] = "Productive Dialogue: If you and your target both miss, both of you heal for 50."
        self.upgrades[3] = "Brinksmanship: Reduce your health and the health of your target to 1. " \
                           "Cure all bleeding on yourself and your target."
        self.upgrades[4] = "TBA: ."
        self.upgrades[5] = "Contractualism: If you would be healed, so is target. If you take damage, so does target."

    def common_foe(self):
        # create a Common Foe minion with health equal to twice
        # the combined health of all characters.
        # All characters must target this minion. If the minion
        # dies, you win.
        pass

    def cease_fire(self):
        # if both you and your opponent miss, fully heal.
        self.heal(100)
        pass

    def dialogue(self):
        # if you miss 3 times, you win.
        pass

    def shrewd_negotiator(self):
        # if you would take damage this turn, instead
        # your opponent takes this damage
        pass

    def understanding(self):
        # if both you and your opponent hit, both characters ignore damage
        pass

    def same_footing(self):
        # if your opponent has less than 15 health more than you
        # your health total is equal to your opponents
        pass
