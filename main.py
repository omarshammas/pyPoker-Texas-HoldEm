#Notes
# - Ace was initially associated with the number 1 but then realized
#that in most cases ace is regarded as a high number(eg. when dealing with pairs, flushes, kickers)
#the only situation where it would need to be considered as a 1 is in the straight from 1-5
#therefore to make coding easier it was set to the ace was associated with the number 14 
#which simplifies the code for most situations

from deck import deck, Card

def score(hand):
    
    score = 0
    kicker = []
    
    #------------------------------------------------
    #-------------Checking for Pairs-----------------
    #------------------------------------------------
    pairs = {}
    prev = 0
    
    #Keeps track of all the pairs in a dictionary where the key is the pair's card value
    #and the value is the number occurrences. Eg. If there are 3 Kings -> {"13":3} 
    for card in hand:
        if prev == card.value:
            key = card.value
            if key in pairs:
                pairs[key] += 1
            else:
                pairs[key] = 2
        prev = card.value
    
    #Keeps track of the number of pairs and sets. The value of the previous dictionary
    #is the key. Therefore if there is a pair of 4s and 3 kings -> {"2":1,"3":1}
    nop = {}
    for k, v in pairs.iteritems():
        if v in nop:
            nop[v] += 1
        else:
            nop[v] = 1
    
    #Here we determine the best possible combination the hand can be knowing if the
    #hand has a four of a kind, three of a kind, and multiple pairs.
    
    if 4 in nop:        #Has 4 of a kind, assigns the score and the value of the 
        score = 7
        kicker = pairs.keys()
        return [score, kicker] # Returns immediately because this is the best possible hand
        #doesn't check get the best 5 card hand if all users have a 4 of a kind
        
    elif 3 in nop:      #Has At least 3 of A Kind
        if nop[3] == 2 or 2 in nop:     #Has two 3 of a kind, or a pair and 3 of a kind (fullhouse)
            score = 6
            kicker = pairs.keys() 
            kicker.reverse()
            #PROBLEM
            #How to differentiate between the keys of the 3 of kind and the pairs
            if ( len(kicker) == 3 ):
                kicker.pop()
            
        else:           #Has Only 3 of A Kind
            score = 3
            
            kicker = pairs.keys()       #Gets the value of the 3 of a king
            key = kicker[0]
            
            #Gets a list of all the cards remaining once the three of a kind is removed
            temp = [card.value for card in hand if card.value != key]
            #Get the 2 last cards in the list which are the 2 highest to be used in the 
            #event of a tie
            card_value = temp.pop()
            kicker.append(card_value)
            
            card_value = temp.pop()
            kicker.append(card_value)

    elif 2 in nop:      #Has at Least a Pair
        if nop[2] >= 2:     #Has at least 2  or 3 pairs
            score = 2
            
            kicker = pairs.keys()   #Gets the card value of all the pairs 
            kicker.reverse()        #reverses the key so highest pairs are used
            
            if ( len(kicker) == 3 ):    #if the user has 3 pairs takes only the highest 2
                kicker.pop()
                
            key1 = kicker[0]
            key2 = kicker[1]
            
            #Gets a list of all the cards remaining once the the 2 pairs are removed
            temp = [card.value for card in hand if card.value != key1 and card.value != key2]
            #Gets the last card in the list which is the highest remaining card to be used in 
            #the event of a tie
            card_value = temp.pop()
            kicker.append(card_value)
            
        else:           #Has only a pair
            score = 1 
            
            kicker = pairs.keys()   #Gets the value of the pair
            key = kicker[0] 
 
            #Gets a list of all the cards remaining once pair are removed
            temp = [card.value for card in hand if card.value != key]
            #Gets the last 3 cards in the list which are the highest remaining cards
            #which will be used in the event of a tie
            card_value = temp.pop()
            kicker.append(card_value)
            
            card_value = temp.pop()
            kicker.append(card_value)
            
            card_value = temp.pop()
            kicker.append(card_value)
            
    
    #------------------------------------------------
    #------------Checking for Straight---------------
    #------------------------------------------------    
    #Doesn't check for the ace low straight
    counter = 0
    high = 0
    straight = False
    
    #Checks to see if the hand contains an ace, and if so starts checking for the straight
    #using an ace low
    if (hand[6].value == 14): 
        prev = 1
    else: 
        prev = None
        
    #Loops through the hand checking for the straight by comparing the current card to the
    #the previous one and tabulates the number of cards found in a row
    #***It ignores pairs by skipping over cards that are similar to the previous one
    for card in hand:
        if prev and card.value == (prev + 1):
            counter += 1
            high = card.value
            if counter == 4: #A straight has been recognized
                straight = True
        elif prev and prev == card.value: #ignores pairs when checking for the straight
            pass
        else:
            counter = 0
        prev = card.value
    
    #If a straight has been realized and the hand has a lower score than a straight
    if (straight or counter >= 4) and score < 4:  
        score = 4
        kicker = [high] #Records the highest card value in the straight in the event of a tie


    #------------------------------------------------
    #-------------Checking for Flush-----------------
    #------------------------------------------------
    total = {}
    
    #Loops through the hand calculating the number of cards of each symbol.
    #The symbol value is the key and for every occurrence the counter is incremented
    for card in hand:
        key = card.symbol
        if key in total:
            total[key] += 1
        else:
            total[key] = 1
    
    #key represents the suit of a flush if it is within the hand
    key = -1
    for k, v in total.iteritems():
        if v >= 5:
            key = int(k)
    
    #If a flush has been realized and the hand has a lower score than a flush
    if key != -1 and score < 5:
        score = 5
        kicker = [card.value for card in hand if card.symbol == key]        
        kicker.reverse()
    
    
    #------------------------------------------------
    #-------------------High Card--------------------
    #------------------------------------------------
    if score == 0:      #If the score is 0 then high card is the best possible hand
        
        #It will keep track of only the card's value
        kicker = [int(card.value) for card in hand]
        #Reverses the list for easy comparison in the event of a tie
        kicker.reverse()
        #Since the hand is sorted it will pop the two lowest cards position 0, 1 of the list
        kicker.pop()
        kicker.pop()       
        #The reason we reverse then pop is because lists are inefficient at popping from
        #the beginning of the list, but fast at popping from the end therefore we reverse 
        #the list and then pop the last two elements which will be the two lowest cards
        #in the hand        
    
    #Return the score, and the kicker to be used in the event of a tie
    return [score, kicker]


