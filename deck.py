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
    
    def display(self):
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
        
            
        if self.symbol == 0:
            text += "D"
        elif self.symbol == 1:
            text += "H"
        elif self.symbol == 2:
            text += "S"
        else:
            text += "C" 
            
        return text    
    
class deck:
    
    #Initializes the deck, and adds jokers if specified
    def __init__(self, addJokers = False):
        self.deck = []
        self.inplay = []
        self.addJokers = addJokers
        for symbol in range(0,4):
            for value in range (2,15):
                self.deck.append( Card(symbol, value) )
        if addJokers:
            self.total_cards = 54
            self.deck.append( Card(-1, -1) )
            self.deck.append( Card(-1, -1) )
        else:
            self.total_cards = 52

    #Shuffles the deck
    def shuffle(self):
        self.deck.extend( self.inplay )
        self.inplay = []
        shuffle( self.deck )
    
    #Cuts the deck by the amount specified
    def cut(self, amount):
        if not amount or amount == 0 or amount > len(self.deck):
            return "Invalid amount entered"
        
        temp = [] 
        for i in range(0,amount):
            temp.append( self.deck.pop(0) )
        self.deck.extend(temp)

    #Returns a data dictionary 
    def deal(self, number_of_cards):
        
        if(number_of_cards > len(self.deck) ):
            return "Insufficient cards."
        
        inplay = []
        for i in range(0, number_of_cards):
            inplay.append( self.deck.pop(0) )
        
        self.inplay.extend(inplay)            
        return inplay      
    
    def cards_left(self):
        return len(self.deck)