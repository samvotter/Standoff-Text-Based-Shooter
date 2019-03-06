# parent
import Character


class Doughboy(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Doughboy"
        self.upgrades.append("Entrench:\n\t Reduce all enemy accuracy by 20%.")
        self.upgrades.append("Field Rations:\n\t Every 2 turns, heal for 20.")
        self.upgrades.append("Reload:\n\t It takes as many turns as you are bleeding to fully reload.")
        self.upgrades.append("TBA:\n\t ")
        self.upgrades.append("TBA:\n\t .")
        self.upgrades.append("TBA:\n\t ..")

        self.rations_switch = False
        self.rations_counter = 2
        self.reload_switch = False
        self.reload_wait = None

        self.upgrade_dict["Entrench:\n\t Reduce all enemy accuracy by 20%."] = 1
        self.upgrade_dict["Field Rations:\n\t Every 2 turns, heal for 20."] = 2
        self.upgrade_dict["Reload:\n\t It takes as many turns as you are bleeding to fully reload."] = 3
        self.upgrade_dict["TBA:\n\t "] = 4
        self.upgrade_dict["TBA:\n\t ."] = 5
        self.upgrade_dict["TBA:\n\t .."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.entrench(gamestate)
            return gamestate
        elif choice == 2:
            self.field_rations(gamestate)
            return gamestate
        elif choice == 3:
            self.reload(gamestate)
            return gamestate
        elif choice == 4:
            return gamestate
        elif choice == 5:
            return gamestate
        elif choice == 6:
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def entrench(self, gamestate):
        # reduce enemy accuracy by -20% accuracy.
        if self.side == "L":
            for character in gamestate.right_side:
                character.accuracy -= 20
        elif self.side == "R":
            for character in gamestate.left_side:
                character.accuracy -= 20
        return gamestate

    def field_rations(self, gamestate):
        # every 2 turns heal for 20
        self.rations_switch = True
        return gamestate

    def turn_start(self, gamestate):
        if self.rations_switch is True:
            if self.side == "L":
                self.rations_counter -= 1
                if self.rations_counter <= 0:
                    self.heal(20)
                    self.rations_counter = 2
        return gamestate

    def reload(self, gamestate):
        # It takes you as many turns as you are bleeding to
        # fully reload your weapon
        self.reload_switch = True
        return gamestate

    def turn_start(self, gamestate):
        if self.reload_switch is True:
            self.reload_wait = self.bleed
        if self.ammo <= 0:
            self.reload_switch = False
            self.reload_wait -= 1
        if self.reload_wait <= 0:
            self.ammo += 6
            self.reload_switch = True
        return gamestate