#------------------------------------------------
#------------------Distribute--------------------
#------------------------------------------------
def distribute(deck, number_of_players, number_of_cards, method):
    
    if(number_of_cards*number_of_players > deck.cards_left() ):
        return "Insufficient cards."
    
    inplay = []
    for i in range(0, number_of_players):
        inplay.append( [] )            
    
    if method == 0:
        #Deals each player one card at a time
        #Has greater complexity, but simulates real life better
        for i in range(0, number_of_cards):
            for j in range(0, number_of_players):
                inplay[j].append( deck.deal(1).pop() )
                
    #Returns a lists of all the hands, which is a list of cards
    return inplay       

#------------------------------------------------
#------------------Get Flop----------------------
#------------------------------------------------    
def getFlop(deck):    
    return deck.deal(3)

#------------------------------------------------
#------------------Get One----------------------
#------------------------------------------------
def getOne(deck):    
    return deck.deal(1)



def determine_score(community_cards, players_hands):
    
    for hand in players_hands:
        hand.extend(community_cards)
        hand.sort()

    #temp = [Card(1, 14), Card(1, 2), Card(1, 3), Card(1, 3), Card(1, 4), Card(1, 5), Card(1, 14)]
    #temp = [Card(2, 14), Card(1, 2), Card(3, 3), Card(1, 3), Card(3, 4), Card(1, 5), Card(1, 14)]
