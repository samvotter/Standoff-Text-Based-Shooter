# parent
import Character


# 6 abilities left
class LandBaron(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Land Baron"
        self.upgrades.append("Scorched Earth:\n\t Deal 5 damage to each opponent for each land token you control.")
        self.upgrades.append("Monopoly:\n\t If an other player would gain a minion of any type, you gain 2 land tokens.")
        self.upgrades.append("Harvest:\n\t Gain 30 health per land token.")
        self.upgrades.append("Hire:\n\t Gain one Field Hand minion for each land token."
                             "At the end of each turn, gain one land token for each pair of Field Hand and Land Token.")
        self.upgrades.append("Recapitalize:\n\t TBA.")
        self.upgrades.append("Stake Claim:\n\t When you strike your opponent, gain a land token.")

        self.upgrade_dict["Scorched Earth:\n\t Deal 5 damage to each opponent for each land token you control."] = 1
        self.upgrade_dict["Monopoly:\n\t If an other player would gain a minion of any type, you gain 2 land tokens."] = 2
        self.upgrade_dict["Harvest:\n\t Gain 30 health per land token."] = 3
        self.upgrade_dict["Hire:\n\t Gain one Field Hand minion for each land token."
                             "At the end of each turn, gain one land token for each pair of Field Hand and Land Token."] = 4
        self.upgrade_dict["Recapitalize:\n\t TBA."] = 5
        self.upgrade_dict["Stake Claim:\n\t When you strike your opponent, gain a land token."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.scorched_earth()
        elif choice == 2:
            self.monopoly()
        elif choice == 3:
            self.harvest()
        elif choice == 4:
            self.hire()
        elif choice == 5:
            self.recapitalize()
        elif choice == 6:
            self.stake_claim()
        else:
            print("ERROR APPLYING UPGRADE")

    def scorched_earth(self):
        # deal 5 damage to each opponent for each land token you control.
        pass

    def monopoly(self):
        # if an other player would gain a minion of any type,
        # you gain 2 land tokens
        pass

    def harvest(self):
        # gain 30 health per land token
        pass

    def hire(self):
        # Gain one Field Hand minion for each land token.
        # At the end of each turn, gain one land token for each
        # pair of Field Hand and Land Token
        pass

    def recapitalize(self):
        pass

    def stake_claim(self):
        # when you strike your opponent, gain a land token.
        pass