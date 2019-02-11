# modules
import Character
import Character_Cowboy
import Character_PodunkCowpoke
import Character_Doctor
import Character_Scoundrel
import Character_Lawman
import Character_Barman
import Character_Hustler
import Character_Proprietor
import Character_Prospector
import Character_SnakeoilSalesman
import Character_LandBaron
import Character_TrainConductor
import Character_Judge
import Character_Banker
import Character_Gambler
import Character_NativeAmerican
import Character_Ninja
import Character_Missionary
import Character_Werewolf
import Character_Scientist
import Character_Vampire
import Character_Zombie
import Character_EldritchHorror
import Character_Robot
import Character_Alien
import Character_Diplomat
import Character_Shapeshifter
import Character_Cattleman
import Character_Doughboy
import Character_Mayor
import Character_FortuneTeller
import Character_Heiress
import Character_Knight
import Character_Barber

# libraries
import random
import copy


# The purpose of the CES class is to manage behaviors that happen between two different players
class CombatEncounterSpace:

    def __init__(self, left_side, right_side):
        # Character Sides
        self.left_side = left_side
        self.right_side = right_side
        self.graveyard = []
        self.character_dictionary = {}

        # Game Data
        self.turn = 0

    def choose_characters(self):
        self.left_side.append(Character_Cowboy.Cowboy("Cowboy", 100, 0, 0))
        self.right_side.append(Character_Banker.Banker("Banker", 100, 0, 0))

    def bullet_wounds(self, character, body_part, damage, bleed_dmg):
        if body_part == "Chest":
            if character.take_damage(damage) is True:
                character.change_bleed(bleed_dmg)
        elif body_part == "Arms":
            if character.take_damage((3 / 5)*damage) is True:
                character.change_bleed(bleed_dmg)
            character.change_accuracy("*", (9 / 10))
        elif body_part == "Hands":
            if character.take_damage((1 / 5) * damage) is True:
                character.change_bleed(bleed_dmg)
            character.change_accuracy("*", (1 / 2))
        elif body_part == "Legs":
            if character.take_damage((3 / 5) * damage) is True:
                character.change_bleed(bleed_dmg)
        elif body_part == "Feet":
            if character.take_damage((1 / 5) * damage) is True:
                character.change_bleed(bleed_dmg)
        elif body_part == "Head":
            if character.take_damage(2 * damage) is True:
                character.change_bleed(bleed_dmg)
        else:
            "ERROR - Invalid body_part"

    def part_translator(self, body_part, damage):
        if body_part == "Chest":
            return damage
        elif body_part == "Legs":
            return damage * (3 / 5)
        elif body_part == "Feet":
            return damage * (1 / 5)
        elif body_part == "Hands":
            return damage * (1 / 5)
        elif body_part == "Arms":
            return damage * (3 / 5)
        elif body_part == "Head":
            return damage * 2
        else:
            return "ERROR SELECTING BODYPART"

    def round(self, gamestate):
        # Rounds are resolved by:
            # UI
            # Left Side
            # Right Side
            # Resolution

        # results are [person, causes, person] IE: Jimmy, Arm, Sally means Jimmy shot Sally in the arm
        l_results = []
        r_results = []

        # UI - Assign Team Numbers
        # Left Side
        l = 0
        for character in gamestate.left_side:
            character.set_id(l)
            character.set_side("L")
            l += 1

        #Right Side
        r = 0
        for character in gamestate.right_side:
            character.set_id(r)
            character.set_side("R")
            r += 1

        # UI - Turn Start
        # Left Side
        for character in gamestate.left_side:
            gamestate = character.turn_start(gamestate)

        # Right Side
        for character in gamestate.right_side:
            gamestate = character.turn_start(gamestate)

        # UI - Health
        print("********************************************************")
        print("Turn:", gamestate.turn)
        print("********************************************************")
        print("Left Side: ")
        # Left Side
        for character in gamestate.left_side:
            print(character.get_name() + ": " + str(character.get_health()))
            if float(character.shields) > 0:
                print("Shields:", str(character.shields))
        # UI
        print("********************************************************")
        print("Right Side: ")
        # Right Side
        for character in gamestate.right_side:
            print(character.get_name() + ": " + str(character.get_health()))
            if float(character.shields) > 0:
                print("Shields:", str(character.shields))
        print("********************************************************")

        # UI - Upgrades
        if gamestate.turn == 0 or gamestate.turn == 1 or gamestate.turn == 3 or gamestate.turn == 5:
            # Left Side
            for character in gamestate.left_side:
                print("********************************************************")
                chosen = character.choose_upgrade()
                gamestate = character.apply_upgrade(chosen, gamestate)
            # Right Side
            for character in gamestate.right_side:
                print("********************************************************")
                chosen = character.choose_upgrade()
                character.apply_upgrade(chosen, gamestate)
        print("********************************************************")

        # UI - before combat triggers
        # Left Side
        for character in gamestate.left_side:
            gamestate = character.before_combat(gamestate)
        # Right Side
        for character in gamestate.right_side:
            gamestate = character.before_combat(gamestate)

        # UI - Aim
        # Left Side
        for character in gamestate.left_side:
            character.set_target(random.randint(0, r-1))

        # Right Side
        for character in gamestate.right_side:
            character.set_target(random.randint(0, l-1))

        # UI - Firing
        # Left Side
        for character in gamestate.left_side:
            print(character.get_name(), "pulls the trigger . . .")
            r_results.append(character.attack(gamestate.right_side[character.get_target()]))

        # Right Side
        for character in gamestate.right_side:
            print(character.get_name(), "pulls the trigger . . .")
            l_results.append(character.attack(gamestate.left_side[character.get_target()]))

        # UI - Figure out damage results:
        # Left Side did stuff
        for players in l_results:
            for result in players:
                if result[1]:
                    # Argument in order:
                        # character taking the damage,
                        # body part that was hit,
                        # damage of the shooter,
                        # bleed_dmg of the shooter
                    gamestate.bullet_wounds(gamestate.left_side[result[3]], result[1],
                                       result[2], gamestate.right_side[result[0]].get_bleed_dmg())
                    print(gamestate.left_side[result[3]].get_name() + " was hit in the " + result[1] +
                          " for " + str(gamestate.part_translator(result[1], result[2])) +
                          " by " + gamestate.right_side[result[0]].get_name())
        # Right Side did stuff
        for players in r_results:
            for result in players:
                if result[1]:
                    # Argument in order:
                        # character taking the damage,
                        # body part that was hit,
                        # damage of the shooter,
                        # bleed_dmg of the shooter
                    gamestate.bullet_wounds(gamestate.right_side[result[3]], result[1],
                                       result[2], gamestate.left_side[result[0]].get_bleed_dmg())
                    print(gamestate.right_side[result[3]].get_name() + " was hit in the " + result[1] +
                          " for " + str(gamestate.part_translator(result[1], result[2])) +
                          " by " + gamestate.left_side[result[0]].get_name())

        # UI - make bleed
        # Left Side
        for character in gamestate.left_side:
            if character.get_bleed() > 0:
                character.bleeds()
                print(character.get_name(), "bleeds for:", character.get_bleed(),)
        # Right Side
        for character in gamestate.right_side:
            if character.get_bleed() > 0:
                character.bleeds()
                print(character.get_name(), "bleeds for:", character.get_bleed(), )

        # UI - Find out who is alive
        # Left Side
        for character in gamestate.left_side:
            if character.get_alive() is False:
                print(character.get_name(), "is dead.")
                gamestate.graveyard.append([character, "Left"])
                gamestate.left_side.remove(character)
        # Right Side
        for character in gamestate.right_side:
            if character.get_alive() is False:
                print(character.get_name(), "is dead.")
                gamestate.graveyard.append([character, "Right"])
                gamestate.right_side.remove(character)

        # UI - Check Winners
        print("********************************************************")
        if len(gamestate.left_side) == 0 and len(gamestate.right_side) == 0:
            print("Everyone is dead. There are no winners.")
        elif len(gamestate.left_side) == 0:
            print("Right side prevails!")
        elif len(gamestate.right_side) == 0:
            print("Left side prevails!")

        # UI - END ROUND
        gamestate.turn += 1
        return gamestate


start = CombatEncounterSpace([], [])

start.choose_characters()

new = start.round(start)
while len(new.left_side) > 0 and len(new.right_side) > 0:
    start.round(new)


