# parent
import Minion

class Cow(Minion.Minion):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        if "last" in kwargs:
            self.last = kwargs["last"]
        else:
            self.last = "Cow"
        self.faction = "Animal"


    def does_thing(self, gamestate):
        self.parent.shields += 10