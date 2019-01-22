# parent
import Character

# 5 abilities left
class Doctor(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Doctor"
        self.upgrades.append("Bandage:\n\t Remove all stacks of bleeding from yourself.")
        self.upgrades.append("Reputation:\n\t Minions will not attack you.")
        self.upgrades.append("Triage:\n\t All friendly characters heal" \
                          " each turn equal to their current number of bleeds.")
        self.upgrades.append("Quarantine:\n\t instead of firing," \
                          " you may choose instead to remove yourself from combat and heal for 20 damage.")
        self.upgrades.append("Infectious:\n\t Every opponent gains 5 stacks of bleeding")
        self.upgrades.append("Surgery:\n\t Heal yourself for 75 health.")

        self.upgrade_dict["Bandage:\n\t Remove all stacks of bleeding from yourself."] = 1
        self.upgrade_dict["Reputation:\n\t Minions will not attack you."] = 2
        self.upgrade_dict["Triage:\n\t All friendly characters heal" \
                          " each turn equal to their current number of bleeds."] = 3
        self.upgrade_dict["Quarantine:\n\t instead of firing," \
                          " you may choose instead to remove yourself from combat and heal for 20 damage."] = 4
        self.upgrade_dict["Infectious:\n\t Every opponent gains 5 stacks of bleeding."] = 5
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
        # Remove all stacks of bleeding from yourself.
        self.bleed = 0

    def reputation(self, gamestate):
        # minions will not attack you.
        pass

    def triage(self, gamestate):
        # At the beginning of each turn,
        # all friendly characters heal each turn equal to their current number of bleeds.
        pass

    def quarantine(self, gamestate):
        # instead of firing, you may choose instead to remove yourself from combat and heal for 20 damage.
        pass

    def infectious(self, gamestate):
        # Every opponent gains 5 stacks of bleeding
        pass

    def surgery(self, gamestate):
        # Heal yourself for 75 health."
        self.heal(75)