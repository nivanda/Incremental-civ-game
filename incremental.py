from numpy import true_divide
import pygame, os, sys

pygame.init()
clock = pygame.time.Clock()

season = "Summer"
day = 1
maxDay = 30
food = 10
foodIncomeBase = 2
foodIncome = "{}".format(foodIncomeBase)
foodExpense = 2
population = 2
populationCap = 5
populationIncomeBase = 0.5
populationIncome = "{} * int({}/2)".format(populationIncomeBase, population)
land = 20
military = 0
wood = 10
stone = 10
iron = 5
gold = 50
woodIncomeBase = 1
woodIncome = "{}".format(woodIncomeBase)
stoneIncomeBase = 0.5
stoneIncome = "{}".format(stoneIncomeBase)
ironIncomeBase = 0.2
ironIncome = "{}".format(ironIncomeBase)
goldIncomeBase = 0.5
goldIncome = "{}*{}".format(goldIncomeBase, population)

currentMenu = "main menu"

run = True
while run:
    os.system("cls")

    if currentMenu == "main menu":
        print("-------------------------------------------")
        print("Pass day: SPACE    |  ------------  | Day: {}".format(day))
        print("Statistics menu: S |  |^^^^^^^^^^|  | Season: {}".format(season))
        print("Building menu: B   | --^^^^^^^^^^-- | ")

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                if currentMenu == "main menu":
                    run = False
                else:
                    currentMenu = "main menu"