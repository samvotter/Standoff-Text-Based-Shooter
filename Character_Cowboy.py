# parent
import Character

# 3 abilities left
class Cowboy(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Cowboy"
        self.upgrades.append("Deadshot:\n\t Set your accuracy to 100%")
        self.upgrades.append("TBA:\n\t ")
        self.upgrades.append("Posse:\n\t Create 2 Posse minions."
                             "They attack for 5 damage and fire whenever you attack.")
        self.upgrades.append("Silver Bullet:\n\t Your next attack does double damage.")
        self.upgrades.append("Ricochet:\n\t Your next attack may hit any number of opponents")
        self.upgrades.append("Lead Poisoning:\n\t Your attacks inflict 4 stacks of bleeding.")

        self.silver_bullets_switch = False
        self.ricochet_switch = False

        self.upgrade_dict["Deadshot:\n\t Set your accuracy to 100%"] = 1
        self.upgrade_dict["TBA:\n\t "] = 2
        self.upgrade_dict["Posse:\n\t Create 2 Posse minions."
                             "They attack for 5 damage and fire whenever you attack."] = 3
        self.upgrade_dict["Silver Bullet:\n\t Your next attack does double damage."] = 4
        self.upgrade_dict["Ricochet:\n\t Your next attack may hit any number of opponents"] = 5
        self.upgrade_dict["Lead Poisoning:\n\t Your attacks inflict 4 stacks of bleeding."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.deadshot(gamestate)
            return gamestate
        elif choice == 2:
            self.two_guns(gamestate)
            return gamestate
        elif choice == 3:
            self.posse(gamestate)
            return gamestate
        elif choice == 4:
            self.silver_bullet(gamestate)
            return gamestate
        elif choice == 5:
            self.ricochet(gamestate)
            return gamestate
        elif choice == 6:
            self.lead_poisoning(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def deadshot(self, gamestate):
        # You never miss
        if self.side == "L":
            gamestate.left_side[self.id].set_accuracy(100)
        elif self.side == "R":
            gamestate.right_side[self.id].set_accuracy(100)
        return gamestate

    def two_guns(self, gamestate):
        # TBA
        return gamestate

    def posse(self, gamestate):
        # Create 2 Posse minions. They attack for 5 damage and fire whenever you attack.
        pass

    def silver_bullet(self, gamestate):
        # Your next attack does double damage."
        self.silver_bullets_switch = True

    def ricochet(self, gamestate):
        # Your next attack has a chance to hit all opponents."
        pass

    def lead_poisoning(self, gamestate):
        # Your attacks inflict 4 stacks of bleeding."
        if self.side == "L":
            gamestate.left_side[self.id].change_bleed_dmg('*', 4)
        elif self.side == "R":
            gamestate.right_side[self.id].set_accuracy('*', 4)
        return gamestate

    def attack(self, victim):
        result = []
        # if fire returns true
        if self.wait > 0:
            result.append([self.get_id(), None, None, None])
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            return result
        if self.fire(victim) is True:
            print('*BANG!*', end='')
            if self.hits(victim) is True:
                if self.silver_bullets_switch is True:
                    print("- The shot hit!")
                    result.append([self.get_id(), self.pick_bodypart(), self.get_damage()*2, self.get_target()])
                    self.silver_bullets_switch = False
                    return result
                else:
                    print("- The shot hit!")
                    result.append([self.get_id(), self.pick_bodypart(), self.get_damage(), self.get_target()])
                    return result
            else:
                result.append([self.get_id(), None, None, self.get_target()])
                print("- The shot missed!")
                return result
        else:
            result.append([self.get_id(), None, None, self.get_target()])
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            return result
