# parent
import Character


class Zombie(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Zombie"
        self.upgrades[0] = "1. Bony Fingers: Being shot in the Hands or Arms does not reduce accuracy."
        self.upgrades[1] = "2. Strength in Numbers: Lose half your health and half your damage," \
                           " gain 1 Zombie minion for each 10 health you lost. Zombies are exact copies of yourself."
        self.upgrades[2] = "3. The Brain: You do not take damage anywhere but from headshots." \
                           "You still receive bleeding and headshots instantly kill you."
        self.upgrades[3] = "4. Bite: Target gains 10 stacks of bleeding."
        self.upgrades[4] = "5. ."
        self.upgrades[5] = "6. ."

    def bony_fingers(self):
        # being shot in the hands does not reduce accuracy
        pass

    def strength_in_numbers(self):
        # Lose half your health and half your damage, gain 1 minion for each 10 health you lost
        # minions are exact copies of yourself.
        pass

    def the_brain(self):
        # You do not take damage anywhere but the head.
        # You still recieve bleeding and headshots instantly kill you.
        pass

    def bite(self, target):
        # inflict 10 bleeding.
        target.change_bleed(10)
        pass