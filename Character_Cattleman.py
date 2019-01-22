# parent
import Character


class Cattleman(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Cattleman"
        self.upgrades[0] = "1. Bull: Create a Cow minion."
        self.upgrades[1] = "2. Ol' Bessy: The next Cow minion to die will be revived" \
                           " with 3 times as much health and will attack for 15 damage per turn."
        self.upgrades[2] = "3. Herd: Gain 8 cow minions."
        self.upgrades[3] = "4. Plow: Each turn, each Cow heals you for 5 health."
        self.upgrades[4] = "5. Breeder: For each pair of Cows, create 1 new Cow minion."
        self.upgrades[5] = "6. ."

    def bull(self):
        # a Cow minion appears on your side. It will attack
        # for 5 each turn and if it hits your opponent
        # they will miss.
        pass

    def ol_bessy(self):
        # the next Cow minion to die will be revived with 3
        # times as much health and will attack for 15 damage per turn.
        pass

    def purchase(self):
        # gain 8 Cow minions. They do not attack and do not have to be targeted.
        pass

    def put_to_work(self):
        # gain 5 health per Cow minion. They all die.
        pass

    def breeder(self):
        # for each pair of Cow minions, create a new Cow minion.
        pass

    def russle(self):
        # each time you are hit lose a control of a Cow minion
        # attacks made against characters who control Cow minions
        # do 15% more damage per Cow minion.
        pass
