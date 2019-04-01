# parent
import Character


# 5 abilities left
class Doctor(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Doctor"
        self.upgrades.append("Bandage:\n\t Remove all stacks of bleeding from yourself.")
        self.upgrades.append("Reputation:\n\t Minions will not attack you.")
        self.upgrades.append("Triage:\n\t All friendly characters heal "
                             "each turn equal to their bleeding this turn.")
        self.upgrades.append("Quarantine:\n\t instead of firing, "
                             "you may choose instead to remove yourself from combat and heal for 20 damage.")
        self.upgrades.append("Infectious:\n\t Every opponent gains 5 stacks of bleeding")
        self.upgrades.append("Surgery:\n\t Heal yourself for 75 health.")

        self.triage_switch = False
        self.triage_dict = {}
        self.quarantine_switch = False

        self.upgrade_dict["Bandage:\n\t Remove all stacks of bleeding from yourself."] = 1
        self.upgrade_dict["Reputation:\n\t Minions will not attack you."] = 2
        self.upgrade_dict["Triage:\n\t All friendly characters heal "
                             "each turn equal to their bleeding this turn."] = 3
        self.upgrade_dict["Quarantine:\n\t instead of firing, "
                             "you may choose instead to remove yourself from combat and heal for 20 damage."] = 4
        self.upgrade_dict["Infectious:\n\t All opponents gain 5 stacks of bleeding."] = 5
        self.upgrade_dict["Surgery:\n\t Heal yourself for 75 health."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.bandage(gamestate)
        elif choice == 2:
            self.reputation(gamestate)
        elif choice == 3:
            self.triage(gamestate)
        elif choice == 4:
            self.quarantine(gamestate)
        elif choice == 5:
            self.infectious(gamestate)
        elif choice == 6:
            self.surgery(gamestate)
        else:
            print("ERROR APPLYING UPGRADE")

    def bandage(self, gamestate):
        self.bleed = 0
        return gamestate

    def reputation(self, gamestate):
        # minions will not attack you.
        pass

    def triage(self, gamestate):
        self.triage_switch = True
        if self.side == "L":
            for character in gamestate.left_side:
                self.triage_dict[character.get_name()] = character.bleed
        elif self.side == "R":
            for character in gamestate.right_side:
                self.triage_dict[character.get_name()] = character.bleed
        return gamestate

    def turn_start(self, gamestate):
        if self.side == "L":
            for character in gamestate.left_side:
                character.heal(self.triage_dict[character.get_name()])
        elif self.side == "R":
            for character in gamestate.right_side:
                character.heal(self.triage_dict[character.get_name()])
        return gamestate

    # still needs to protect character from incoming attacks
    def quarantine(self, gamestate):
        self.quarantine_switch = True
        return gamestate

    def attack(self, victim):
        result = []
        if self.quarantine_switch is True:
            self.heal(20)
            result.append([self.target, None, None, None])
            print("But", self.get_name(), "instead chose to sit this round out.")
            self.quarantine_switch = False
            return result
        if self.wait > 0:
            result.append([self.target, None, None, None])
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            return result
        # if fire returns true
        if self.fire() is True:
            print('*BANG!*', end='')
            if self.hits(victim) is True:
                print("- The shot hit!")
                result.append([self.target, self.pick_bodypart(), self.damage, self.bleed_dmg])
                return result
            else:
                result.append([self.target, None, None, None])
                print("- The shot missed!")
                return result
        else:
            result.append([self.target, None, None, None])
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            return result

    def infectious(self, gamestate):
        if self.side == "L":
            for character in gamestate.right_side:
                character.bleed += 5
        elif self.side == "R":
            for character in gamestate.right_side:
                character.bleed += 5
        return gamestate

    def surgery(self, gamestate):
        self.heal(75)
        return gamestate