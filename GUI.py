import tkinter as tk
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

left = []
right = []


def display_mainMenu():
    display_mm = tk.Canvas(root, bg="black")
    display_mm.place(relx=.4, rely=.1, relwidth=.2, relheight=.6)
    chooseCharacters_button = tk.Button(display_mm, text="Choose Characters", command=display_chooseCharacters)
    chooseCharacters_button.pack()


def display_chooseCharacters():
    display_cc = tk.Canvas(root, bg="#50A5FE")
    display_cc.place(relwidth=1, relheight=1)
    left_cc = tk.Canvas(display_cc, bg="black")
    left_cc.place(relwidth=.2, relheight=2)
    right_cc = tk.Canvas(display_cc, bg="black")
    right_cc.place(relx=.8, relwidth=.2, relheight=2)
    display_characters_1 = tk.Canvas(display_cc, bg="#50A5FE")
    display_characters_1.place(relx=.2, rely=0, relwidth=.2)
    display_characters_2 = tk.Canvas(display_cc, bg="#50A5FE")
    display_characters_2.place(relx=.4, rely=0, relwidth=.2)
    display_characters_3 = tk.Canvas(display_cc, bg="#50A5FE")
    display_characters_3.place(relx=.6, rely=0, relwidth=.2)

    left_title = tk.Label(left_cc, text="Left Side:", bg="black", fg="white")
    left_title.pack()
    right_title = tk.Label(right_cc, text="Right Side:", bg="black", fg="white")
    right_title.pack()

    left_text = tk.StringVar()
    left_team = tk.Label(left_cc, textvariable=left_text, bg="black", fg="white", justify="left")
    left_text.set("")
    left_team.pack()
    right_text = tk.StringVar()
    right_team = tk.Label(right_cc, textvariable=right_text, bg="black", fg="white", justify="left")
    right_text.set("")
    right_team.pack()

    def team_display(text, team):
        buffer = ""
        for character in team:
            buffer += character.get_name() + "\n"
            buffer += "Health: " + str(character.health) + "\n"
            if character.armor > 0:
                buffer += "Armor: " + str(character.armor) + "\n"
            if character.shields > 0:
                buffer += "Shields: " + str(character.shields) + "\n"
        text.set(buffer)

    def add_alien():
        if len(left) < 4:
            left.append(Character_Alien.Alien())
            team_display(left_text, left)
        elif len(right) < 4:
            right.append(Character_Alien.Alien())
            team_display(right_text, right)

    def add_banker():
        if len(left) < 4:
            left.append(Character_Banker.Banker())
            team_display(left_text, left)
        elif len(right) < 4:
            right.append(Character_Banker.Banker())
            team_display(right_text, right)

    def add_barber():
        if len(left) < 4:
            left.append(Character_Barber.Barber())
            team_display(left_text, left)
        elif len(right) < 4:
            right.append(Character_Barber.Barber())
            team_display(right_text, right)

    def add_barman():
        if len(left) < 4:
            left.append(Character_Barman.Barman())
            team_display(left_text, left)
        elif len(right) < 4:
            right.append(Character_Barman.Barman())
            team_display(right_text, right)

    alien_button = tk.Button(display_characters_1, text="Alien", command=add_alien)
    alien_button.pack(fill="x")
    banker_button = tk.Button(display_characters_1, text="Banker", command=add_banker)
    banker_button.pack(fill="x")
    barber_button = tk.Button(display_characters_1, text="Barber", command=add_barber)
    barber_button.pack(fill="x")
    bar_button = tk.Button(display_characters_1, text="Barman", command=add_barman)
    bar_button.pack(fill="x")
    cattleman_button = tk.Button(display_characters_1, text="Cattleman")
    cattleman_button.pack(fill="x")
    cowboy_button = tk.Button(display_characters_1, text="Cowboy")
    cowboy_button.pack(fill="x")
    diplomat_button = tk.Button(display_characters_1, text="Diplomat")
    diplomat_button.pack(fill="x")
    doctor_button = tk.Button(display_characters_1, text="Doctor")
    doctor_button.pack(fill="x")
    doughboy_button = tk.Button(display_characters_1, text="Doughboy")
    doughboy_button.pack(fill="x")
    eldritch_button = tk.Button(display_characters_1, text="Eldritch Horror")
    eldritch_button.pack(fill="x")
    fortune_button = tk.Button(display_characters_1, text="Fortune Teller")
    fortune_button.pack(fill="x")
    gambler_button = tk.Button(display_characters_1, text="Gambler")
    gambler_button.pack(fill="x")
    heiress_button = tk.Button(display_characters_2, text="Heiress")
    heiress_button.pack(fill="x")
    hustler_button = tk.Button(display_characters_2, text="Hustler")
    hustler_button.pack(fill="x")
    judge_button = tk.Button(display_characters_2, text="Judge")
    judge_button.pack(fill="x")
    knight_button = tk.Button(display_characters_2, text="Knight")
    knight_button.pack(fill="x")
    land_button = tk.Button(display_characters_2, text="Land Baron")
    land_button.pack(fill="x")
    law_button = tk.Button(display_characters_2, text="Lawman")
    law_button.pack(fill="x")
    mayor_button = tk.Button(display_characters_2, text="Mayor")
    mayor_button.pack(fill="x")
    mission_button = tk.Button(display_characters_2, text="Missionary")
    mission_button.pack(fill="x")
    native_button = tk.Button(display_characters_2, text="Native American")
    native_button.pack(fill="x")
    ninja_button = tk.Button(display_characters_2, text="Ninja")
    ninja_button.pack(fill="x")
    podunk_button = tk.Button(display_characters_2, text="Podunk")
    podunk_button.pack(fill="x")
    prop_button = tk.Button(display_characters_2, text="Proprietor")
    prop_button.pack(fill="x")
    pros_button = tk.Button(display_characters_3, text="Prospector")
    pros_button.pack(fill="x")
    robot_button = tk.Button(display_characters_3, text="Robot")
    robot_button.pack(fill="x")
    science_button = tk.Button(display_characters_3, text="Scientist")
    science_button.pack(fill="x")
    scoundrel_button = tk.Button(display_characters_3, text="Scoundrel")
    scoundrel_button.pack(fill="x")
    shape_button = tk.Button(display_characters_3, text="Shapeshifter")
    shape_button.pack(fill="x")
    snake_button = tk.Button(display_characters_3, text="Snakeoil Salesman")
    snake_button.pack(fill="x")
    train_button = tk.Button(display_characters_3, text="Train Conductor")
    train_button.pack(fill="x")
    vampire_button = tk.Button(display_characters_3, text="Vampire")
    vampire_button.pack(fill="x")
    werewolf_button = tk.Button(display_characters_3, text="Werewolf")
    werewolf_button.pack(fill="x")
    wizard_button = tk.Button(display_characters_3, text="Wizard")
    wizard_button.pack(fill="x")
    zombie_button = tk.Button(display_characters_3, text="Zombie")
    zombie_button.pack(fill="x")


root = tk.Tk()
root.geometry("800x650")

canvas = tk.Canvas(root, bg="black")
canvas.place(relwidth=1, relheight=1)

mainMenu = tk.Button(root, text="Main Menu", command=display_mainMenu)
mainMenu.grid(row=0)

root.mainloop()


