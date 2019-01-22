# parent
import Character


# 6 abilities left
class Werewolf(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Werewolf"
        self.upgrades.append("Moon Cycles:\n\t On even turns, heal for 5. On odd turns, you do +10 damage.")
        self.upgrades.append("Bloodthirsty:\n\t Attacks heal you for three times the target's amount of bleeding.")
        self.upgrades.append("Ferocity:\n\t Every successful attack increases your damage by 5.")
        self.upgrades.append("Claws:\n\t On odd turns, you do not spend ammo to attack.")
        self.upgrades.append("Rage:\n\t On odd turns, you have 25 shields and 5 armor. Lose these benefits on even turns.")
        self.upgrades.append("Blood God:\n\t Your attacks inflict bleeding equal to the amount you are bleeding.")

        self.upgrade_dict["Moon Cycles:\n\t On even turns, heal for 5. On odd turns, you do +10 damage."] = 1
        self.upgrade_dict["Bloodthirsty:\n\t Attacks heal you for three times the target's amount of bleeding."] = 2
        self.upgrade_dict["Ferocity:\n\t Every successful attack increases your damage by 5."] = 3
        self.upgrade_dict["Claws:\n\t On odd turns, you do not spend ammo to attack."] = 4
        self.upgrade_dict["Rage:\n\t On odd turns, you have 25 shields and 5 armor. Lose these benefits on even turns."] = 5
        self.upgrade_dict["Blood God:\n\t Your attacks inflict bleeding equal to the amount you are bleeding."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.moon_cycles()
        elif choice == 2:
            self.bloodthirsty()
        elif choice == 3:
            self.ferocity()
        elif choice == 4:
            self.claws()
        elif choice == 5:
            self.rage()
        elif choice == 6:
            self.blood_god()
        else:
            print("ERROR APPLYING UPGRADE")

    def moon_cycles(self):
        # on even turns, heal for 5. On odd turns, you do +10 damage.
        pass

    def bloodthirsty(self):
        # Attacks heal you for three times the target's amount of bleeding.
        pass

    def ferocity(self):
        # Every successful attack increases your damage by 5.
        pass

    def claws(self):
        # On odd turns, you do not spend ammo to attack.
        pass

    def rage(self):
        # On odd turns, you have 25 shields and 5 armor. Lose these benefits on even turns.
        pass

    def blood_god(self):
        # Your attacks inflict bleeding equal to the amount you are bleeding.
        pass