# Caitlyn Low caitlynl Section N
# Kings in the Corner (Card Game)
###################################

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
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3
    
    @staticmethod
    def getDeck(shuffled=True):
        deck = [ ]
        for number in range(1, 14):
            for suit in range(4):
                deck.append(PlayingCard(number, suit))
        if (shuffled):
            random.shuffle(deck)
        return deck
        
    @staticmethod
    def dealHand(gameDeck):
        cards = []
        numCards = 8
        for card in range(numCards):
            cards.append(gameDeck.pop())
        return cards
    
    @staticmethod
    def dealCard(gameDeck):
        if gameDeck != []:
            return gameDeck.pop()
                

    def __init__(self, number, suit):
        # number is 1 for Ace, 2...10,
        #           11 for Jack, 12 for Queen, 13 for King
        # suit is 0 for Clubs, 1 for Diamonds,
        #         2 for Hearts, 3 for Spades
        self.number = number
        self.suit = suit

    def __repr__(self):
        return ("%s of %s" %
                (PlayingCard.numberNames[self.number],
                 PlayingCard.suitNames[self.suit]))

    def getHashables(self):
        return (self.number, self.suit) # return a tuple of hashables

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        return (isinstance(other, PlayingCard) and
                (self.number == other.number) and
                (self.suit == other.suit))


#######################################
# COMPUTER PLAYER
#######################################









########################################
from tkinter import *

def init(data):
    loadPlayingCardImages(data) # always load images in init!
    data.home = True
    data.rules = False
    data.game = False
    data.gameOver = False
    data.gameDeck = PlayingCard.getDeck()
    data.playerHand = PlayingCard.dealHand(data.gameDeck)
    data.compHand = PlayingCard.dealHand(data.gameDeck)
    data.nPile = [PlayingCard.dealCard(data.gameDeck)]
    data.ePile = [PlayingCard.dealCard(data.gameDeck)]
    data.sPile = [PlayingCard.dealCard(data.gameDeck)]
    data.wPile = [PlayingCard.dealCard(data.gameDeck)]

def loadPlayingCardImages(data):
    cards = 53 # cards 1-52, back
    data.cardImages = [ ]
    for card in range(cards):
        rank = (card%13)+1
        suit = "cdhsx"[card//13]
        filename = "playing-card-gifs/%s%d.gif" % (suit, rank)
        data.cardImages.append(PhotoImage(file=filename))

def getPlayingCardImage(data, rank, suitName):
    suitName = suitName[0].lower() # only care about first letter
    suitNames = "cdhsx"
    assert(1 <= rank <= 13)
    assert(suitName in suitNames)
    suit = suitNames.index(suitName)
    return data.cardImages[13*suit + rank - 1]


def onMousePress(self, event):
    pass

def onMouseRelease(self, event):
    pass

def onMouseMove(self, event):
    pass
    
def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if event.keysym == "p":
        data.home = False
        data.game = True

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.home:
        canvas.create_rectangle(0, 0, data.width, data.height, fill="white")
        welX = data.width//2
        welY = data.height//4
        canvas.create_text(welX, welY, fill="black", 
            text="Welcome to \nKings in the Corner", font=" Arial 50 bold")
        gameX = data.width//2
        gameY = data.height//2
        canvas.create_text(gameX, gameY, fill="black", 
            text="To start the game press 'p'", font=" Arial 30 bold")
    if  data.game:
        canvas.create_rectangle(0, 0, data.width, data.height,
            fill="#076324")
        if data.gameDeck != []:
            image = getPlayingCardImage(data, 1, "Xtras")
            canvas.create_image(data.width//2, data.height//2, image=image)
        nCard = data.nPile[-1]
        suit = getCardSuit(nCard)
        rank = getCardRank(nCard)
        img = getPlayingCardImage(data, rank, suit)
        canvas.create_image(data.width//2, data.height//2 - 100,
            image=img)
            
        eCard = data.ePile[-1]
        suit = getCardSuit(eCard)
        rank = getCardRank(eCard)
        img = getPlayingCardImage(data, rank, suit)
        canvas.create_image(data.width//2 + 100, data.height//2,
            image=img)
            
        sCard = data.sPile[-1]
        suit = getCardSuit(sCard)
        rank = getCardRank(sCard)
        img = getPlayingCardImage(data, rank, suit)
        canvas.create_image(data.width//2, data.height//2 + 100,
            image=img)
            
        wCard = data.wPile[-1]
        suit = getCardSuit(wCard)
        rank = getCardRank(wCard)
        img = getPlayingCardImage(data, rank, suit)
        canvas.create_image(data.width//2 - 100, data.height//2,
            image=img)
        
def getCardSuit(card):
    cardS = None
    for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
        if suit in str(card):
            cardS = suit
    return cardS
def getCardRank(card):
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
    return int(cardR)
   

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='green', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 250 # milliseconds
    # Create root before calling init (so we can create images in init)
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(700, 700)