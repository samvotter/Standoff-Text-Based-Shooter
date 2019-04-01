# parent
import Character

# child
import Minion_Scientist as m

# libraries
import copy as c

# 6 abilities left
class Scientist(Character.Character):

    def __init__(self):
        super().__init__()
        self.last = "Scientist"
        self.upgrades.append("Cure Disease:\n\t Remove all debuffs placed on you by opponents.")
        self.upgrades.append("Work Smarter:\n\t If you miss, you hit your target's feet. "
                             "If you would hit your target's legs, you hit your target's chest.")
        self.upgrades.append("Technocracy:\n\t Instead of causing damage, all attacks now heal one another. "
                             "They still cause bleeding.")
        self.upgrades.append("Collaborate:\n\t Create 2 Graduate Assistant minions, each provide 10 shields every turn.")
        self.upgrades.append("Dedication:\n\t Select any upgrade, except this one, again.")
        self.upgrades.append("Research:\n\t Gain one of your opponent's upgrades.")

        self.smarter_switch = False
        self.dedication_switch = False

        self.upgrade_dict["Cure Disease:\n\t Remove all debuffs placed on you by opponents."] = 1
        self.upgrade_dict["Work Smarter:\n\t If you miss, you hit your target's feet. "
                             "If you would hit your target's legs, you hit your target's chest."] = 2
        self.upgrade_dict["Technocracy:\n\t Instead of causing damage, all attacks now heal one another. "
                             "They still cause bleeding."] = 3
        self.upgrade_dict["Collaborate:\n\t Create 2 Graduate Assistant minions, each provide 10 shields every turn."] = 4
        self.upgrade_dict["Dedication:\n\t Select any upgrade, except this one, again."] = 5
        self.upgrade_dict["Research:\n\t Gain one of your opponent's upgrades."] = 6

        self.all_upgrades = c.deepcopy(self.upgrades)
        self.all_upgrade_dict = c.deepcopy(self.upgrade_dict)

    def apply_upgrade(self, chosen, gamestate):
        choice = self.upgrade_dict[chosen]
        if choice == 1:
            self.cure_disease(gamestate)
            return gamestate
        elif choice == 2:
            self.work_smarter(gamestate)
            return gamestate
        elif choice == 3:
            self.technocracy(gamestate)
            return gamestate
        elif choice == 4:
            self.collaborate(gamestate)
            return gamestate
        elif choice == 5:
            self.dedication(gamestate)
            return gamestate
        elif choice == 6:
            self.research(gamestate)
            return gamestate
        else:
            print("ERROR APPLYING UPGRADE")

    def cure_disease(self, gamestate):
        # remove all debuffs placed on you by opponents.
        pass

    def work_smarter(self, gamestate):
        # if you miss, you hit your target's feet
        # if you would hit your target's legs, you hit your target's chest
        self.smarter_switch = True
        return gamestate

    def technocracy(self, gamestate):
        # instead of causing damage, all shots now heal one another.
        # shots still cause bleeding
        pass

    def collaborate(self, gamestate):
        # create to Graduate Assistant minions, each provide 10 shields
        # per turn.
        self.minions.append(m.GA(self))
        return gamestate

    def dedication(self, gamestate):
        # select any upgrade, except this one, again.
        self.dedication_switch = True
        chosen = self.choose_upgrade()
        gamestate = self.apply_upgrade(chosen, gamestate)
        return gamestate

    def research(self, gamestate):
        # gain one of your opponent's upgrades
        pass

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
            if self.hits(victim) is True:
                part = self.pick_bodypart()
                if self.smarter_switch and part == "Legs":
                    part = "Chest"
                print("- The shot hit!")
                result.append([self.target, part, self.damage, self.bleed_dmg])
                return result
            else:
                if self.smarter_switch:
                    print("- The shot hit!")
                    part = "Feet"
                    result.append([self.target, part, self.damage, self.bleed_dmg])
                    return result
                result.append([self.target, "Miss", None, None])
                print("- The shot missed!")
                return result
        else:
            print("*CLICK!*", self.get_name(), "has run out of ammo.")
            result = [self.target, None, None, None]
            return result

    def turn_start(self, gamestate):
        for minion in self.minions:
            minion.does_thing(gamestate)
        return gamestate

    def choose_upgrade(self):
        if self.dedication_switch:
            print(self.get_name(), "upgrades:")
            i = 1
            for option in self.all_upgrades:
                print(str(i) + ". ", option)
                i += 1
            choice = 0
            while choice < 1 or choice > len(self.all_upgrades):
                choice = int(input("Pick an upgrade by typing the number"))
            chosen = c.deepcopy(self.all_upgrades[choice - 1])
            return chosen
        print(self.get_name(), "upgrades:")
        i = 1
        for option in self.upgrades:
            print(str(i)+". ", option)
            i += 1
        choice = 0
        while choice < 1 or choice > len(self.upgrades):
            choice = int(input("Pick an upgrade by typing the number"))
        chosen = c.deepcopy(self.upgrades[choice-1])
        self.upgrades.remove(self.upgrades[choice-1])
        return chosen
