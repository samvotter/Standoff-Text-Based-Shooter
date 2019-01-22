# parent
import Character


class Mayor(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Mayor"

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