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

# From 112  website 
class PlayingCard(object):
    numberNames = [None, "Ace", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Jack", "Queen", "King"]
    suitNames = ["Clubs", "Diamonds", "Hearts", "Spades"]
    # From 112  website 
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


#######################################
# COMPUTER PLAYER
#######################################





#######################################
# Human Player or do I even need a human player?????
#######################################

#def cardMoving




########################################
# Table display 
########################################
from tkinter import *

def init(data):
    loadPlayingCardImages(data) # always load images in init!
    data.home = True
    data.rules = False
    data.game = False
    data.gameOver = False
    data.first = random.choice(["Comp", "Human"]) #who's turn is first 
    if data.first == "Comp":
        data.compTurn = True 
        data.humTurn = False
    else:
        data.humTurn = True
        data.compTurn = False
    data.gameDeck = PlayingCard.getDeck()
    data.playerHand = PlayingCard.dealHand(data.gameDeck)
    data.compHand = PlayingCard.dealHand(data.gameDeck)
    data.nPile = [PlayingCard.dealCard(data.gameDeck)] #cards to display on north deck
    data.nXY = [(data.width//2, data.height//2 - 100)] # (x,y) coords of cards on pile 
    data.ePile = [PlayingCard.dealCard(data.gameDeck)]
    data.eXY = [(data.width//2 + 100, data.height//2)]
    data.sPile = [PlayingCard.dealCard(data.gameDeck)]
    data.sXY = [(data.width//2, data.height//2 + 100)]
    data.wPile = [PlayingCard.dealCard(data.gameDeck)]
    data.wXY = [(data.width//2 - 100, data.height//2)]
    
    data.nePile = []
    data.neXY = [(data.width//2 -100,data.height//2 + 100)] #position of ne pile
    data.sePile = []
    data.seXY = [(data.width//2 +100, data.height//2 +100)]
    data.swPile = []
    data.swXY = [(data.width//2 -100, data.height//2 + 100)]
    data.nwPile = []
    data.nwXY = [(data.width//2 -100, data.height//2 -100)]

    data.round = 0
    data.xyPlayerCards = [] #list containing tuples of the (x,y) coords of cards
    data.margin = data.width//10
    data.cardHeight = 96
    data.cardWidth = 71
    if len(data.playerHand) > 10: 
        cards = len(data.playerHand)
        yplace = data.height - 60
        num = 0 
        index = 0
        while cards > 0: 
            data.xyPlayerCards.append((data.margin + (i*cardWidth), yplace))
            cards -= 1
            num += 1
            index += 1
            if cards == 10:
                yplace -= 100
                num = 0
    else:
        yplace = data.height - 60
        for i in range(len(data.playerHand)):
            data.xyPlayerCards.append((data.margin + (i*data.cardWidth), yplace))
    data.dragImg = {"x": 0, "y": 0, "card": None}
    data.cardW = data.cardWidth//2 # half card w
    data.cardH = data.cardHeight//2 # half card h
    data.origIndex = None
    data.oldX = None
    data.oldY = None
    data.card = None
    
# From 112  website 
def loadPlayingCardImages(data):
    cards = 53 # cards 1-52, back
    data.cardImages = [ ]
    for card in range(cards):
        rank = (card%13)+1
        suit = "cdhsx"[card//13]
        filename = "playing-card-gifs/%s%d.gif" % (suit, rank)
        data.cardImages.append(PhotoImage(file=filename))
# From 112  website 
def getPlayingCardImage(data, rank, suitName):
    suitName = suitName[0].lower() # only care about first letter
    suitNames = "cdhsx"
    assert(1 <= rank <= 13)
    assert(suitName in suitNames)
    suit = suitNames.index(suitName)
    return data.cardImages[13*suit + rank - 1]

def getCardSuit(card): #take a card and returns the suit name of the card
    cardS = None
    for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
        if suit in str(card):
            cardS = suit
    return cardS

def getCardRank(card): # takes a card and returns it's rank 
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

def drawCard(x, y, card):
    suit = getCardSuit(card)
    rank = getCardRank(card)
    img = getPlayingCardImage(data, rank, suit)
    canvas.create_image(x, y, image=img)

def validMove():
    pass
def onMouseReleased(event, data):
    nX, nY = data.nXY[0]
    sX, sY = data.sXY[0]
    eX, eY = data.eXY[0]
    wX, wY = data.wXY[0]
    # has to be on a pile and a valid move; MAKE VALID MOVE FUNCTION
    if (nX-data.cardW <= event.x <= nX+data.cardW and
            nY-data.cardH <= event.y <= nY+data.cardH and validMove()):
        #add card to the pile 
        pass
                
    elif (sX-data.cardW <= event.x <= sX+data.cardW and
            sY-data.cardH <= event.y <= sY+data.cardH and validMove()):
        #add card to pile
        pass
                
    elif (wX-data.cardW <= event.x <= wX+data.cardW and
            wY-data.cardH <= event.y <= wY+data.cardH and validMove()):
        #add card to pile
        pass
    elif (eX-data.cardW <= event.x <= eX+data.cardW and
            eY-data.cardH <= event.y <= eY+data.cardH and validMove()):
        #add card to pile 
        pass
    else: #add card back into player's hand 
        data.playerHand.insert(data.origIndex, data.card)
        data.xyPlayerCards.insert(data.origIndex, (data.oldX, data.oldY))
        data.dragImg["card"] = None
        data.dragImg["x"] = 0
        data.dragImg["y"] = 0


def onMouseMoved(event, canvas, data):
    print(data.dragImg)
    '''Handle dragging of an object'''
    # compute mouse movement 
    deltaX = event.x - data.dragImg["x"]
    deltaY = event.y - data.dragImg["y"]
    # move the object by deltaX and deltaY
    canvas.move(data.dragImg["card"], deltaX, deltaY)
    # record the new position
    data.dragImg["x"] = event.x
    data.dragImg["y"] = event.y
    
def mousePressed(event, data):
    for i in range(len(data.xyPlayerCards)):
        x, y = data.xyPlayerCards[i]
        
        if (x-data.cardW <= event.x <= x+data.cardW and
                y-data.cardH <= event.y <= y+data.cardH):
            data.origIndex = i 
            data.oldX = x 
            data.oldY = y
            data.card = data.playerHand.pop(i)
            print(card)
            data.dragImg["card"] = card
            data.dragImg["x"] = event.x
            data.dragImg["y"] = event.y
            drawCard(event.x, event.y, card)
            
def keyPressed(event, data):
    if event.keysym == "p":
        data.home = False
        data.game = True
        data.rules = False
    if event.keysym == "r":
        data.home = False
        data.game = False
        data.rules = True

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.home: #home screen 
        canvas.create_rectangle(0, 0, data.width, data.height, fill="white")
        welX = data.width//2
        welY = data.height//4
        canvas.create_text(welX, welY, fill="black", 
            text="Welcome to \nKings in the Corner", font=" Arial 50 bold")
        gameX = data.width//2
        gameY = data.height//2
        canvas.create_text(gameX, gameY, fill="black", 
            text="To start the game press 'p'", font=" Arial 30 bold")
    if data.rules: # rules screen 
    
        
    if  data.game: # game state
        canvas.create_rectangle(0, 0, data.width, data.height,
            fill="#076324")
        if data.gameDeck != []: #stockpile image
            image = getPlayingCardImage(data, 1, "Xtras")
            canvas.create_image(data.width//2, data.height//2, image=image)
        
        nCard = data.nPile[-1] #display card north of stock
        suit = getCardSuit(nCard)
        rank = getCardRank(nCard)
        img = getPlayingCardImage(data, rank, suit)
        canvas.create_image(data.width//2, data.height//2 - 100,
            image=img)
        
            
        eCard = data.ePile[-1] # east of stock
        suit = getCardSuit(eCard)
        rank = getCardRank(eCard)
        img = getPlayingCardImage(data, rank, suit)
        canvas.create_image(data.width//2 + 100, data.height//2,
            image=img)
       
            
        sCard = data.sPile[-1] # south of stock
        suit = getCardSuit(sCard)
        rank = getCardRank(sCard)
        img = getPlayingCardImage(data, rank, suit)
        canvas.create_image(data.width//2, data.height//2 + 100,
            image=img)
        
        
        wCard = data.wPile[-1] # west of stock 
        suit = getCardSuit(wCard)
        rank = getCardRank(wCard)
        img = getPlayingCardImage(data, rank, suit)
        canvas.create_image(data.width//2 - 100, data.height//2,
            image=img)
        
        #display human cards 
        if len(data.playerHand) > 10: 
        #dispays 10 cards per line so the cards don't run off the board
            cards = len(data.playerHand)
            yplace = data.height - 60
            num = 0 
            index = 0
            while cards > 0: #display cards in player's hand
                suit = getCardSuit(data.playerHand[index])
                rank = getCardRank(data.playerHand[index])
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.margin + (num*data.cardWidth), yplace, image=img)
                cards -= 1
                num += 1
                index += 1
                if cards == 10:
                    yplace -= 100
                    num = 0
        else:
            yplace = data.height - 60
            for i in range (len(data.playerHand)):
                suit = getCardSuit(data.playerHand[i])
                rank = getCardRank(data.playerHand[i])
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.margin + (i*data.cardWidth), yplace, image=img)
        
        #display computer cards backs     
        if len(data.compHand) > 10:
            cards = len(data.compHand)
            yplace = 60
            num = 0
            while cards > 0:
                img = getPlayingCardImage(data, 1, "Xtras")
                canvas.create_image(data.margin + (num*data.cardWidth), yplace,
                    image=img)
                cards -= 1
                num += 1
                if cards == 10:
                    yplace += 100
                    num = 0
        else:
            yplace = 60
            for i in range (len(data.compHand)):
                img = getPlayingCardImage(data, 1, "Xtras")
                canvas.create_image(data.margin + (i*data.cardWidth), yplace,
                    image=img)
        # if data.compTurn == True:
        #     canvas.create
        
        


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
    
    def onMouseMovedWrapper(event, canvas, data):
        onMouseMoved(event, canvas, data)
        redrawAllWrapper(canvas, data)
        
    def onMouseReleasedWrapper(event, canvas, data):
        onMouseReleased(event, data)
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
                            
    root.bind("<B1-Motion>", lambda event:
                            onMouseMovedWrapper(event, canvas, data))
    root.bind("<ButtonRelease-1>", lambda event:
                            onMouseReleasedWrapper(event, canvas, data))
                            
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(900, 800)