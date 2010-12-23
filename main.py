from holdem import Poker
import sys, random

debug = False    #Set to True to see the debug statements
number_of_players = 4


poker = Poker(number_of_players, debug)
if not poker:
    sys.exit("*** ERROR ***: Invalid number of players. It must be between 2 and 22.")

print "1. Shuffling"
poker.shuffle()

   
print "2. Cutting"
if not poker.cut( random.randint(1,51) ):
    #Cannot cut 0, or the number of cards in the deck
    sys.exit("*** ERROR ***: Invalid amount entered to cut the deck.")    

print "3. Distributing"
players_hands = poker.distribute()
if not players_hands:
    sys.exit("*** ERROR ***: Insufficient cards to distribute.")


print "4. Hands"
print "-----------------------"
for hand in players_hands:
    text = "Player - "
    for card in hand:
        text += str(card) + "  "
    print text
print "-----------------------"


#Gets and prints the community cards
print "5. Community Cards"
print "-----------------------"

#Gets the flop
card = poker.getFlop()
if not card:
    sys.exit("*** ERROR ***: Insufficient cards to distribute.")
community_cards = card

#Gets the Turn
card = poker.getOne()
if not card:
    sys.exit("*** ERROR ***: Insufficient cards to distribute.")
community_cards.extend( card )

#Gets the River
card = poker.getOne()
if not card:
    sys.exit("*** ERROR ***: Insufficient cards to distribute.")
community_cards.extend( card ) 


#Displays the Cards
text = "Community Cards - "
for card in community_cards:
    text += str(card) + "  "
print text  
print "-----------------------"


print "6. Determining Score"
try:
    results = poker.determine_score(community_cards, players_hands)
except:
    sys.exit("*** ERROR ***: Problem determining the score.")

print "7. Determining Winner"  
try:
    winner = poker.determine_winner(results)
except:
    sys.exit("*** ERROR ***: Problem determining the winner.")

#Checks to see if the hand has ended in tie and displays the appropriate message         
tie = True
try:
    len(winner)
except:
    tie = False
    
if not tie:
    counter = 0
    print "-------- Winner has Been Determined --------"
    for hand in players_hands:
        if counter == winner:
            text = "Winner ** "
        else:
            text = "Loser  -- " 
        for c in hand:
            text += str(c) + "  "
        
        text += " --- " + poker.name_of_hand(results[counter][0])
        counter += 1
        print text
else: 
    counter = 0
    print "--------- Tie has Been Determined --------"
    for hand in players_hands:
        if counter in winner:
            text = "Winner ** "
        else:
            text = "Loser  -- " 
        for c in hand:
            text += str(c) + "  "
        
        text += " --- " + poker.name_of_hand(results[counter][0])
        counter += 1
        print text