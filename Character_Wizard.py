# parent
import Character

# 3 abilities left
class Cowboy(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Cowboy"
        self.upgrades.append("Pyromaniac:\n\t Your attacks apply 2 stacks of burning.")
        self.upgrades.append("Deep Freeze:\n\t All opponents are frozen for 1 turn.")
        self.upgrades.append("Chain Lightning:\n\t Your next attack does full damage to up to 3 targets.")
        self.upgrades.append("Invisible Shroud:\n\t Each turn gain 10 avoidance.")
        self.upgrades.append("Patronum:\n\t Each character on your side gains 20 shields.")
        self.upgrades.append("Transfigure:\n\t Reduce taget's damage by 15 for 2 turns.")

        self.pyro_switch = False
        self.chain_switch = False
        self.shroud_switch = False
        self.trans_duration = 0
        self.saved_damage = 0

        self.upgrade_dict["Pyromaniac:\n\t Your attacks apply 2 stacks of burning."] = 1
        self.upgrade_dict["Deep Freeze:\n\t All opponents are frozen for 1 turn."] = 2
        self.upgrade_dict["Chain Lightning:\n\t Your next attack does full damage to up to 3 targets."] = 3
        self.upgrade_dict["Invisible Shroud:\n\t Each turn gain 10 avoidance."] = 4
        self.upgrade_dict["Patronum:\n\t Each character on your side gains 20 shields."] = 5
        self.upgrade_dict["Transfigure:\n\t Reduce taget's damage by 15 for 2 turns."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.pyro(gamestate)
            return gamestate
        elif choice == 2:
            self.freeze(gamestate)
            return gamestate
        elif choice == 3:
            self.chain(gamestate)
            return gamestate
        elif choice == 4:
            self.shroud(gamestate)
            return gamestate
        elif choice == 5:
            self.patronum(gamestate)
            return gamestate
        elif choice == 6:
            self.trans(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def pryo(self, gamestate):
        self.pyro_switch = True
        return gamestate

    def freeze(self, gamestate):
        if self.side == "L":
            for character in gamestate.right_side:
                character.wait += 1
        else:
            for character in gamestate.left_side:
                character.wait += 1

    def chain(self, gamestate):
        self.chain_switch = True
        return gamestate

    def shroud(self, gamestate):
        self.shroud_switch = True
        return gamestate

    def patronum(self, gamestate):
        if self.side == "L":
            for character in gamestate.left_side:
                character.shields += 20
        else:
            for character in gamestate.right_side:
                character.shields += 20
        return gamestate

    def trans(self, gamestate):
        self.trans_duration = gamestate.turn + 2
        self.saved_damage = self.target.damage
        self.target.damage -= 10
        return gamestate

    def turn_start(self, gamestate):
        if self.shroud_switch is True:
            self.avoidance += 10
        return gamestate

    def before_combat(self, gamestate):
        if gamestate.turn == self.trans_duration:
            self.target.damage = self.saved_damage
        return gamestate
