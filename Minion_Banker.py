# parent
import Minion


class Account(Minion.Minion):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.last = "Account"
        self.faction = "Innocent"
        self.health = 10

        self.health = 1

    def does_thing(self, gamestate):
        pass
