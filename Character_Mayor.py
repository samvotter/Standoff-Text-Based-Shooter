# parent
import Character


class Mayor(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Mayor"
        self.upgrades.append("Election:\n\t At the end of the next three turns, "
                             "the team who has dealt the most damage wins.")
        self.upgrades.append("Rally:\n\t Friendly characters gain +6 ammo.")
        self.upgrades.append("Pander:\n\t Gain 15 shields and 2 armor per opponent.")
        self.upgrades.append("Appoint:\n\t ")
        self.upgrades.append("Horse Trading:\n\t Lose any number of votes and heal yourself"
                             "for half that amount, or, hurt yourself and gain three times that many votes.")
        self.upgrades.append("Policy:\n\t ")

        self.left_damage = 0
        self.right_damage = 0

        self.upgrade_dict["Election:\n\t "] = 1
        self.upgrade_dict["Rally:\n\t "] = 2
        self.upgrade_dict["Pander:\n\t "] = 3
        self.upgrade_dict["Appoint:\n\t TBA"] = 4
        self.upgrade_dict["Horse Trading:\n\t TBA"] = 5
        self.upgrade_dict["Policy:\n\t "] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.bigger_gun(gamestate)
            return gamestate
        elif choice == 2:
            self.pa(gamestate)
            return gamestate
        elif choice == 3:
            self.dumb_luck(gamestate)
            return gamestate
        elif choice == 4:
            self.liquid_courage(gamestate)
            return gamestate
        elif choice == 5:
            self.grapple(gamestate)
            return gamestate
        elif choice == 6:
            self.spread(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def monument(self):
        # Create a Monument minion that is a copy of yourself as you are right now.
        # Will only activate on your death.
        pass

    def sash(self):
        # Gain three armor. Remove any debuffs applied by an opponent's upgrade affecting your character.
        pass

    def incumbency(self):
        # Every turn, all opponents lose -4% accuracy
        pass

    def demagoguery(self):
        # all minions heal you for 4 health every turn.
        pass

    def buying_votes(self):
        # You may choose to lose X amount of health to gain +X amount of accuracy.
        swap = input("How much health would you like to trade for accuracy?")
        self.health -= swap
        self.accuracy += swap

    def consensus(self):
        # Anytime you and target opponent hit the same body part, all damage is negated.
        pass