# parent
import Character


class Robot(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Robot"
        self.upgrades[0] = "1. Reconstitute: When you are stuck, gain 1 ammo."
        self.upgrades[1] = "2. Positronic Brain: Your attacks no longer hit feet or arms." \
                           "You gain +15% accuracy."
        self.upgrades[2] = "3. Made of Metal: Gain 10 armor."
        self.upgrades[3] = "4. Monstrous Size: Double your current health and max health."
        self.upgrades[4] = "5. Bloodless: You cannot take bleed damage."
        self.upgrades[5] = "6. Pitiless Machine: If your attack would kill a minion, take another shot."

    def reconstitute(self):
        # when you are stuck, gain 1 ammo
        pass

    def positronic_brain(self):
        # Your attacks no longer hit feet or arms. Accuracy +15%.
        self.accuracy += 15
        pass

    def made_of_metal(self):
        # gain 10 armor
        self.armor += 10

    def bloodless(self):
        # you cannot bleed
        pass

    def pitiless(self):
        pass