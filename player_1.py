from functions import *

# Create four columns
# D* go from 100 to 2
# U* go from 1 to 99
D1 = 100; D2 = 100; U1 = 1; U2 = 1

# Create the deck: a list that contains numbers from 2 to 99
deck = list(range(2,100))

# Create the initial hand of cards
hand = []
hand = draw(hand, 8, deck)
hand.sort()

# Print initial hand
print_hand(hand, D1, D2, U1, U2, len(deck), 0)

n_cards = 0
game_over = False

# The game goes on until there are cards to be played
while len(deck) + len(hand) > 0:
    # Check if there are no cards in hand, player has to draw
    if len(hand) == 0:
        hand = draw(hand, n_cards, deck)
        hand.sort()
        n_cards = 0
        print_hand(hand, D1, D2, U1, U2, len(deck), n_cards)

    # Check if player can play
    if not can_play(hand, D1, D2, U1, U2):
        if n_cards == 0 or n_cards >= 2:
            hand = draw(hand, n_cards, deck)
            hand.sort()
            n_cards = 0
            print_hand(hand, D1, D2, U1, U2, len(deck), n_cards)
            # After drawing check if it can play
            if not can_play(hand, D1, D2, U1, U2):
                print("GAME OVER!")
                break
        else:
            print("GAME OVER!")
            break

    # Player has cards in hand and can play
    if n_cards < 2:
        # I have to play at least 2 cards, so there is no draw function
        column2play = input ("Choose where to play the card: ")

        # Player cannot draw
        while not check_draw(column2play, n_cards):
            print("You have to play at least two cards!")
            column2play = input ("Choose where to play the card (D1, D2, U1, U2): ")

        # Now choose which card to play
        card2play = int(input("Choose the card you want to play: "))

        # Check if the player is allowed to play that card in that position
        result = check_play(card2play, column2play, hand, D1, D2, U1, U2)
        while not result:
            column2play = input ("Choose where to play the card (D1, D2, U1, U2): ")
            while not check_draw(column2play, n_cards):
                print("You have to play at least two cards!")
                column2play = input ("Choose where to play the card (D1, D2, U1, U2): ")
            card2play = int(input("Choose the card you want to play: "))
            result = check_play(card2play, column2play, hand, D1, D2, U1, U2)

        # Now play the card
        match column2play:
            case "D1":
                D1 = card2play
            case "D2":
                D2 = card2play
            case "U1":
                U1 = card2play
            case _:
                U2 = card2play
        
        hand.remove(card2play)
        n_cards += 1

        print_hand(hand, D1, D2, U1, U2, len(deck), n_cards)

    elif n_cards >= 2:
        # There is still a card that can be played
        column2play = input ("Choose where to play the card or draw: ")

        # Player cannot draw
        while not check_draw(column2play, n_cards):
            column2play = input ("Choose where to play the card (D1, D2, U1, U2): ")

        if column2play == "draw":
            hand = draw(hand, n_cards, deck)
            hand.sort()
            n_cards = 0
            print_hand(hand, D1, D2, U1, U2, len(deck), n_cards)
            continue

        # Now choose which card to play
        card2play = int(input("Choose the card you want to play: "))

        # Check if the player is allowed to play that card in that position
        while not check_play(card2play, column2play, hand, D1, D2, U1, U2):
            column2play = input ("Choose where to play the card (D1, D2, U1, U2) or draw: ")
            while not check_draw(column2play, n_cards):
                print("You have to play at least two cards!")
                column2play = input ("Choose where to play the card (D1, D2, U1, U2): ")

            if column2play == "draw":
                hand = draw(hand, n_cards, deck)
                hand.sort()
                n_cards = 0
                print_hand(hand, D1, D2, U1, U2, len(deck), n_cards)
                continue
            else:
                card2play = int(input("Choose the card you want to play: "))
        
        # Now play the card
        match column2play:
            case "D1":
                D1 = card2play
            case "D2":
                D2 = card2play
            case "U1":
                U1 = card2play
            case _:
                U2 = card2play
        
        hand.remove(card2play)
        n_cards += 1

        print_hand(hand, D1, D2, U1, U2, len(deck), n_cards) 
    
if len(deck) + len(hand) == 0:
    print("WIN!")