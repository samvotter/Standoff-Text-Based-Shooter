# parent
import Character


class Heiress(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Heiress"
        self.upgrades.append("Laudanum:\n\t Gain +10 avoidance and 40 shields. Every turn your shields decay by -5.")
        self.upgrades.append("Aristocrat:\n\t Instead of taking damage,"
                             " you may choose to give 1 ammunition to your attacker.")
        self.upgrades.append("Outlast:\n\t Whenever a character dies, gain all of their unspent ammunition.")
        self.upgrades.append("Refinement:\n\t Gain +6 accuracy every turn.")
        self.upgrades.append("Cash Infusion:\n\t Choose to gain either 20 health, 2 bullets, 5 armor, or 15 shields.")
        self.upgrades.append("Classy:\n\t You may only be targeted by 1 person each turn.")

        self.upgrade_dict["Laudanum:\n\t Gain +10 avoidance and 40 shields. Every turn your shields decay by -5."] = 1
        self.upgrade_dict["Aristocrat:\n\t Instead of taking damage,"
                             " you may choose to give 1 ammunition to your attacker."] = 2
        self.upgrade_dict["Outlast:\n\t Whenever a character dies, gain all of their unspent ammunition."] = 3
        self.upgrade_dict["Refinement:\n\t Gain +6 accuracy every turn."] = 4
        self.upgrade_dict["Cash Infusion:\n\t Choose to gain either 20 health, 2 bullets, 5 armor, or 15 shields."] = 5
        self.upgrade_dict["Classy:\n\t You may only be targeted by 1 person each turn."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.laudanum()
        elif choice == 2:
            self.aristocrat()
        elif choice == 3:
            self.outlast()
        elif choice == 4:
            self.refinement()
        elif choice == 5:
            self.cash_infusion()
        elif choice == 6:
            self.classy()
        else:
            print("ERROR APPLYING UPGRADE")

    def laudanum(self):
        self.avoidance += 10
        self.shields += 40
        #reduce shields by 5 each turn
        pass

    def aristocrat(self):
        pass

    def outlast(self):
        pass

    def refinement(self):
        pass

    def cash_infusion(self):
        print("Select an option:",
              "\t 1. Heal for 20.\n",
              "\t 2. Gain 2 ammo.\n",
              "\t 3. Gain 5 armor.\n",
              "\t 4. Gain 15 shields.\n",)
        choice = input()
        if choice == 1:
            self.heal(20)
        elif choice == 2:
            self.ammo += 2
        elif choice == 3:
            self.armor += 5
        elif choice == 4:
            self.shields += 15

    def classy(self):
        pass