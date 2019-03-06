# parent
import Character


class EldritchHorror(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Eldritch Horror"
        self.upgrades.append("Impossible Geometries:\n\t Misses become hits, hits become misses.")
        self.upgrades.append("Cult:\n\t Gain control of all minions. After two turns, all minions die.")
        self.upgrades.append("Unreality:\n\t Enemy attacks which miss, strike the shooter.")
        self.upgrades.append("Monstrous Size:\n\t Double your current health and max health.")
        self.upgrades.append("Tentacles:\n\t Every turn you grow a new Tentacle minion which attacks at random " \
                           "for 10 damage. If a Tentacle minion dies, you take 15 damage.")
        self.upgrades.append("Unstoppable Growth:\n\t Your health and damage increase by +10%" \
                           " at the beginning of each turn.")

        self.upgrade_dict["Impossible Geometries:\n\t Misses become hits, hits become misses."] = 1
        self.upgrade_dict["Cult:\n\t Gain control of all minions. After two turns, all minions die."] = 2
        self.upgrade_dict["Unreality:\n\t Enemy attacks which miss, strike the shooter."] = 3
        self.upgrade_dict["Monstrous Size:\n\t Double your current health and max health."] = 4
        self.upgrade_dict["Tentacles:\n\t Every turn you grow a new Tentacle minion which attacks at random " \
                           "for 10 damage. If a Tentacle minion dies, you take 15 damage."] = 5
        self.upgrade_dict["Unstoppable Growth:\n\t Your health and damage increase by +10%" \
                           " at the beginning of each turn."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.impossible_geometry(gamestate)
            return gamestate
        elif choice == 2:
            self.cult(gamestate)
            return gamestate
        elif choice == 3:
            self.unreality(gamestate)
            return gamestate
        elif choice == 4:
            self.monstrous(gamestate)
            return gamestate
        elif choice == 5:
            self.tentacles(gamestate)
            return gamestate
        elif choice == 6:
            self.unstoppable_growth(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def impossible_geometry(self, gamestate):
        # Misses become hits, hits become misses
        return gamestate

    def cult(self, gamestate):
        # gain control of all minions. After two turns, all minions die
        return gamestate

    def unreality(self, gamestate):
        # Enemy attacks which miss, strike the shooter
        return gamestate

    def monstrous(self, gamestate):
        #double your current health
        self.maxhp *= 2
        self.health *= 2
        return gamestate

    def tentacles(self, gamestate):
        # Every turn you grow a new tentacle which swipes at random
        # opponents each turn for 10 dmg. Attacking tentacles damages you
        return gamestate

    def unstoppable_growth(self, gamestate):
        # your health, and damage increase by 10% each turn
        self.health *= 1.1
        self.damage *= 1.1
        return gamestate