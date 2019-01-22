# parent
import Character


class Knight(Character.Character):

    def __init__(self, last, health, armor, shields):
        super().__init__(last, health, armor, shields)
        self.last = "Knight"
        self.upgrades.append("Longsword:\n\t If you run out of ammo: "
                             "after waiting 1 turn, your attacks no longer cost ammo. "
                             "Gain +15 damage and +20% accuracy.")
        self.upgrades.append("Empty The Chamber:\n\t Fire all of your remaining ammunition for 2/7 base damage.")
        self.upgrades.append("Raise Shields:\n\t Trade the maximum of up to 2 bullets for 25 shields each.")
        self.upgrades.append("Suit of Armor:\n\t Trade the maximum of up to 3 bullets: "
                             "1 bullet gives 5 armor. 2 bullets gives 9 armor. 3 bullets gives 12 armor.")
        self.upgrades.append("Chivalry:\n\t Give one of your bullets to every friendly character.")
        self.upgrades.append("Squire:\n\t Resupply yourself with another 6 ammo before combat 3 turns from now.")

        self.longsword_stun = False
        self.longsword_switch = False
        self.empty_switch = False
        self.squire_wait_end = 0

        self.upgrade_dict["Longsword:\n\t If you run out of ammo: "
                             "after waiting 1 turn, your attacks no longer cost ammo. "
                             "Gain +15 damage and +20% accuracy."] = 1
        self.upgrade_dict["Empty The Chamber:\n\t Fire all of your remaining ammunition for 2/7 base damage."] = 2
        self.upgrade_dict["Raise Shields:\n\t Trade the maximum of up to 2 bullets for 25 shields each."] = 3
        self.upgrade_dict["Suit of Armor:\n\t Trade the maximum of up to 3 bullets: "
                             "1 bullet gives 5 armor. 2 bullets gives 9 armor. 3 bullets gives 12 armor."] = 4
        self.upgrade_dict["Chivalry:\n\t Give one of your bullets to every friendly character."] = 5
        self.upgrade_dict["Squire:\n\t Resupply yourself with another 6 ammo before combat 3 turns from now."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.longsword(gamestate)
            return gamestate
        elif choice == 2:
            self.empty_the_chamber(gamestate)
            return gamestate
        elif choice == 3:
            self.raise_shield(gamestate)
            return gamestate
        elif choice == 4:
            self.suit_of_armor(gamestate)
            return gamestate
        elif choice == 5:
            self.chivalry(gamestate)
            return gamestate
        elif choice == 6:
            self.squire(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def longsword(self, gamestate):
        # if you run out of ammo:
        # your attacks no longer cost ammo. Gain +15 damage and +20% accuracy.
        # You must wait at least 1 turn before this takes effect.
        if self.side == "L":
            gamestate.left_side[self.id].longsword_switch = True
            gamestate.left_side[self.id].longsword_stun = True
        elif self.side == "R":
            gamestate.right_side[self.id].longsword_switch = True
            gamestate.right_side[self.id].longsword_stun = True
        return gamestate

    def empty_the_chamber(self, gamestate):
        # Fire all of your remaining ammunition for 2/7 base damage.
        if self.side == "L":
            gamestate.left_side[self.id].empty_switch = True
        elif self.side == "R":
            gamestate.right_side[self.id].empty_switch = True
        return gamestate

    def raise_shield(self, gamestate):
        # Trade the maximum of up to 2 bullets for 25 shields each.
        if self.side == "L":
            times = 2
            while gamestate.left_side[self.id].get_ammo() > 0 and times > 0:
                gamestate.left_side[self.id].change_shields('+', 25)
                gamestate.left_side[self.id].ammo -= 1
                times -= 1
        elif self.side == "R":
            times = 2
            while gamestate.right_side[self.id].get_ammo() > 0 and times > 0:
                gamestate.right_side[self.id].change_shields('+', 25)
                gamestate.right_side[self.id].ammo -= 1
                times -= 1
        return gamestate

    def suit_of_armor(self, gamestate):
        # Trade the maximum of up to 3 bullets:
        #  1 bullet gives 5 armor. 2 bullets gives 9 armor. 3 bullets gives 12 armor.
        if self.side == "L":
            times = 3
            gift = 5
            while gamestate.left_side[self.id].get_ammo() > 0 and times > 0:
                gamestate.left_side[self.id].armor += gift
                gamestate.left_side[self.id].ammo -= 1
                times -= 1
                gift -= 1
        elif self.side == "R":
            times = 3
            gift = 5
            while gamestate.right_side[self.id].get_ammo() > 0 and times > 0:
                gamestate.right_side[self.id].armor += gift
                gamestate.right_side[self.id].ammo -= 1
                times -= 1
                gift -= 1
        return gamestate

    def chivalry(self, gamestate):
        # Give one bullet to all friendly characters
        if self.side == "L":
            for character in gamestate.left_side:
                if gamestate.left_side[self.id].ammo > 0:
                    character.ammo += 1
                    gamestate.left_side[self.id].ammo -= 1
        elif self.side == "R":
            for character in gamestate.right_side:
                if gamestate.right_side[self.id].ammo > 0:
                    character.ammo += 1
                    gamestate.right_side[self.id].ammo -= 1
        return gamestate

    def squire(self, gamestate):
        # Resupply yourself with another 6 ammo before combat 3 turns from now.
        wait = gamestate.turn + 3
        if self.side == "L":
            gamestate.left_side[self.id].squire_wait_end = wait
        elif self.side == "R":
            gamestate.right_side[self.id].squire_wait_end = wait
        return gamestate

    def before_combat(self, gamestate):
        if gamestate.turn == self.squire_wait_end:
            if self.side == "L":
                gamestate.left_side[self.id].ammo += 6
            elif self.side == "R":
                gamestate.right_side[self.id].ammo += 6
            return gamestate
        else:
            return gamestate


    def attack(self, victim):
        result = []
        # if character is stunned
        if self.wait > 0:
            result.append([self.get_id(), None, None, None])
            print("But", self.get_name(), "could not attack this turn.")
            self.wait -= 1
            return result
        #if they have chosen to use a sword
        if self.longsword_switch is True:
            # and just ran out of ammo
            if self.longsword_stun is True and self.ammo == 0:
                result.append([self.get_id(), None, None, None])
                print("But", self.get_name(), "could not attack this turn.")
                self.longsword_stun = False
                self.accuracy += 20
                return result
            # or they still have ammo so they
            elif self.ammo > 0:
                # go through the gun sequence
                if self.empty_switch is True:
                    # fire everything
                    while self.ammo > 0:
                        print('*BANG!*', end='')
                        if self.hits(victim) is True:
                            print("- The shot hit!")
                            result.append(
                                [self.get_id(), self.pick_bodypart(), self.get_damage() * (2 / 7), self.get_target()])
                            self.ammo -= 1
                        else:
                            result.append([self.get_id(), None, None, self.get_target()])
                            print("- The shot missed!")
                            self.ammo -= 1
                    self.empty_switch = False
                    return result
                # fire once
                else:
                    if self.fire(victim) is True:
                        print('*BANG!*', end='')
                        if self.hits(victim) is True:
                            print("- The shot hit!")
                            result.append([self.get_id(), self.pick_bodypart(), self.get_damage(), self.get_target()])
                            return result
                        else:
                            result.append([self.get_id(), None, None, self.get_target()])
                            print("- The shot missed!")
                            return result
                    else:
                        return "ERROR - KNIGHT SHOULD HAVE AMMO"
            else:
                # time to use the sword
                print('*SWING!*', end='')
                if self.hits(victim) is True:
                    print("- The strike landed true!")
                    result.append([self.get_id(), self.pick_bodypart(), self.get_damage()+15, self.get_target()])
                else:
                    result.append([self.get_id(), None, None, self.get_target()])
                    print("- The shot missed!")
                return result
            # gun sequence
        else:
            if self.empty_switch is True:
                # fire everything
                while self.ammo > 0:
                    print('*BANG!*', end='')
                    if self.hits(victim) is True:
                        print("- The shot hit!")
                        result.append(
                            [self.get_id(), self.pick_bodypart(), self.get_damage() * (2 / 7), self.get_target()])
                        self.ammo -= 1
                    else:
                        result.append([self.get_id(), None, None, self.get_target()])
                        print("- The shot missed!")
                        self.ammo -= 1
                return result
            # fire once
            else:
                if self.fire(victim) is True:
                    print('*BANG!*', end='')
                    if self.hits(victim) is True:
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