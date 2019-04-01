# parent
import Character


# 6 abilities left
class NativeAmerican(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Native American"
        self.upgrades.append("Virgin Land:\n\t The upgrade card your opponent chooses"
                             " this turn provides the opposite effect.")
        self.upgrades.append("Culture Destroyed:\n\t 8 Relative minions appear. Each turn 1 Relative minion dies."
                             "If there are no Relatives left, you win.")
        self.upgrades.append("Alien Diseases:\n\t When you die, you inflict 25 damage on all opponents."
                             " If this damage would kill them, you win the game.")
        self.upgrades.append("Foreign Invasion:\n\t Minions your opponents control deal damage"
                             " equal to their current health to their master.")
        self.upgrades.append("Forced Resettlement:\n\t When you gain a stack of bleeding,"
                             " all opponents gain twice as many stacks.")
        self.upgrades.append("Dishonest Treaties:\n\t Give all your ammo to target opponent. "
                             "If you die from being stuck by one of those bullets, you win.")

        self.upgrade_dict["Virgin Land:\n\t The upgrade card your opponent chooses"
                             " this turn provides the opposite effect."] = 1
        self.upgrade_dict["Culture Destroyed:\n\t 8 Relative minions appear. Each turn 1 Relative minion dies."
                             "If there are no Relatives left, you win."] = 2
        self.upgrade_dict["Alien Diseases:\n\t When you die, you inflict 25 damage on all opponents."
                             " If this damage would kill them, you win the game."] = 3
        self.upgrade_dict["Foreign Invasion:\n\t Minions your opponents control deal damage"
                             " equal to their current health to their master."] = 4
        self.upgrade_dict["Forced Resettlement:\n\t When you gain a stack of bleeding,"
                             " all opponents gain twice as many stacks."] = 5
        self.upgrade_dict["Dishonest Treaties:\n\t Give all your ammo to target opponent. "
                             "If you die from being stuck by one of those bullets, you win."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.virgin_land()
        elif choice == 2:
            self.culture_destroyed()
        elif choice == 3:
            self.alien_diseases()
        elif choice == 4:
            self.foreign_invasion()
        elif choice == 5:
            self.forced_resettlement()
        elif choice == 6:
            self.dishonest_treaties()
        else:
            print("ERROR APPLYING UPGRADE")

    def virgin_land(self):
        # The upgrade card your opponent chooses this turn
        # provides the opposite effect.
        pass

    def culture_destroyed(self):
        # 8 Relative minions appear under your control.
        # each turn 1 Relative dies.
        # if there are no Relatives left, you win.
        pass

    def alien_diseases(self):
        # when you die, you inflict 25 damage on all opponents.
        # if this damage would kill them, you win the game.
        pass

    def foreign_invasion(self):
        # minions your opponents control attack all targets.
        pass

    def forced_resettlement(self):
        # when you gain a stack of bleeding, all opponents gain twice as many stacks
        pass

    def dishonest_treaties(self):
        # give all your ammo to target opponent
        # if you die from being stuck by one of those bullets
        # you win
        pass
