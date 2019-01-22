# parent
import Character


class EldritchHorror(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Eldritch Horror"
        self.upgrades[0] = "Impossible Geometries: Misses become hits, hits become misses."
        self.upgrades[1] = "Cult: Gain control of all minions. After two turns, all minions die."
        self.upgrades[2] = "Unreality: Enemy attacks which miss, strike the shooter."
        self.upgrades[3] = "Monstrous Size: Double your current health and max health."
        self.upgrades[4] = "Tentacles: Every turn you grow a new Tentacle minion which attacks at random " \
                           "for 10 damage. If a Tentacle minion dies, you take 15 damage."
        self.upgrades[5] = "Unstoppable Growth: Your health and damage increase by +10%" \
                           " at the beginning of each turn."

    def impossible_geometry(self):
        # Misses become hits, hits become misses
        pass

    def cult(self):
        # gain control of all minions. After two turns, all minions die
        pass

    def unreality(self):
        # Enemy attacks which miss, strike the shooter
        pass

    def monstrous(self):
        #double your current health
        self.health *= 2

    def tentacles(self):
        # Every turn you grow a new tentacle which swipes at random
        # opponents each turn for 10 dmg. Attacking tentacles damages you
        pass

    def unstoppable_growth(self):
        # your health, and damage increase by 10% each turn
        self.health *= 1.1
        self.damage *= 1.1