# parent
import Minion

class Innocent(Minion.Minion):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.last = "Innocent"
        self.faction = "Innocent"
        self.origin = kwargs["origin"]

        self.health = 1

    def get_alive(self):
        if self.health > 0:
            return True
        else:
            print(self.get_name(), "died tragicly!")
            self.origin.minion_deaths += 1
            self.parent.minions.remove(self)
            return False
