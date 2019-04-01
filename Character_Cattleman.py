# parent
import Character

# child
import Minion_Cattleman as m


class Cattleman(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Cattleman"
        self.upgrades.append("Ol' Bessy:\n\t Create a Cow minion with 45 health and 15 damage. She attacks with you.")
        self.upgrades.append("Herd:\n\t Gain four cow minions. Cows have 15 health.")
        self.upgrades.append("Plow:\n\t Each turn, each Cow minion heals you for 4.")
        self.upgrades.append("Breeder:\n\t Each pair of Cow minions produces an addition cow minion on even turns.")
        self.upgrades.append("Stampede:\n\t Cow minions attack with you for 5 damage each turn.")
        self.upgrades.append("Bull:\n\t Whenever you take damage, create a Cow minion.")

        self.herd_switch = False
        self.breeder_switch = False
        self.stampede_switch = False
        self.bull_switch = False

        self.upgrade_dict["Ol' Bessy:\n\t Create a Cow minion with 45 health and 15 damage. She attacks with you."] = 1
        self.upgrade_dict["Herd:\n\t Gain four cow minions. Cows have 15 health."] = 2
        self.upgrade_dict["Plow:\n\t Each turn, each Cow minion heals you for 4."] = 3
        self.upgrade_dict["Breeder:\n\t Each pair of Cow minions produces an addition cow minion on even turns."] = 4
        self.upgrade_dict["Stampede:\n\t Cow minions attack with you for 5 damage each turn."] = 5
        self.upgrade_dict["Bull:\n\t Whenever you take damage, create a Cow minion."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.bessy(gamestate)
            return gamestate
        elif choice == 2:
            self.herd(gamestate)
            return gamestate
        elif choice == 3:
            self.plow(gamestate)
            return gamestate
        elif choice == 4:
            self.breed(gamestate)
            return gamestate
        elif choice == 5:
            self.stampede(gamestate)
            return gamestate
        elif choice == 6:
            self.bull(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def bessy(self, gamestate):
        # Create a Cow minion with 45 health and 15 damage. She attacks with you."
        self.minions.append(m.Cow(self, health=45, damage=15, last="Bessy"))
        return gamestate

    def herd(self):
        # Gain four cow minions. Cows have 15 health."
        for i in range(0,4):
            self.minions.append(self, health=15)
        return

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
