'''
####################
Lab 3.03
####################
Card Game: War
----------------
Create a program that lets a user play a simplified version of the card game 'War'. 
In this version, the users will share a single deck of cards and cards will not be 
added back to the deck after they have been played.

​​Your game should
Start with a given shuffled deck variable (shuffle function comes from python's random library, more details below)

Ask for player1 and player2's names.

Have a function player_turn, with the contract shown below:
# name: player_turn
# purpose: takes in a player name and draws/removes a card from the deck, prints "user drew card x", and returns the value
# Arguments: player_name as string, deck as list
# returns: integer

Have a function compare_scores that takes in the two integers representing the cards drawn and compares the card values. 
Make sure to write the contract for compare_scores!

For simplicity Jacks will be represented as 11, Queens will be represented as 12, Kings will be represented as 13, 
and Aces will be represented as 14

For simplicity the suit does not matter

Include a while loop that keeps the game running until there are no cards in the deck.

If there is a tie, there is "war".  Take the next two cards an whoever wins that gets 
all four cards (including the previous tied cards).  If there is another tie, continue 
taking the next two cards until there a winner.  The winner takes all the "war" cards.

Keep track of the score.

Player who won the most number of cards wins.

Declare the name of the winner and final score at the end of the game.

'''
import random

def shuffled_deck():
    basic_deck = list(range(2, 15)) * 4
    random.shuffle(basic_deck)
    return basic_deck
    

def player_turn(name,deck):
    card = deck.pop(0)
    print(f"{name} drew a: {card}")

    return card

reset = True

while reset:
    deck = shuffled_deck()
    name = input("Enter your name: ")

    player1_deck = deck[0:26]
    player2_deck = deck[26:52]

    computer_score = 0
    player_score = 0
    points_at_stake = 2

    while len(player1_deck) > 0:
        print(f"{name}'s score: {player_score}")
        print(f"Computer's score: {computer_score}")
        input("Please enter to start round. ")
        print()
        card1 = player_turn(name, player1_deck)
        card2 = player_turn("computer", player2_deck)

        if card1 > card2:
            print(f"{name} won this time and wins {points_at_stake} points")
            points_at_stake = 2
            player_score += points_at_stake
        elif card2 > card1:
            print(f"Computer won this time and wins {points_at_stake} points")
            points_at_stake = 2
            computer_score += points_at_stake
            print()
        else:
            print("WAR")
            points_at_stake += 2


    print("Game over. No more Cards")
    print(f"{name}'s score: {player_score}")
    print(f"Computer's score: {computer_score}")
    GameOver = True
    print()

    
    if player_score > computer_score:
        print(f"{name} won!")

    elif computer_score > player_score:
        print("Computer Won!")
        
    else:
        print("It was a tie.")
    
    player_choice = input("Would you like to play again? (y/n) > ")

    if player_choice == 'y':
        print("Here we go again")
    else:
        reset = False
        
