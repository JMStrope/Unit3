
import random


# Global Variables
MONTHS = ['Dummy','January','February','March','April','May','June','July',
'August','September','October','November','December']
MONTHS_WITH_30_DAYS = ['April', 'June', 'September', 'November']
miles_to_go = 2000
food = 500
health = 5
current_day = 1
current_month = 3

# all function definitions

def Quit():
    global playing
    Game_Over_Choice = input("Would you like to quit the game? All progress will be lost")
    if Game_Over_Choice == "Yes" or Game_Over_Choice == "yes":
        playing = False
    else:
        print("Continuing Game.")


def Hunt():
    global food
    food += 100
    days_this_hunt = random.randint(2, 5) 
    print(f"You hunted for {days_this_hunt} miles")
    add_day(days_this_hunt)


def Rest():
    global health
    health_added = 1
    health += health_added
    days_this_travel = random.randint(2,5)
    print(f"You rest for {days_this_travel} days \n"
    "and gained 1 extra health point")


    add_day(days_this_travel)


def Travel():
    global miles_to_go
    global current_day
    miles_traveled = random.randint(30, 60)
    miles_to_go -= miles_traveled
    days_this_travel = random.randint(3, 7) 
    print(f"You Traveled {miles_traveled} miles")

    add_day(days_this_travel) 

def Status():
    print()
    print(f"You have {miles_to_go} miles left to travel")
    print()
    print(f"You have {food} pounds of food left" )
    print()
    print(f"You have {health} health left")
    print()
    print(f"It is {MONTHS[current_month]} {current_day}")
    print()

def add_day(days):
    global current_day, current_month, playing, health
    current_day += days
    if MONTHS[current_month] in MONTHS_WITH_30_DAYS:
        if current_day > 30:
            current_day -= 30 
            current_month += 1
            health -= 2
    else:
        if current_day > 31:
            current_day -= 31
            current_month += 1
            health -= 2
        if current_month == 13:
            print('you are outta time')
            playing = False

    consume_food(days)

def consume_food(days):
    global food

    food -= 5 * days

def Help():
    print("The possible inputs are: Hunting, Traveling, Resting, Player Status, and Quit ")
    Person_Help = input("Which would you like to know more about? > ")
    if Person_Help == "Hunting":
            print()
            print("By inputting 'Hunt' you, the player, will hunt for animals and any other edible items")
            print("Hunt always results in 100lbs of food and takes anywhere from 2-5 days (random) ")
            print()
    elif Person_Help == "Traveling":
            print()
            print("By inputting 'Travel' you, the player, will travel anywhere between 30-60 miles in 3-7 days (Both random)")
            print()
    elif Person_Help == "Resting":
            print()
            print("By 'Resting' you, the player, will gain 1 extra health, this can take anywhere between 2-5 days (random)")
            print()
    elif Person_Help == "Player Status":
            print()
            print("Inputting 'Status' will display your current miles travled, health, food supply, and the date.")
            print()





print("Welcome to the oregon Trail. \n"
    "Your goal is to reach Oregon from Independence, Missouri by December 31st. \n"
    "The current day is March 1st \n"
    "You will lose the game if you're health reaches 0\n"
    "Or if you run out of food completely \n"
    "So be sure to rest and hunt regularly \n"
    "Good luck on your adventure. \n"
    "Input 'Help' if you need help at anytime! \n")
Name = input("What is your name, traveler? > ")

playing = True
while playing:
    Player_Action = input("What would you like to do? (Hunt, Travel, Rest, Status, Help, and Quit) > ")
    if Player_Action == "Travel" or Player_Action == "travel":
        Travel()

    elif Player_Action == "Status" or Player_Action == "status":
        Status()

    elif Player_Action == "Help" or Player_Action == "help":
        Help()
    
    elif Player_Action == "Rest" or Player_Action == "rest":
        Rest()
    
    elif Player_Action == "Hunt" or Player_Action == "hunt":
        Hunt()

    elif Player_Action == "Quit" or Player_Action == "quit":
        Quit()

    if health == 0:
        print("You have ran out of health and died on the Oregon trail.")
        print("Better Luck Next Time")
        playing = False
    
    if food == 0:
        print("You ran out of food, and starved.")
        print("Better Luck Next Time")
        playing = False
    
    if miles_to_go == 0:
        print("You made it to Oregon before Winter.")
        print("Congratulations, you survived the arduos Oregon Trail")
        playing = False





    
    
    

    
