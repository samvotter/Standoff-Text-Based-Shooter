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
import Character_Wizard

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
        self.left_side.append(Character_Cowboy.Cowboy())
        self.right_side.append(Character_PodunkCowpoke.Podunk_Cowpoke())

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
        for character in gamestate.left_side:
            character.set_side("L")
        # Right Side
        for character in gamestate.right_side:
            character.set_side("R")

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
            print(character.get_name() + ": " + str(character.health))
            if float(character.shields) > 0:
                print("Shields:", str(character.shields))
        # Right Side
        print("********************************************************")
        print("Right Side: ")
        # Right Side
        for character in gamestate.right_side:
            print(character.get_name() + ": " + str(character.health))
            if float(character.shields) > 0:
                print("Shields:", str(character.shields))
        print("********************************************************")

        # UI - Aim
        # Left Side
        for character in gamestate.left_side:
            character.set_target(gamestate.right_side)

        # Right Side
        for character in gamestate.right_side:
            character.set_target(gamestate.left_side)

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

        # UI - Firing
        # Left Side
        print("********************************************************")
        for character in gamestate.left_side:
            print(character.get_name(), "pulls the trigger . . .")
            r_results.append(character.attack(gamestate))

        # Right Side
        print("********************************************************")
        for character in gamestate.right_side:
            print(character.get_name(), "pulls the trigger . . .")
            l_results.append(character.attack(gamestate))

        # UI - Figure out damage results:
        # Left Side did stuff
        for item in l_results:
            for result in item:
                if result[1]:
                    # Argument in order:
                        # character taking the damage,
                        # body part that was hit,
                        # damage of the shooter,
                        # bleed_dmg of the shooter
                    result[0].take_damage(result)
        # Right Side did stuff
        for item in r_results:
            for result in item:
                if result[1]:
                    # Argument in order:
                        # character taking the damage,
                        # body part that was hit,
                        # damage of the shooter,
                        # bleed_dmg of the shooter
                    result[0].take_damage(result)

        # UI - after combat trigger
        # Left Side
        for character in gamestate.left_side:
            gamestate = character.after_combat(gamestate)

        # Right Side
        for character in gamestate.right_side:
            gamestate = character.after_combat(gamestate)

        # UI - make bleed / burn
        # Left Side
        for character in gamestate.left_side:
            if character.bleed > 0:
                character.bleeds()
                character.burns(gamestate)
                for minion in character.minions:
                    if minion.bleed > 0:
                        minion.bleeds()
                        minion.burns(gamestate)
        # Right Side
        for character in gamestate.right_side:
            if character.bleed > 0:
                character.bleeds()
                character.burns(gamestate)
                for minion in character.minions:
                    if minion.bleed > 0:
                        minion.bleeds()
                        minion.burns(gamestate)

        # UI - Find out who is alive
        # Left Side
        for character in gamestate.left_side:
            for minion in character.minions:
                minion.get_alive()
            if character.get_alive() is False:
                print(character.get_name(), "is dead.")
                gamestate.graveyard.append([character, "Left"])
                gamestate.left_side.remove(character)
        # Right Side
        for character in gamestate.right_side:
            for minion in character.minions:
                minion.get_alive()
            if character.get_alive() is False:
                print(character.get_name(), "is dead.")
                gamestate.graveyard.append([character, "Right"])
                gamestate.right_side.remove(character)

        # UI - End Turn trigger
        # Left Side
        for character in gamestate.left_side:
            gamestate = character.end_turn(gamestate)

        # Right Side
        for character in gamestate.right_side:
            gamestate = character.end_turn(gamestate)

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


