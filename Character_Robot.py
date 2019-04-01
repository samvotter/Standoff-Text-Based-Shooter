# parent
import Character


class Robot(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Robot"
        self.upgrades.append("1. Reconstitute:\n\t When you are stuck, gain 1 ammo.")
        self.upgrades.append("2. Positronic Brain:\n\t Your attacks no longer hit feet or arms." \
                           "You gain +15% accuracy.")
        self.upgrades.append("3. Made of Metal:\n\t Gain 10 armor.")
        self.upgrades.append("4. TBA.")
        self.upgrades.append("5. Bloodless:\n\t You cannot take bleed damage.")
        self.upgrades.append("6. Pitiless Machine:\n\t If your attack would kill a minion, take another shot." \
                          "It does +50% more damage.")

        self.recyle_switch = False
        self.bleed_switch = False
        self.brain_switch = False

        self.upgrade_dict["1. Reconstitute:\n\t When you are stuck, gain 1 ammo."] = 1
        self.upgrade_dict["2. Positronic Brain:\n\t Your attacks no longer hit feet or arms." \
                           "You gain +15% accuracy."] = 2
        self.upgrade_dict["3. Made of Metal:\n\t Gain 10 armor."] = 3
        self.upgrade_dict["4. TBA."] = 4
        self.upgrade_dict["5. Bloodless:\n\t You cannot take bleed damage."] = 5
        self.upgrade_dict["6. Pitiless Machine:\n\t If your attack would kill a minion, take another shot." \
                          "It does +50% more damage."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.reconstitute(gamestate)
            return gamestate
        elif choice == 2:
            self.positronic_brain(gamestate)
            return gamestate
        elif choice == 3:
            self.made_of_metal(gamestate)
            return gamestate
        elif choice == 4:
            return gamestate
        elif choice == 5:
            self.bloodless(gamestate)
            return gamestate
        elif choice == 6:
            self.pitiless(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def reconstitute(self, gamestate):
        # when you are stuck, gain 1 ammo
        self.recyle_switch = True
        return gamestate

    def positronic_brain(self, gamestate):
        # Your attacks no longer hit feet or arms. Accuracy +15%.
        self.brain_switch = True
        self.accuracy += 15
        return gamestate

    def made_of_metal(self, gamestate):
        # gain 10 armor
        self.armor += 10
        return gamestate

    def bloodless(self, gamestate):
        # you cannot bleed
        self.bleed_switch = True
        return gamestate

    def pitiless(self, gamestate):
        return gamestate

    def bleeds(self):
        # if the target is alive . . .
        if self.alive is True:
            # and bleeding . . .
            if self.bleed_switch is True:
                return False
            if self.bleed > 0:
                # then they take damage
                self.health -= self.bleed
                return True
            else:
                return False
        else:
            return False