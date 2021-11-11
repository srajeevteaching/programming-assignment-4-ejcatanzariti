# Emily Catanzariti
# CS151, Dr. Rajeev
# Programming Assignment 4
# Program Inputs:
# Program Outputs:

# import random
import random

# function to develop and shuffle cards
def deck_of_cards():
    deck = []
    for num in range(1, 14, 1):
        numstring = str(num)
        deck.append(numstring + " c")
        deck.append(numstring + " d")
        deck.append(numstring + " h")
        deck.append(numstring + " s")
    random.shuffle(deck)
    return deck


# function for selecting cards
def card_selector(index):
    unnamed_card = []
    unnamed_card.append(deck_of_cards[index])
    return unnamed_card


# function for naming cards
def card_name(unnamed):
    unnamed.split( )
    card_num = unnamed[0]
    letter = unnamed[1]
    named_hand = []
    if card_num == "10":
        num = "10"
    elif card_num == "11":
        num = "jack"
    elif card_num == "12":
        num = "queen"
    elif card_num == "13":
        num = "king"
    elif card_num == "1":
        num = "ace"
    elif card_num == "2":
        num = "2"
    elif card_num == "3":
        num = "3"
    elif card_num == "4":
        num = "4"
    elif card_num == "5":
        num = "5"
    elif card_num == "6":
        num = "6"
    elif card_num == "7":
        num = "7"
    elif card_num == "8":
        num = "8"
    elif card_num == "9":
        num = "9"
    if letter == "c":
        suit = "clubs"
    elif letter == "d":
        suit = "diamonds"
    elif letter == "h":
        suit = "hearts"
    elif letter == "s":
        suit = "spades"
    named_hand.append(num + "of" + suit)
    return named_hand


# calculating points
def point_function(num):
    if num == "king" or num == "queen" or num == "jack":
        points = 10
    elif num == "ace":
        points = 11
    elif num == "10":
        points = 10
    elif num == "9":
        points = 9
    elif num == "8":
        points = 8
    elif num == "7":
        points = 7
    elif num == "6":
        points = 6
    elif num == "5":
        points = 5
    elif num == "4":
        points = 4
    elif num == "3":
        points = 3
    elif num == "2":
        points = 2
    return points


# main function
def main():
    shuffled_deck = deck_of_cards()
    unnamed = card_selector()
    name = card_name(unnamed)
    print(name)
    total_points = 0
    point_per_card = point_function(name)
    total_points += point_per_card
    if total_points > 21:
        print("sorry, you lost")


main()
