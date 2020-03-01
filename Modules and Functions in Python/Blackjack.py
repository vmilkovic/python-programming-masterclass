import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    extension = 'png'

    # for each suit, retrieve the image of the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(suit, str(card), extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(suit, card, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def _deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # and add it to back of the pack
    deck.append(next_card)
    # add the image to the Label and display the label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list
    # Only one ace can have the value 11, and this will be reduced to 1 if the hand would burst.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # If we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealerCardFrame))
        dealer_score = score_hand(dealer_hand)
        dealerScoreLabel.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(_deal_card(playerCardFrame))
    player_score = score_hand(player_hand)
    playerScoreLabel.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealerCardFrame))
    dealerScoreLabel.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealerCardFrame, playerCardFrame, dealer_hand, player_hand
    # Embedded frame to hold the card images
    dealerCardFrame.destroy()
    dealerCardFrame = tkinter.Frame(cardFrame, background="green")
    dealerCardFrame.grid(row=0, column=1, sticky="ew", rowspan=2)
    # Embedded from to hold the card images
    playerCardFrame.destroy()
    playerCardFrame = tkinter.Frame(cardFrame, background="green")
    playerCardFrame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")

    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []

    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()

# Set up the screen and frame for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("960x720")
mainWindow.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images
dealerCardFrame = tkinter.Frame(cardFrame, background="green")
dealerCardFrame.grid(row=0, column=1, sticky="ew", rowspan=2)

playerScoreLabel = tkinter.IntVar()

tkinter.Label(cardFrame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=playerScoreLabel, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images
playerCardFrame = tkinter.Frame(cardFrame, background="green")
playerCardFrame.grid(row=2, column=1, sticky="ew", rowspan=2)

buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky="w")

dealerButton = tkinter.Button(buttonFrame, text="Dealer", command=deal_dealer)
dealerButton.grid(row=0, column=0)

playerButton = tkinter.Button(buttonFrame, text="Player", command=deal_player)
playerButton.grid(row=0, column=1)

newGameButton = tkinter.Button(buttonFrame, text="New Game", command=new_game)
newGameButton.grid(row=0, column=2)

shuffleButton = tkinter.Button(buttonFrame, text="Shufle", command=shuffle)
shuffleButton.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
# For more decks of cards
# deck = list(cards) + list(cards) + list(cards)
shuffle()

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()
