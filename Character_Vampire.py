# parent
import Character


# 6 abilities left
class Vampire(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Vampire"
        self.upgrades.append("Hypnosis:\n\t Retarget incoming attack to any target other than the shooter.")
        self.upgrades.append("Trance:\n\t Change the target of an opponent's attack.")
        self.upgrades.append("Blood Sucker:\n\t Heal for half the damage you inflict.")
        self.upgrades.append("Turn:\n\t Minions you kill return under your control.")
        self.upgrades.append("Sparkle:\n\t On even turns gain 20 shields.")
        self.upgrades.append("Must Be Staked:\n\t If the attack which would kill you is not in the chest,"
                             " it does not kill you.")

        self.upgrade_dict["Hypnosis:\n\t Retarget incoming attack to any target other than the shooter."] = 1
        self.upgrade_dict["Trance:\n\t Change the target of an opponent's attack."] = 2
        self.upgrade_dict["Blood Sucker:\n\t Heal for half the damage you inflict."] = 3
        self.upgrade_dict["Turn:\n\t Minions you kill return under your control."] = 4
        self.upgrade_dict["Sparkle:\n\t On even turns gain 20 shields."] = 5
        self.upgrade_dict["Must Be Staked:\n\t If the attack which would kill you is not in the chest,"
                             " it does not kill you."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.hypnosis()
        elif choice == 2:
            self.trance()
        elif choice == 3:
            self.blood_sucker()
        elif choice == 4:
            self.turn()
        elif choice == 5:
            self.sparkle()
        elif choice == 6:
            self.must_be_staked()
        else:
            print("ERROR APPLYING UPGRADE")

    def hypnosis(self):
        # retarget incoming attack to any target other than the shooter.
        pass

    def trance(self):
        # change the target of an opponent's attack
        pass

    def blood_sucker(self):
        # heal for half the damage you inflict
        pass

    def turn(self):
        # minions you kill return under your control
        pass

    def sparkle(self):
        # on even turns gain 20 shields
        pass

    def must_be_staked(self):
        # if the attack which would kill you is not in the chest, it does not kill you.
        pass
