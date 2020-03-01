# from Blackjack import *
import Blackjack as blackjack

g = sorted(globals())
for x in g:
    print(x)

# functions with underscore (_) are private functions and are not imported
# _deal_card(dealer_card_frame)

print(__name__)
blackjack._deal_card(blackjack.dealerCardFrame) # deals one more card for dealer
print(blackjack.cards)
blackjack.play()

