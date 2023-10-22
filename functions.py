import random
# Function that prints the actual table
#
# INPUT:
#       - hand : list of actual card in hand
#       - D1: card on top of the first pile that goes down
#       - D2: card on top of the second pile that goes down
#       - U1: card on top of the first pile that goes up
#       - U2: card on top of the second pile that goes up
#       - left: number of cards that are still in the deck
#       - played: number of cards already played

def print_hand(hand, D1, D2, U1, U2, left, played):
    print("#"*41, "\n#", " "*37, "#")
    print("#\t D1\t D2\t U1\t U2\t#")
    print("#\t", D1, "\t", D2, "\t", U1, "\t", U2, "\t#")
    print("#", " "*37, "#")
    print("#"*41)
    print("\nYour hand: ", hand, "\tDeck: ", left, "\tPlayed cards: ", played)

###############################################################################

# Function that checks if the player can play a 10 difference in the pile U*
#
# INPUT:
#       - card: card that the player wants to play
#       - U: value of the pile U

def down_ten(card, U):
    # In the pile numbers are growing, card is 10 smaller
    if U - card != 10:
        return False
    else:
        return True
    
###############################################################################

# Function that checks if the player can play a 10 difference in the pile D
#
# INPUT:
#       - card: card that the player wants to play
#       - D: value of the pile U
    
def up_ten(card, D):
    # In the pile numbers are going down, card is 10 bigger
    if card - D != 10:
        return False
    else:
        return True
    
###############################################################################

# Function that checks if the player can play the selected card in a pile
#
# INPUT:
#       - card: card that the player wants to play
#       - position: string that represent the pile
#       - hand : list of actual card in hand
#       - D1: card on top of the first pile that goes down
#       - D2: card on top of the second pile that goes down
#       - U1: card on top of the first pile that goes up
#       - U2: card on top of the second pile that goes up
    
def check_play(card, position, hand, D1, D2, U1, U2):
    positions = ["D1", "D2", "U1", "U2"]

    # Check if card is in hand
    if card not in hand:
        print("Error! The card is not in your hand")
        return False

    # Check if position is in the type (D1, D2, U1, U2)
    if position not in positions:
        print("Error! The position should be in the format: D1, D2, U1, U2")
        return False
    
    # Check if player can play the selected card on the pile
    # To do this check if the player cannot play the card, otherwize at the end it returns True
    match position:
        case "D1":
            if card > D1:
                if up_ten(card, D1):
                    # Even if the card is going up, player can do that because of difference of 10
                    return True
                else:
                    # Player cannot play a card that is going up in a pile that is going down
                    print("You cannot play this card on D1")
                    return False
        case "D2":
            if card > D2:
                if up_ten(card, D2):
                    # Even if the card is going up, player can do that because of difference of 10
                    return True
                else:
                    # Player cannot play a card that is going up in a pile that is going down
                    print("You cannot play this card on D2")
                    return False
        case "U1":
            if card < U1:
                if down_ten(card, U1):
                    # Even if the card is going down, player can do that because of difference of 10
                    return True
                else:
                    # Player cannot play a card that is going down in a pile that is going up
                    print("You cannot play this card on U1")
                    return False
        case _:
            if card < U2:
                if down_ten(card, U2):
                    return True
                else:
                    print("You cannot play this card on U2")
                    return False
    return True
                
# Function that checks if the player can draw cards from the deck
#
# INPUT:
#       - input: string that checks if the action is draw
#       - n_cards: number of cards alredy played

def check_draw(input, n_cards):
    if input == "draw":
        if n_cards >= 2:
            return True
        else:
            return False
    elif input in ["D1", "D2", "U1", "U2"]:
        return True
    else:
        return False
    
def draw(hand, n_cards, deck):
    if n_cards <= len(deck):
        if n_cards == 0:
            for i in range(8):
                card = random.choice(deck)
                hand.append(card)
                deck.remove(card)
        else:
            for i in range(n_cards):
                card = random.choice(deck)
                hand.append(card)
                deck.remove(card)
    elif len(deck) > 0:
        hand += deck
        deck = []

    return hand

def can_play(hand, D1, D2, U1, U2):
    for card in hand:
        if card < D1:
            return True
        else:
            if up_ten(card, D1):
                return True
            else:
                if card < D2:
                    return True
                else:
                    if up_ten(card, D2):
                        return True
                    else:
                        if card > U1:
                            return True
                        else:
                            if down_ten(card, U1):
                                return True
                            else:
                                if card > U2:
                                    return True
                                else:
                                    if down_ten(card, U2):
                                        return True
    return False