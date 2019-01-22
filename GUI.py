from tkinter import *

import Game_Board


class PlayerInfo:

    def __init__(self, game, frame, character):
        self.game = game
        self.name_info = Label(frame, text="Player Name: " + str(character.get_name()))
        self.name_info.grid(row=0, column=0, sticky=W)

        self.hp_info = Label(frame, text="Health: " + str(character.get_health()))
        self.hp_info.grid(row=1, column=0, sticky=W)

        self.armor_info = Label(frame, text="Armor: " + str(character.get_armor()))
        self.armor_info.grid(row=2, column=0, sticky=W)

        self.shields_info = Label(frame, text="Shields: " + str(character.get_shields()))
        self.shields_info.grid(row=3, column=0, sticky=W)

        self.avoidance_info = Label(frame, text="Avoidance: " + str(character.get_avoidance()))
        self.avoidance_info.grid(row=4, column=0, sticky=W)


Showdown = Game_Board.CombatEncounterSpace()

Showdown.choose_characters()

root = Tk()
main_display = Frame(root)
main_display.pack(fill=BOTH, side=LEFT)

l_info = Frame(main_display)
l_info.pack(fill=BOTH, side=LEFT)
PlayerInfo(Showdown, l_info, Showdown.left_side[0])

r_info = Frame(main_display)
r_info.pack(fill=BOTH, side=RIGHT)
PlayerInfo(Showdown, r_info, Showdown.right_side[0])


scene = Frame(main_display)
scene.pack(side=BOTTOM)

root.mainloop()