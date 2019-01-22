# parent
import Character


class Alien(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Alien"
        self.upgrades[0] = "1. Reactive Design: If you take damage on a specific body part, the next time that " \
                           "spot would take damage, ignore that damage."
        self.upgrades[1] = "2. Slow Shield: Gain 100 shields."
        self.upgrades[2] = "3. Transporter: Whenever your opponent misses, you may chose to leave. " \
                           "If you do, the game ends. The winner is whoever has more health."
        self.upgrades[3] = "4. Big Head: All successful attacks are headshots."
        self.upgrades[4] = "5. Set to Stun: your hits cause enemies to lose their next turn. " \
                           "This cannot happen twice in a row."
        self.upgrades[5] = "6. Future Tech: Your successful attacks always do 10 more damage than they otherwise would."

    def reactive_design(self):
        # If you take damage on a specific body part, the next time that
        # spot would take damage, ignore that damage.
        pass

    def dune_shield(self):
        self.shields += 100

    def beam_me_up(self):
        # whenever your opponent misses, you may chose to leave
        # if you do, the game ends. The winner is whoever has more health
        pass

    def big_head(self):
        # all successful attacks are headshots. This affects you too.
        pass

    def set_to_stun(self):
        # your hits cause enemies to lose their next turn. This cannot
        # happen twice in a row.
        pass

    def advanced_technology(self):
        # your attacks always do 10 more damage than they otherwise would.
        pass