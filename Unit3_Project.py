miles = 0


food = 500

health = 5

import random

while True:
    Player_Action = input("What would you like to do? (Hunt, Travel, Rest, Status, Help, and Quit) > ")
    if Player_Action == "Help":
        print("The possible inputs are: Hunt, Travel, Rest, Status, and Quit ")
        Person_Help = input("Which would you like to know more about? > ")
        if Person_Help == "Hunt":
            print()
            print("By inputting 'Hunt' you, the player, will hunt for animals and any other edible items")
            print("Hunt always results in 100lbs of food and takes anywhere from 2-5 days (random) ")
            print()
        elif Person_Help == "Travel":
            print()
            print("By inputting 'Travel' you, the player, will travel anywhere between 30-60 miles in 3-7 days (Both random)")
            print()
        elif Person_Help == "Rest":
            print()
            print("By 'Resting' you, the player, will gain 1 extra health, this can take anywhere between 2-5 days (random)")
            print()
        elif Person_Help == "Status":
            print()
            print("Inputting 'Status' will display your current miles travled, health, food supply, and the date.")
            print