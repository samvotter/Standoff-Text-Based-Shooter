# parent
import Minion

class Child(Minion.Minion):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.last = "Child"

    def does_thing(self, gamestate):
        if self.parent.side == "L":
            for character in gamestate.right_side:
                if character.target == self.parent:
                    character.target = self
        else:
            for character in gamestate.left_side:
                if character.target == self.parent:
                    character.target = self

    def get_alive(self):
        if self.health > 0:
            return True
        else:
            self.parent.damage += 10
            print(self.get_name(), "died tragicly!", self.parent.get_name(), "flew into a rage, gaining +10 damage.")
            self.parent.minions.remove(self)
            return False
