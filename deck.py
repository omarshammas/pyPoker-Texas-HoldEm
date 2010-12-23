from random import shuffle


class Card:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value
    
    def __cmp__(self, other):
        if self.value < other.value:
            return -1
        elif self.value == other.value:
            return 0
        return 1
    
    def __str__(self):
        text = ""
        if self.value < 0:
            return "Joker";
        elif self.value == 11:
            text = "J"
        elif self.value == 12:
            text = "Q"
        elif self.value == 13:
            text = "K"
        elif self.value == 14:
            text = "A"
        else:
            text = str(self.value)
        
        
        
        
        
        if self.symbol == 0:    #D-Diamonds
            text += "D" 
        elif self.symbol == 1:  #H-Hearts
            text += "H"
        elif self.symbol == 2:  #S-Spade
            text += "S"
        else:   #C-Clubs
            text += "C" 
            
        return text    
    
class deck:
    
    #Initializes the deck, and adds jokers if specified
    def __init__(self, addJokers = False):
        self.cards = []
        self.inplay = []
        self.addJokers = addJokers
        for symbol in range(0,4):
            for value in range (2,15):
                self.cards.append( Card(symbol, value) )
        if addJokers:
            self.total_cards = 54
            self.cards.append( Card(-1, -1) )
            self.cards.append( Card(-1, -1) )
        else:
            self.total_cards = 52

    #Shuffles the deck
    def shuffle(self):
        self.cards.extend( self.inplay )
        self.inplay = []
        shuffle( self.cards )
    
    #Cuts the deck by the amount specified
    #Returns true if the deck was cut successfully and false otherwise
    def cut(self, amount):
        if not amount or amount < 0 or amount >= len(self.cards):
            return False #returns false if cutting by a negative number or more cards than in the deck
        
        temp = [] 
        for i in range(0,amount):
            temp.append( self.cards.pop(0) )
        self.cards.extend(temp)
        return True

    #Returns a data dictionary 
    def deal(self, number_of_cards):
        
        if(number_of_cards > len(self.cards) ):
            return False #Returns false if there are insufficient cards
        
        inplay = []
        for i in range(0, number_of_cards):
            inplay.append( self.cards.pop(0) )
        
        self.inplay.extend(inplay)            
        return inplay      
    
    def cards_left(self):
        return len(self.cards)