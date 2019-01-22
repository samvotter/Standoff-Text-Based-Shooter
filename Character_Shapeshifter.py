# parent
import Character


class Shapeshifter(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Shapeshifter"