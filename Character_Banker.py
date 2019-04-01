# parent
import Character


# Character should take Health on a rollercoaster of ups n downs
class Banker(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Banker"
        self.upgrades.append("Loan:\n\t Give as much Health as you choose to target. At the beginning of each turn, "
                             "gain one third of the lost health as interest from the target.")
        self.upgrades.append("Print Money:\n\t All characters gain 30 Health. All attacks do +10 damage.")
        self.upgrades.append("Hedge:\n\t After combat, gain shields equal to the damage you receive.")
        self.upgrades.append("Overdraft Protection:\n\t When you die, they return to the battlefield with 20 health.")
        self.upgrades.append("Deposit:\n\t Create an Account minion with twice health" \
                          " of the damage you inflicted last turn.")
        self.upgrades.append("Withdraw:\n\t Destroy target friendly minion. Gain its health.")

        self.gift = 0
        self.loan_switch = False
        self.loan_target = None
        self.hedge_switch = False
        self.overdraft_switch = False
        self.last_damage = 0

        self.upgrade_dict["Loan:\n\t Give as much Health as you choose to target. At the beginning of each turn, "
                             "gain one third of the lost health as interest from the target."] = 1
        self.upgrade_dict["Print Money:\n\t All characters gain 30 Health. All attacks do +10 damage."] = 2
        self.upgrade_dict["Hedge:\n\t After combat, gain shields equal to the damage you receive."] = 3
        self.upgrade_dict["Overdraft Protection:\n\t When you die, they return to the battlefield with 20 health."] = 4
        self.upgrade_dict["Deposit:\n\t Create an Account Minion. Its health is equal to the total amount of" \
                          "damage you inflict. Damage taken is split between you and your Account."] = 5
        self.upgrade_dict["Withdraw:\n\t Destroy target friendly minion. Gain its health."] = 6

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.loan(gamestate)
            return gamestate
        elif choice == 2:
            self.print_money(gamestate)
            return gamestate
        elif choice == 3:
            self.hedge(gamestate)
            return gamestate
        elif choice == 4:
            self.overdraft(gamestate)
            return gamestate
        elif choice == 5:
            self.deposit(gamestate)
            return gamestate
        elif choice == 6:
            self.withdrawl(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def loan(self, gamestate):
        self.loan_switch = True
        self.loan_target = self.target
        self.gift = input("How much life would you like to give?")
        self.gift = float(self.gift)
        while self.gift > self.health:
            self.gift = input("Too much! please choose a number less than: " + str(self.health))
        self.health -= self.gift
        self.target.heal(self.gift)
        return gamestate

    def print_money(self, gamestate):
        for character in gamestate.left_side:
            character.heal(30)
            character.damage += 10
        for character in gamestate.right_side:
            character.heal(30)
            character.damage += 10
        return gamestate

    def hedge(self, gamestate):
        self.hedge_switch = True
        return gamestate

    def overdraft(self, gamestate):
        self.overdraft_switch = True
        return gamestate

    def deposit(self, gamestate):
        
        return gamestate

    def withdrawl(self, gamestate):
        minis = []
        if self.side == "L":
            for character in gamestate.left_side:
                for minion in character.minions:
                    minis.append(minion)
        else:
            for character in gamestate.right_side:
                for minion in character.minions:
                    minis.append(minion)
        num = 1
        for minion in minis:
            print(str(num)+".", minion.get_name())
            num += 1
        choice = minis[int(input("Which minion do you want to destroy?"))-1]
        choice.parent.minions.remove(choice)
        return gamestate

    def turn_start(self, gamestate):
        if self.loan_switch:
            self.heal(self.gift / 3)
            self.loan_target.health -= (self.gift / 3)
        return gamestate

    def take_damage(self, result):
        if result[2] is None:
            print(self.get_name(), "took no damage.")
            return False
        else:
            if result[1] == "Chest":
                damage = result[2]
            elif result[1] == "Arms":
                damage = result[2]*(3 / 5)
                self.accuracy *= (9 / 10)
            elif result[1] == "Hands":
                damage = result[2] * (1 / 5)
                self.accuracy /= 2
            elif result[1] == "Legs":
                damage = result[2] * (3 / 5)
            elif result[1] == "Feet":
                damage = result[2] * (1 / 5)
            elif result[1] == "Head":
                damage = result[2] * 2
            else:
                damage = result[2]
            # if the target is alive . . .
            reduce = damage
            if self.alive is True:
                # and they have shields . . .
                if self.shields > 0:
                    # shields reduce incoming damage by a percentage.
                    damage *= (100-self.shields)/100
                    self.shields -= reduce
                    if self.shields < 0:
                        self.shields = 0
                # and if they have armor
                if self.armor > 0:
                    # armor reduces incoming damage by a flat amount.
                    damage -= self.armor
                # and not all of it was blocked
                if damage > 0:
                    if self.hedge_switch is True:
                        self.shields += damage
                    self.health -= damage
                    self.bleed += result[3]
                    print(result[0].get_name(), "was hit in the", result[1], "for", damage)
                    self.last_damage = damage
                    return True
                else:
                    print(self.get_name(), "All damage was blocked!")
                    return False
            # if the target is dead
            else:
                print(self.get_name(), "was dead.")
                return False

    def get_alive(self):
        if self.health > 0:
            self.alive = True
        else:
            if self.overdraft_switch:
                self.health = 20
                self.overdraft_switch = False
                return True
            else:
                self.alive = False
        return self.alive
