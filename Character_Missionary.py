# parent
import Character

# 6 abilities left
class Missionary(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Missionary"
        self.upgrades.append("Come to Jesus:\n\t If you are not being targeted, deal twice as much damage.")
        self.upgrades.append("Martyrdom:\n\t Friendly characters heal equal to the damage you take.")
        self.upgrades.append("Guilt:\n\t Opponents you have already hit gain 6 stacks of bleeding.")
        self.upgrades.append("Sermonize:\n\t Until next turn, all players gain 30 avoidance.")
        self.upgrades.append("Tithe:\n\t All opponents give you one bullet or 10% of their maximum health.")
        self.upgrades.append("Pray:\n\t If your next attack hits, the target dies. If it misses, you die.")

        self.jesus_switch = False
        self.jesus_target = False
        self.marty_switch = False
        self.hurt = 0
        self.success_hits = []
        self.release = None
        self.allNone_switch = False
        self.turnOff = None

        self.upgrade_dict["Come to Jesus:\n\t If you are not being targeted, deal twice as much damage."] = 1
        self.upgrade_dict["Martyrdom:\n\t Friendly characters heal equal to the damage you take."] = 2
        self.upgrade_dict["Guilt:\n\t Opponents you have already hit gain 6 stacks of bleeding."] = 3
        self.upgrade_dict["Sermonize:\n\t Until next turn, all players gain 30 avoidance."] = 4
        self.upgrade_dict["Tithe:\n\t All opponents give you one bullet or 10% of their maximum health."] = 5
        self.upgrade_dict["Pray:\n\t If your next attack hits, the target dies. If it misses, you die."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.come_to_jesus(gamestate)
            return gamestate
        elif choice == 2:
            self.martyrdom(gamestate)
            return gamestate
        elif choice == 3:
            self.guilt(gamestate)
            return gamestate
        elif choice == 4:
            self.sermonize(gamestate)
            return gamestate
        elif choice == 5:
            self.tithe(gamestate)
            return gamestate
        elif choice == 6:
            self.pray(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def come_to_jesus(self, gamestate):
        self.jesus_switch = True
        return gamestate

    def martyrdom(self, gamestate):
        self.marty_switch = True
        return gamestate

    def guilt(self, gamestate):
        for victim in self.success_hits:
            victim.bleed += 6
        return gamestate

    def sermonize(self, gamestate):
        self.release = gamestate.turn + 1
        for char in gamestate.left_side:
            char.avoidance += 30
        for char in gamestate.right_side:
            char.avoidance += 30
        return gamestate

    def tithe(self, gamestate):
        for char in gamestate.left_side:
            if char != self:
                char.ammo -= 1
                hpTransfer = char.health / 10
                char.health *= (9 / 10)
                self.ammo += 1
                self.heal(hpTransfer)
        for char in gamestate.right_side:
            if char != self:
                char.ammo -= 1
                hpTransfer = char.health / 10
                char.health *= (9 / 10)
                self.ammo += 1
                self.heal(hpTransfer)
        return gamestate

    def pray(self, gamestate):
        self.allNone_switch = True
        self.turnOff = gamestate.turn + 1
        return gamestate

    def turn_start(self, gamestate):
        if gamestate.turn == self.turnOff:
            self.allNone_switch = False
        if gamestate.turn == self.release:
            for char in gamestate.left_side:
                char.avoidance -= 30
            for char in gamestate.right_side:
                char.avoidance -= 30
        return gamestate

    def before_combat(self, gamestate):
        self.jesus_target = False
        if self.jesus_switch is True:
            for characters in gamestate.left_side:
                if characters.target == self:
                    self.jesus_target = True
            for characters in gamestate.right_side:
                if characters.target == self:
                    self.jesus_target = True

    def attack(self, victim):
        result = []
        if self.wait > 0:
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            return result
        # if fire returns true
        if self.fire() is True:
            print('*BANG!*', end='')
            if self.hits(victim) is True:
                if self.allNone_switch is True:
                    self.target.health = 0
                    print("- The shot hit!")
                    return result
                else:
                    self.success_hits.append(self.target)
                    if self.jesus_target is True:
                        print("- The shot hit!")
                        result.append([self.target, self.pick_bodypart(), self.damage*2, self.bleed_dmg])
                        return result
                    else:
                        print("- The shot hit!")
                        result.append([self.target, self.pick_bodypart(), self.damage, self.bleed_dmg])
                        return result
            else:
                if self.allNone_switch is True:
                    self.health = 0
                    print("- The shot missed!")
                    return result
                else:
                    result.append([self.target, "Miss"])
                    print("- The shot missed!")
                    return result
        else:
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            return result

    def take_damage(self, result):
        if result[2] is None:
            print(self.get_name(), "took no damage.")
            return False
        else:
            if result[1] == "Chest":
                damage = result[2]
            elif result[1] == "Arms":
                damage = result[2]*(3 / 5)
                self.accuracy *= (9 / 10)
            elif result[1] == "Hands":
                damage = result[2] * (1 / 5)
                self.accuracy /= 2
            elif result[1] == "Legs":
                damage = result[2] * (3 / 5)
            elif result[1] == "Feet":
                damage = result[2] * (1 / 5)
            elif result[1] == "Head":
                damage = result[2] * 2
            else:
                damage = result[2]
            # if the target is alive . . .
            reduce = damage
            if self.alive is True:
                # and they have shields . . .
                if self.shields > 0:
                    # shields reduce incoming damage by a percentage.
                    damage *= (100-self.shields)/100
                    self.shields -= reduce
                    if self.shields < 0:
                        self.shields = 0
                # and if they have armor
                if self.armor > 0:
                    # armor reduces incoming damage by a flat amount.
                    damage -= self.armor
                # and not all of it was blocked
                if damage > 0:
                    self.health -= damage
                    self.bleed += result[3]
                    self.hurt = damage
                    print(result[0].get_name(), "was hit in the", result[1], "for", damage)
                    return True
                else:
                    print(self.get_name(), "All damage was blocked!")
                    return False
            # if the target is dead
            else:
                print(self.get_name(), "was dead.")
                return False

    def after_combat(self, gamestate):
        if self.marty_switch is True:
            if self.side == "L":
                for character in gamestate.left_side:
                    character.heal(self.hurt)
            else:
                for character in gamestate.right_side:
                    character.heal(self.hurt)
        return gamestate