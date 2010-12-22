from holdem import Poker
import sys

debug = False
poker = Poker(5, debug) 

#counter = 0
#for k in range(0, 100):
#    number_of_ties = 0
#    for n in range(0,100):

print "1. Shuffling"
poker.shuffle()
   
print "2. Cutting"
if not poker.cut(13):
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
        text += card.display() + ", "
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
    text += card.display() + ", "
print text  
print "-----------------------"


#Determines the winner
print "6. Determining Score"
results = poker.determine_score(community_cards, players_hands)
print "7. Determining Score"  
winner = poker.determine_winner(results)

tie = True
try:
    len(winner)
except:
    tie = False
    
if not tie:
    #Prints out the winner
    counter = 0
    print "-------- Winner has Been Determined --------"
    for hand in players_hands:
        if counter == winner:
            text = "Winner ** "
        else:
            text = "Loser  -- " 
        for c in hand:
            text += c.display() + ", "
        
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
            text += c.display() + ", "
        
        text += " --- " + poker.name_of_hand(results[counter][0])
        counter += 1
        print text

#counter = 0
#print "---- Determining Scores----"
#for hand in players_hands:
#    if counter == winner:
#        text = "Winner -- "
#    else:
#        text = "Loser  -- " 
#    for c in hand:
#        text += c.display() + ", "
#    counter += 1
#    print text
#if determine_score(community_cards, players_hands):
#    number_of_ties += 1 
#    
#    counter += number_of_ties
#print "The Average number of ties is " + str(counter/100)