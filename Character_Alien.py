# parent
import Character


class Alien(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Alien"
        self.upgrades.append("Reactive Design:\n\t If you take damage on a specific body part, the next time that "
                             "spot would take damage, ignore that damage.")
        self.upgrades.append("Slow Shield:\n\t Gain 100 shields.")
        self.upgrades.append("Abduct:\n\t You and target character leave the battlefield for 3 turns.")
        self.upgrades.append("Probe:\n\t TBA.")
        self.upgrades.append("Set to Stun:\n\t your hits cause enemies to lose their next turn. "
                             "This cannot happen twice in a row.")
        self.upgrades.append("Future Tech:\n\t Your successful attacks always do 10 more damage "
                             "than they otherwise would.")

        self.reactive_switch = False
        self.reactive_parts = []
        self.stun_switch = False
        self.future_switch = False

        self.upgrade_dict["Reactive Design:\n\t If you take damage on a specific body part, the next time that "
                             "spot would take damage, ignore that damage."] = 1
        self.upgrade_dict["Slow Shield:\n\t Gain 100 shields."] = 2
        self.upgrade_dict["Abduct:\n\t You and target character leave the battlefield for 3 turns."] = 3
        self.upgrade_dict["Probe:\n\t TBA."] = 4
        self.upgrade_dict["Set to Stun:\n\t your hits cause enemies to lose their next turn. "
                             "This cannot happen twice in a row."] = 5
        self.upgrade_dict["Future Tech:\n\t Your successful attacks always do 10 more damage "
                             "than they otherwise would."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.reactive_design(gamestate)
            return gamestate
        elif choice == 2:
            self.slow_shield(gamestate)
            return gamestate
        elif choice == 3:
            self.abduct(gamestate)
            return gamestate
        elif choice == 4:
            self.probe(gamestate)
            return gamestate
        elif choice == 5:
            self.set_to_stun(gamestate)
            return gamestate
        elif choice == 6:
            self.future_tech(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def reactive_design(self, gamestate):
        self.reactive_switch = True
        return gamestate

    def slow_shield(self, gamestate):
        self.shields += 100
        return gamestate

    def abduct(self, gamestate):
        return gamestate

    def probe(self, gamestate):
        return gamestate

    def set_to_stun(self, gamestate):
        self.stun_switch = True
        return gamestate

    def future_tech(self, gamestate):
        return

    def take_damage(self, result):
        if result[2] is None:
            print(self.get_name(), "took no damage.")
            return False
        else:
            if result[1] in self.reactive_parts:
                print(self.get_name(), "took no damage.")
                self.reactive_parts.remove(result[1])
                return False
            elif result[1] == "Chest":
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
            if self.reactive_switch:
                self.reactive_parts.append(result[1])
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



