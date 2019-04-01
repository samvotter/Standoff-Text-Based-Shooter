# parent
import Character
import copy as c


class Zombie(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Zombie"
        self.upgrades.append("Bony Fingers:\n\t Being shot in the Hands or Arms does not reduce accuracy.")
        self.upgrades.append("Strength in Numbers:\n\t Lose half your health and half your damage," \
                           " gain 1 Zombie minion for each 10 health you lost. Zombies are exact copies of yourself.")
        self.upgrades.append("The Brain:\n\t You do not take damage anywhere but from headshots." \
                           "You still receive bleeding and headshots instantly kill you.")
        self.upgrades.append("Bite:\n\t Target gains 6 stacks of bleeding.")
        self.upgrades.append("TBA . . ")
        self.upgrades.append("TBA . . .")

        self.brain_switch = False
        self.bony_switch = False

        self.upgrade_dict["Bony Fingers:\n\t Being shot in the Hands or Arms does not reduce accuracy."] = 1
        self.upgrade_dict["Strength in Numbers:\n\t Lose half your health and half your damage," \
                           " gain 1 Zombie minion for each 10 health you lost. Zombies are exact copies of yourself."] = 2
        self.upgrade_dict["The Brain:\n\t You do not take damage anywhere but from headshots." \
                           "You still receive bleeding and headshots instantly kill you."] = 3
        self.upgrade_dict["Bite:\n\t Target gains 6 stacks of bleeding."] = 4
        self.upgrade_dict["TBA . . "] = 5
        self.upgrade_dict["TBA . . ."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.bony_fingers(gamestate)
            return gamestate
        elif choice == 2:
            self.strength_in_numbers(gamestate)
            return gamestate
        elif choice == 3:
            return gamestate
        elif choice == 4:
            self.bite(gamestate)
            return gamestate
        elif choice == 5:
            return gamestate
        elif choice == 6:
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def bony_fingers(self, gamestate):
        # being shot in the hands does not reduce accuracy
        self.bony_switch = True
        return gamestate

    def strength_in_numbers(self, gamestate):
        # Lose half your health and 3/5ths of your damage, gain 1 minion for each 10 health you lost.
        # minions are exact copies of yourself.
        loss = int((self.health/2)/10)
        self.health /= 2
        self.damage *= (2 / 5)
        if self.side == "L":
            for i in range(0, loss):
                new = c.deepcopy(self)
                new.minion = True
                gamestate.left_side.append(new)
        else:
            for i in range(0, loss):
                new = c.deepcopy(self)
                new.minion = True
                gamestate.right_side.append(new)
        return gamestate

    def the_brain(self, gamestate):
        # You do not take damage anywhere but the head.
        # You still recieve bleeding and headshots instantly kill you.
        self.brain_switch = True
        return gamestate

    def bite(self, gamestate):
        # inflict 6 bleeding.
        self.target.bleed += 6
        return gamestate

    def take_damage(self, result):
        if self.brain_switch is False:
            if result[1] == "Chest":
                damage = result[2]
            elif result[1] == "Arms":
                damage = result[2]*(3 / 5)
                self.accuracy *= (9 / 10)
            elif result[1] == "Hands":
                if self.bony_switch is True:
                    damage = result[2] * (1 / 5)
                else:
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
                    print(result[0].get_name(), "was hit in the", result[1], "for", damage)
                    return True
                else:
                    print(self.get_name(), "All damage was blocked!")
                    return False
            # if the target is dead
            else:
                print(self.get_name(), "was dead.")
                return False
        else:
            if result[1] == "Chest":
                damage = 0
            elif result[1] == "Arms":
                damage = 0
                self.accuracy *= (9 / 10)
            elif result[1] == "Hands":
                if self.bony_switch is True:
                    damage = 0
                else:
                    damage = 0
                    self.accuracy /= 2
            elif result[1] == "Legs":
                damage = 0
            elif result[1] == "Feet":
                damage = 0
            elif result[1] == "Head":
                damage = result[2]*2
                self.health = 0
            else:
                damage = 0
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
                    print(result[0].get_name(), "was hit in the", result[1], "for", damage)
                    return True
                else:
                    print(self.get_name(), "All damage was blocked!")
                    return False
            # if the target is dead
            else:
                print(self.get_name(), "was dead.")
                return False