#    temp.sort() 
#    players_hands.append(temp)

    results = []
    print "---- Determining Scores----"
    for hand in players_hands:
        text = "Hand -- " 
        for c in hand:
            text += c.display() + ", "
        overall = score(hand)
        
        results.append([overall[0], overall[1]])    # Stores the results
        
        kicker = ""
        for c in overall.pop(1):
            try:
                kicker += c.display() + ", "
            except:
                kicker += str(c) + ", "
        print text + "Score: " + str(overall.pop(0)) + ", Kicker: " + kicker
    
    print "---- Determining Winner----"
    high = 0
    for r in results:
        if r[0] > high:
            high = r[0]
        
        print r
    
    kicker = {}    
    counter = 0
    #Keeps track of all the kickers in a dictionary where the key is the player's number
    #and the value is the player's kickers
    for r in results:
        if r[0] == high:
            kicker[counter] = r[1]
            
        counter += 1
    
    
    debug = True
    winner = -1
    if(len(kicker) > 1):
        print "---- Tie Braker ----"
        if debug:
            print "---- Kicker ----"
            for k, v in kicker.items():
                print str(k) + " : " + str(v)
        number_of_kickers = len(kicker[kicker.keys().pop()])
        for i in range (0, number_of_kickers):
            high = 0
            for k, v in kicker.items():
                if v[i] > high:
                    high = v[i]
            kicker = {k:v for k, v in kicker.items() if v[i] == high}
            if debug:
                print "---- " + "Round " + str(i) + " ----"
                for k in kicker:
                    print k
            if( len(kicker) <= 1):
                winner = kicker.keys().pop()
            
        # if needs to go here in case the players tie     
    else:
        winner = kicker.keys().pop()
    
    if winner != -1:
        #Prints out the winner
        counter = 0
        print "----- Winner has Been Determined ----"
        for hand in players_hands:
            if counter == winner:
                text = "Winner ** "
            else:
                text = "Loser  -- " 
            for c in hand:
                text += c.display() + ", "
            
            text += " --- " + name_of_hand(results[counter][0])
            counter += 1
            print text
    else:
        winner = kicker.keys()
        counter = 0
        print "----- Tie has Been Determined ----"
        for hand in players_hands:
            if counter in winner:
                text = "Winner ** "
            else:
                text = "Loser  -- " 
            for c in hand:
                text += c.display() + ", "
            
            text += " --- " + name_of_hand(results[counter][0])
            counter += 1
            print text

def name_of_hand(type_of_hand):
    if type_of_hand == 0:
        return "High Card"
    elif type_of_hand == 1:
        return "Pair"
    elif type_of_hand == 2:
        return "2 Pair"
    elif type_of_hand == 3:
        return "3 of a Kind"
    elif type_of_hand == 4:
        return "Straight"
    elif type_of_hand == 5:
        return "Flush"
    elif type_of_hand == 6:
        return "Full House"
    elif type_of_hand == 7:
        return "Four of a Kind"
    elif type_of_hand == 8:
        return "Straight Flush"
    else:
        return "Royal Flush"

    
    

        
        
    
poker = deck()
#for n in poker.deck:
#    print str(n.symbol) + ":" + str(n.value)
 

#counter = 0
#for k in range(0, 100):
#    number_of_ties = 0
#    for n in range(0,100):
poker.shuffle()
#for n in poker.deck:
#    print str(n.symbol) + ":" + str(n.value)
print "-----------------------"
print "1. Shuffled"
print "-----------------------"
    

poker.cut(13)
#for n in poker.deck:
#    print str(n.symbol) + ":" + str(n.value)
print "-----------------------"
print "2. Cut"
print "-----------------------"
    
#print "Just Deal-----------"
#deal = poker.deal(13)
#for n in deal:
#    print str(n.symbol) + ":" + str(n.value)
    
print "-----------------------"
print "3. Distributing"
print "-----------------------"
players_hands = distribute(poker, 5, 2, 0)

print "-----------------------"
print "4. Hands"
print "-----------------------"
for hand in players_hands:
    text = "Player - "
    for card in hand:
        text += card.display() + ", "
    print text


#Gets and prints the community cards
print "-----------------------"
print "5. Community Cards"
print "-----------------------"
getOne(poker) # Burnt Card
community_cards = getFlop(poker) # Gets the flop
getOne(poker) # Burnt Card
community_cards.extend( getOne(poker) ) # Gets the turn
getOne(poker) # Burnt Card
community_cards.extend( getOne(poker) ) # Gets the river

text = "Community Cards - "
for card in community_cards:
    text += card.display() + ", "
print text  


#Determines the winner
print "-----------------------"
print "6. Determining Score"  
print "-----------------------"
winner = determine_score(community_cards, players_hands)

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