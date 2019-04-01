# parent
import Minion

class GA(Minion.Minion):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.last = "Graduate Assistant"
        self.faction = "Innocent"

        self.health = 1

    def does_thing(self, gamestate):
        self.parent.shields += 10
