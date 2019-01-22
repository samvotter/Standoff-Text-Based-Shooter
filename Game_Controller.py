#modules
from Character import *
from Game_Board import *


class GameController:

    def __init__(self):
        self.mainMenu = ["Single Player", "Squads", "Help", "Exit"]
        self.helpMenu = ["Rules", "Characters", "Back"]
        self.rulesMenu = ["The Game", "Definitions", "Back"]
        self.leftCharacters = []
        self.rightCharacters = []

        with open("Rules.txt") as a:
            pass
        with open("Definitions.txt", 'r') as b:
            pass
        with open("Classes.txt", 'r') as c:
            pass

    def launch(self):
        print("Top Level Display")
        self.menuMain()

    def menuMain(self):
        for i in range(len(self.mainMenu)):
            print(str(i+1) + ". " + self.mainMenu[i])
        select = input("Choose a menu option: ")
        if select == "1":
            self.single()
        elif select == "2":
            self.squads()
        elif select == "3":
            self.menuHelp()
        elif select == "4":
            print("Exiting program . . .")
            self.EXIT()
        else:
            print("ERROR!")
            self.menuMain()

    def menuHelp(self):
        for i in range(len(self.helpMenu)):
            print(str(i+1) + ". " + self.helpMenu[i])
        select = input("Choose a menu option: ")
        if select == "1":
            self.helpRules()
        elif select == "2":
            self.helpClasses()
        elif select == "3":
            return None
        else:
            print("ERROR!")
            self.menuHelp()

    def helpRules(self):
        print("Table of contents: ")
        for i in range(len(self.rulesMenu)):
            print(str(i+1) + ". " + self.rulesMenu[i])
        select = input("Select an item you wish to learn more about: ")
        if select == "1":
            self.helpRulesGame()
        elif select == "2":
            self.helpRulesDefinitions()
        elif select == "3":
            return None
        else:
            print("ERROR")
            self.helpRules()

    def helpClasses(self):
        pass

    def helpRulesGame(self):
        pass

    def helpRulesDefinitions(self):
        pass

    def EXIT(self):
        exit()

    def single(self):
        self.launch()

    def squads(self):
        self.launch()


