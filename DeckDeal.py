################
# Deck Class
# Makes a deck
# Deals hands to player and computer 
# Deals a singluar card to the player or computer based on input 
################
# Parts from 112  website 
import random

class PlayingCard(object):
    numberNames = [None, "Ace", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Jack", "Queen", "King"]
    suitNames = ["Clubs", "Diamonds", "Hearts", "Spades"]
    # From 112  website 
   
    @staticmethod
    def getDeck(shuffled=True): # creates a random deck of 52 cards 
        deck = [ ]
        for number in range(1, 14):
            for suit in range(4):
                deck.append(PlayingCard(number, suit))
        if (shuffled):
            random.shuffle(deck)
        return deck
        
    @staticmethod
    def dealHand(gameDeck): #deals a had of 8 cards from a given deck
        cards = []
        numCards = 8
        for card in range(numCards):
            cards.append(gameDeck.pop())
        return cards
    
    @staticmethod
    def dealCard(gameDeck): 
    #deals a single card that is suppose to be 
    #added to a player's hand at the start of every round after the first round 
        if gameDeck != []:
            return gameDeck.pop()
                
    # From 112  website 
    def __init__(self, number, suit):
        # number is 1 for Ace, 2...10,
        #           11 for Jack, 12 for Queen, 13 for King
        # suit is 0 for Clubs, 1 for Diamonds,
        #         2 for Hearts, 3 for Spades
        self.number = number
        self.suit = suit
    # From 112  website 
    def __repr__(self):
        return ("%s of %s" %
                (PlayingCard.numberNames[self.number],
                 PlayingCard.suitNames[self.suit]))
    # From 112  website 
    def getHashables(self):
        return (self.number, self.suit) # return a tuple of hashables
    # From 112  website 
    def __hash__(self):
        return hash(self.getHashables())
    # From 112  website 
    def __eq__(self, other):
        return (isinstance(other, PlayingCard) and
                (self.number == other.number) and
                (self.suit == other.suit))

def getCardSuit(card): #take a card and returns the suit name of the card
    cardS = None
    for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
        if suit in str(card):
            cardS = suit
    return cardS

def getCardRank(card): # takes a card and returns it's rank as an integer 
    cardR = None
    for rank in ["Ace", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Jack", "Queen", "King"]:
        if rank in str(card):
            cardR = rank
            if cardR == "Jack":
                cardR = 11
            if cardR == "Queen":
                cardR = 12
            if cardR == "King":
                cardR = 13
            if cardR == "Ace":
                cardR = 1
    return int(cardR)