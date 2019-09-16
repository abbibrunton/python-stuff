import random
deck_hearts = ["ace of hearts", "2 of hearts", "3 of hearts", "4 of hearts", "5 of hearts", "6 of hearts", "7 of hearts", "8 of hearts", "9 of hearts", "10 of hearts", "jack of hearts", "queen of hearts", "king of hearts"]
deck_diamonds = ["ace of diamonds", "2 of diamonds", "3 of diamonds", "4 of diamonds", "5 of diamonds", "6 of diamonds", "7 of diamonds", "8 of diamonds", "9 of diamonds", "10 of diamonds", "jack of diamonds", "queen of diamonds", "king of diamonds"]
deck_clubs = ["ace of clubs", "2 of clubs", "3 of clubs", "4 of clubs", "5 of clubs", "6 of clubs", "7 of clubs", "8 of clubs", "9 of clubs", "10 of clubs", "jack of clubs", "queen of clubs", "king of clubs"]
deck_spades = ["ace of spades", "2 of spades", "3 of spades", "4 of spades", "5 of spades", "6 of spades", "7 of spades", "8 of spades", "9 of spades", "10 of spades", "jack of spades", "queen of spades", "king of spades"]
values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"}
values_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "jack":10, "queen":10, "king":10}

deck = deck_spades + deck_clubs + deck_diamonds + deck_hearts
def card_value(card):
	if not "ace" in card:
		for item in values:
			if item in card:
				card_value = values_dict[item]
				break
			else:
				continue
	else:
		card_value = 1

		
	return(card_value)

n = len(deck)
players_cards = []
i = 1
hand = 2
hand_value = 0
while i<=hand:
	card_id = random.randint(0,n-1)
	card_selected = deck[card_id]
	print(card_selected)
	deck.remove(card_selected)
	players_cards.append(card_selected)
	i+=1
	n-=1
	hand_value += card_value(card_selected)

print(players_cards)
print(hand_value)
state = True
if (hand_value <= 21): #and (not "ace" in players_cards)
	 

