# parent
import Character

# 4 abilities left
class Scoundrel(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Scoundrel"
        self.upgrades.append("Flee:\n\t Your attacks, as well as attacks made against you, have a -20% chance to hit.")
        self.upgrades.append("Wanton Cruelty:\n\t Your accuracy is reduced by 50%. Damage is increased by 30%.")
        self.upgrades.append("Cannot Lose:\n\t Your misses create an Innocent minion and hit it instead.")
        self.upgrades.append("Disregard:\n\t Attacks which strike minions also strike target character.")
        self.upgrades.append("Coward:\n\t Create three Innocent minions. Attacks are as likely to hit them as you.")
        self.upgrades.append("Chaos:\n\t If six or more minions die, you win.")

        self.minion_deaths = 0

        self.upgrade_dict["Flee:\n\t Your attacks, as well as attacks made against you, have a -20% chance to hit."] = 1
        self.upgrade_dict["Wanton Cruelty:\n\t Your accuracy is reduced by 50%. Damage is increased by 30%."] = 2
        self.upgrade_dict["Cannot Lose:\n\t Your misses create an Innocent minion and hit it instead."] = 3
        self.upgrade_dict["Disregard:\n\t Attacks which strike minions also strike target character."] = 4
        self.upgrade_dict["Coward:\n\t Create three Innocent minions. Attacks are as likely to hit them as you."] = 5
        self.upgrade_dict["Chaos:\n\t If six or more minions die, you win."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.flee(gamestate)
        elif choice == 2:
            self.wanton_cruelty(gamestate)
        elif choice == 3:
            self.cannot_lose(gamestate)
        elif choice == 4:
            self.disregard(gamestate)
        elif choice == 5:
            self.coward(gamestate)
        elif choice == 6:
            self.chaos(gamestate)
        else:
            print("ERROR APPLYING UPGRADE")

    def flee(self, gamestate):
        # +20% chance attacks made against you will miss, your own accuracy also decreases by -20%
        self.avoidance = 20
        self.accuracy -= 20

    def wanton_cruelty(self, gamestate):
        # Your accuracy is reduced by 50%. Damage is increased by 30%."
        self.accuracy /= 2
        self.damage *= (4/3)

    def cannot_lose(self, gamestate):
        # your misses create an Innocent minion and hit it instead.
        pass

    def disregard(self, gamestate):
        # attacks which strike minions also strike target character
        pass

    def coward(self, gamestate):
        # create three Innocent minions. Attacks are as likely to hit them as you
        # append temp
        pass

    def chaos(self, gamestate):
        # if six or more minions die, you win.
        pass