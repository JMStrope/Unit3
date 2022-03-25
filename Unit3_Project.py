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


def Travel():
    global miles_to_go
    global current_day
    miles_traveled = random.randint(30, 60)
    miles_to_go -= miles_traveled
    days_this_travel = random.randint(3, 7) 
    print(f"You Traveled {miles_traveled} miles")

    add_day(days_this_travel)

def Status():
    global food
    print()
    print(f"You have {miles_to_go} miles left to travel")
    print()
    print(f"You have {food} pounds of food left" )
    print()
    print(f"It is {MONTHS[current_month]} {current_day}")
    print()
def add_day(days):
    global current_day, current_month
    current_day += days
    if MONTHS[current_month] in MONTHS_WITH_30_DAYS:
        if current_day > 30:
            current_day -= 30 
            current_month += 1
    else:
        if current_day > 31:
            current_day -= 31
            current_month += 1

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
    "Good luck on your adventure. \n"
    "Input Help if you need help at anytime! \n")

while True:
    Player_Action = input("What would you like to do? (Hunt, Travel, Rest, Status, Help, and Quit) > ")
    if Player_Action == "Travel":
        Travel()

    elif Player_Action == "Status":
        Status()

    elif Player_Action == "Help":
        Help()


    
    
    

    
