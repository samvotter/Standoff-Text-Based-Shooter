# parent
import Character


class Fortune_Teller(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Fortune Teller"

    def crystal_ball(self):
        # After your opponent chooses their upgrade for this turn,
        # eliminate two upgrade choices for target opponent
        pass

    def meant_to_do_that(self):
        # pick a body part. If your next attack does that, target opponent takes 25 damage.
        pass

    def broken_clock(self):
        # on turns 3 and 6, if your attack lands, you choose where it hits
        pass

    def future_change(self):
        # change the outcome of either your attack or an attack made against you.
        pass

    def worthless_advice(self):
        # pick a body part. If your opponent strikes that body part, it does no damage.
        pass

    def seance(self):
        # all characters in the graveyard come back to life for 1 turn
        pass