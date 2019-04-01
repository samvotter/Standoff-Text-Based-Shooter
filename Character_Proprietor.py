# parent
import Character

# 6 abilities left
class Proprietor(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Proprietor"
        self.upgrades.append("Sell Clothes:\n\t Target opponent gains 5 armor, loses 1 bullet, you gain one bullet.")
        self.upgrades.append("Costly Interactions:\n\t If an opponent hits you, they lose 7 health.")
        self.upgrades.append("Repossess:\n\t Target loses all benefits you may have applied.")
        self.upgrades.append("Sell Eyewear:\n\t Target gains +25% accuracy, loses 2 bullets, you gain 2 bullets.")
        self.upgrades.append("Sell Medicine:\n\t Target heals for 10 health, you gain 40 health.")
        self.upgrades.append("Sell Bullets:\n\t TBA.")

        self.upgrade_dict["Sell Clothes:\n\t Target opponent gains 5 armor, loses 1 bullet, you gain one bullet."] = 1
        self.upgrade_dict["Costly Interactions:\n\t If an opponent hits you, they lose 7 health."] = 2
        self.upgrade_dict["Repossess:\n\t Target loses all benefits you may have applied."] = 3
        self.upgrade_dict["Sell Eyewear:\n\t Target gains +25% accuracy, loses 2 bullets, you gain 2 bullets."] = 4
        self.upgrade_dict["Sell Medicine:\n\t Target heals for 10 health, you gain 40 health."] = 5
        self.upgrade_dict["Sell Bullets:\n\t TBA."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.sell_clothes()
        elif choice == 2:
            self.costly_interactions()
        elif choice == 3:
            self.repossess()
        elif choice == 4:
            self.sell_eyewear()
        elif choice == 5:
            self.sell_medicine()
        elif choice == 6:
            self.sell_bullets()
        else:
            print("ERROR APPLYING UPGRADE")

    def sell_clothes(self):
        # target opponent gains 5 armor, loses 1 bullet, you gain one bullet.
        self.ammo += 1
        pass

    def costly_interactions(self):
        # if an opponent hits you, they lose 7 health.
        pass

    def repossess(self):
        # target loses all benefits you may have applied.
        pass

    def sell_eyewear(self):
        # target gains +25% accuracy, loses 2 bullets, you gain 2 bullets
        self.ammo += 2
        pass

    def sell_medicine(self):
        # Target heals for 10 health, you gain 40 health
        self.heal(40)

    def sell_bullets(self):
        # undecided
        pass