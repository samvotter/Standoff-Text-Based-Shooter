# parent
import Character


class Doughboy(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Doughboy"

    def entrench(self):
        # reduce enemy accuracy by -20% accuracy. gain 5 armor
        self.armor += 5
        pass

    def field_rations(self):
        # every 3 turns heal for 20
        self.heal(20)
        pass

    def reload(self):
        # It takes you as many turns as you are bleeding to
        # fully reload your weapon
        pass