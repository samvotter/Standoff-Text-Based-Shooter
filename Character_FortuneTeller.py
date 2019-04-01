# modules
import random

# parent
import Character


class Fortune_Teller(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Fortune Teller"
        self.upgrades.append("Crystal Ball:\n\t Eliminate two random upgrade choices for target opponent.")
        self.upgrades.append("Prediction:\n\t Pick a body part. "
                             "If your next attack does that, target opponent takes 25 damage.")
        self.upgrades.append("Broken Clock:\n\t ")
        self.upgrades.append("Future Change:\n\t ")
        self.upgrades.append("Worthless Advice:\n\t ")
        self.upgrades.append("Seance:\n\t ")

        self.prediction_part = ""
        self.prediction_switch = True

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
            self.crystal_ball(gamestate)
            return gamestate
        elif choice == 2:
            self.prediction(gamestate)
            return gamestate
        elif choice == 3:
            self.broken_clock(gamestate)
            return gamestate
        elif choice == 4:
            self.future_change(gamestate)
            return gamestate
        elif choice == 5:
            self.worthless_advice(gamestate)
            return gamestate
        elif choice == 6:
            self.seance(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def crystal_ball(self, gamestate):
        # eliminate two random upgrade choices for target opponent
        self.target.upgrades.remove(self.target.upgrades[random.randint(0, len(self.target.upgrades))])
        self.target.upgrades.remove(self.target.upgrades[random.randint(0, len(self.target.upgrades))])
        return gamestate

    def prediction(self, gamestate):
        # pick a body part. If your next attack does that, target opponent takes 25 damage.
        print("1. Head\n2. Chest\n3. Arms\n4. Hands\n5. Legs\n 6. Feet")
        choice = int(input("Choose a body part: "))
        if choice == 1:
            self.prediction_part = "Head"
        elif choice == 2:
            self.prediction_part = "Chest"
        elif choice == 3:
            self.prediction_part = "Arms"
        elif choice == 4:
            self.prediction_part = "Hands"
        elif choice == 5:
            self.prediction_part = "Legs"
        elif choice == 6:
            self.prediction_part = "Feet"
        self.prediction_switch = True
        return gamestate

    def broken_clock(self, gamestate):
        # on turns 3 and 6, if your attack lands, you choose where it hits
        pass

    def future_change(self, gamestate):
        # change the outcome of either your attack or an attack made against you.
        pass

    def worthless_advice(self, gamestate):
        # pick a body part. If your opponent strikes that body part, it does no damage.
        pass

    def seance(self, gamestate):
        # return all characters from the graveyard back to your side with 1 health
        if self.side == "L":
            for character in gamestate.graveyard:
                if character.side == "L":
                    character.health = 1
                    character.bleed = 0
                    gamestate.left_side.append(character)
        else:
            for character in gamestate.graveyard:
                if character.side == "R":
                    character.health = 1
                    character.bleed = 0
                    gamestate.right_side.append(character)
        return gamestate

    def attack(self, victim):
        result = []
        if self.wait > 0:
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            result = [self.target, None, None, None]
            return result
        # if fire returns true
        if self.fire() is True:
            print('*BANG!*', end='')
            part = self.pick_bodypart()
            if self.hits(victim) is True:
                print("- The shot hit!")
                result.append([self.target, part, self.damage, self.bleed_dmg])
                if part == self.prediction_part:
                    print("The prediction came true!", self.target.get_name(), "took 25 damage.")
                    self.target.health -= 25
                    self.prediction_part = ""
                return result
            else:
                result.append([self.target, "Miss", None, None])
                print("- The shot missed!")
                return result
        else:
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            result = [self.target, None, None, None]
            return result

