# parent
import Character


# 6 abilities left
class Gambler(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Gambler"
        self.upgrades.append("Fold:\n\t You may choose to intentionally miss. This does not cost ammo.")
        self.upgrades.append("Better Hand:\n\t Hitting your opponent in the hand allows you to fire again.")
        self.upgrades.append("Reroll:\n\t TBA.")
        self.upgrades.append("Straight:\n\t If you ever hit: Hands, Arms, and Chest or Feet, Legs, Chest - then you win.")
        self.upgrades.append("Pair:\n\t If you hit the same body part twice it does double damage.")
        self.upgrades.append("Coin Flip:\n\t Your next shot will hit either your target's head or feet.")

        self.upgrade_dict["Fold:\n\t You may choose to intentionally miss. This does not cost ammo."] = 1
        self.upgrade_dict["Better Hand:\n\t Hitting your opponent in the hand allows you to fire again."] = 2
        self.upgrade_dict["Reroll:\n\t TBA."] = 3
        self.upgrade_dict["Straight:\n\t If you ever hit: Hands, Arms, and Chest or Feet, Legs, Chest - then you win."] = 4
        self.upgrade_dict["Pair:\n\t If you hit the same body part twice it does double damage."] = 5
        self.upgrade_dict["Coin Flip:\n\t Your next shot will hit either your target's head or feet."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.fold()
        elif choice == 2:
            self.better_hand()
        elif choice == 3:
            self.reroll()
        elif choice == 4:
            self.straight()
        elif choice == 5:
            self.pair()
        elif choice == 6:
            self.coin_flip()
        else:
            print("ERROR APPLYING UPGRADE")

    def fold(self):
        # You may choose to intentionally miss. This does not cost ammo.
        pass

    def better_hand(self):
        # hitting your opponent in the hand gives you an extra shot
        pass

    def reroll(self):
        pass

    def straight(self):
        # if you ever hit: Hands, Arms, and Chest or
        # Feet, Legs, Chest - then you win
        pass

    def pair(self):
        # if you hit the same body part twice it does double damage
        pass

    def coin_flip(self):
        # your next shot will hit either your target's head or feet.
        # or miss
        pass