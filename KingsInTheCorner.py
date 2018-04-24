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
def validPlay(data, pile):
    suit = getCardSuit(data.selectedCard)
    rank = getCardRank(data.selectedCard)
    reds = ["Hearts", "Diamonds"]
    blacks = ["Clubs", "Spades"]
    playColor = None
    if suit in reds:
        playColor = "red"
    else: 
        playColor = "black"
    if pile == 2:
        deckSuit = getCardSuit(data.nPile[-1])
        deckRank = getCardRank(data.nPile[-1])
        deckColor = None
        if deckSuit in reds:
            deckColor = "red"
        else: 
            deckColor = "black"
        if deckColor == playColor:
            return False
        else:
            if deckRank - 1 != rank:
                return False
            else:
                return True
    elif pile == 4:
        deckSuit = getCardSuit(data.wPile[-1])
        deckRank = getCardRank(data.wPile[-1])
        deckColor = None
        if deckSuit in reds:
            deckColor = "red"
        else: 
            deckColor = "black"
        if deckColor == playColor:
            return False
        else:
            if deckRank - 1 != rank:
                return False
            else:
                return True
    elif pile == 5:
        deckSuit = getCardSuit(data.ePile[-1])
        deckRank = getCardRank(data.ePile[-1])
        deckColor = None
        if deckSuit in reds:
            deckColor = "red"
        else: 
            deckColor = "black"
        if deckColor == playColor:
            return False
        else:
            if deckRank - 1 != rank:
                return False
            else:
                return True
        
    else: #pile == 7
        deckSuit = getCardSuit(data.sPile[-1])
        deckRank = getCardRank(data.sPile[-1])
        deckColor = None
        if deckSuit in reds:
            deckColor = "red"
        else: 
            deckColor = "black"
        if deckColor == playColor:
            return False
        else:
            if deckRank - 1 != rank:
                return False
            else:
                return True

def placeKing(data, pile):
    if "King" not in data.selectedCard:
        return False
    else:
        if pile == 1:
            if data.nwPile != []:
                return False
            else:
                return True
                data.nwPile.append(data.selectedCard)
                data.playerHand.remove(data.selectedCard)
                data.xyPlayerCards.remove(data.selectedXY)
        elif pile == 3:
            if data.nePile != []:
                return False
            else:
                return True
                data.nePile.append(data.selectedCard)
                data.playerHand.remove(data.selectedCard)
                data.xyPlayerCards.remove(data.selectedXY)
        elif pile == 6:
            if data.swPile != []:
                return False
            else:
                return True
                data.swPile.append(data.selectedCard)
                data.playerHand.remove(data.selectedCard)
                data.xyPlayerCards.remove(data.selectedXY)
        else:
            if data.sePile != []:
                return False
            else:
                return True
                data.sePile.append(data.selectedCard)
                data.playerHand.remove(data.selectedCard)
                data.xyPlayerCards.remove(data.selectedXY)
def validMove():
    pass
def humanTurn(data):
    action = input("What do you want to do? \nTo play a card enter, 'play'. \nTo move a pile on the table enter, 'move'. \nTo knock and end your turn enter, 'knock'.")
    action = action.lower()
    while not action in ["play", "move", "knock"]:
        action = input("What do you want to do? \nTo play a card enter, 'play'. \nTo move a pile on the table enter, 'move'. \nTo knock and end your turn enter, 'knock'.")
        action = action.lower()
    if action == "play":
        print("Select a card to play with your mouse.")
        pile = input("Which pile would you like to play your selected card on?\n1 2 3\n4   5\n6 7 8")
        while pile not in [1,2,3,4,5,6,7,8]:
            print("Invalid pile inputted")
            pile = input("Which pile would you like to play your selected card on?\n1 2 3\n4   5\n6 7 8")
        rank = getCardRank(data.selectedCard)
        if (pile == 1 or pile == 3 or pile == 6 or pile == 8) and rank == 13:
            # runs this code if the card you select is a king and you're 
            # trying to move it to a corner
            if placeKing(data, pile) == False:
                print("The pile you selected is invalid. Either you are trying to put a card that is not a king in the corners or there is already a king there.")
            else:
                if pile == 1: 
                    data.nwPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                if pile == 3:
                    data.nePile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                if pile == 6:
                    data.swPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                if pile == 8:
                    data.sePile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
        else:
            if validPlay(data, pile) == False:
                print("That's not a valid move man.")
            else:
                if pile == 2:
                    data.nPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                if pile == 4:
                    data.wPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                if pile == 5:
                    data.ePile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                
                if pile == 7:
                    data.sPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
    if action == "move":
        deckTop = input("Which deck do you want to move? /n1 2 3/n4   5/n6 7 8")
        deckBot = input("Which pile would you like to move the deck you've selected to? /n1 2 3/n4   5/n6 7 8")
        
            
            
    




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
    # data.nXY = [(data.width//2, data.height//2 - 100)] # (x,y) coords of cards on pile 
    data.ePile = [PlayingCard.dealCard(data.gameDeck)]
    # data.eXY = [(data.width//2 + 100, data.height//2)]
    data.sPile = [PlayingCard.dealCard(data.gameDeck)]
    # data.sXY = [(data.width//2, data.height//2 + 100)]
    data.wPile = [PlayingCard.dealCard(data.gameDeck)]
    # data.wXY = [(data.width//2 - 100, data.height//2)]
    
    data.nePile = []
    # data.neXY = [(data.width//2 -100,data.height//2 + 100)] #position of ne pile
    data.sePile = []
    # data.seXY = [(data.width//2 +100, data.height//2 +100)]
    data.swPile = []
    # data.swXY = [(data.width//2 -100, data.height//2 + 100)]
    data.nwPile = []
    # data.nwXY = [(data.width//2 -100, data.height//2 -100)]

    data.playerRound = 0
    data.compRound = 0
    data.xyTurnCards = [] #list containing tuples of the (x,y) coords of cards of the player whose turn it is
    data.margin = data.width//10
    data.cardHeight = 96
    data.cardWidth = 71
    if data.humTurn:
        if len(data.playerHand) > 10: 
            cards = len(data.playerHand)
            yplace = data.height - 60
            num = 0 
            index = 0
            while cards > 0: 
                data.xyTurnCards.append((data.margin + (i*cardWidth), yplace))
                cards -= 1
                num += 1
                index += 1
                if cards == 10:
                    yplace -= 100
                    num = 0
        else:
            yplace = data.height - 60
            for i in range(len(data.playerHand)):
                data.xyTurnCards.append((data.margin + (i*data.cardWidth), yplace))
    else:
        if len(data.compHand) > 10: 
            cards = len(data.compHand)
            yplace = data.height - 60
            num = 0 
            index = 0
            while cards > 0: 
                data.xyTurnCards.append((data.margin + (i*cardWidth), yplace))
                cards -= 1
                num += 1
                index += 1
                if cards == 10:
                    yplace -= 100
                    num = 0
        else:
            yplace = data.height - 60
            for i in range(len(data.compHand)):
                data.xyTurnCards.append((data.margin + (i*data.cardWidth), yplace))
                
    # data.dragImg = {"x": 0, "y": 0, "card": None}
    data.cardW = data.cardWidth//2 # half card w
    data.cardH = data.cardHeight//2 # half card h
    # data.origIndex = None
    # data.oldX = None
    # data.oldY = None
    # data.card = None
    data.selectedXY = None
    data.selectedCard = None

def getTurnCoords(data): 
#updates a list containing the position of the cards depending on whose turn it is
#function needs to be called every time it changes turns
    newCoords = []
    if data.humTurn:
        if len(data.playerHand) > 10: 
            cards = len(data.playerHand)
            yplace = data.height - 60
            num = 0 
            index = 0
            while cards > 0: 
                data.newCoords.append((data.margin + (i*cardWidth), yplace))
                cards -= 1
                num += 1
                index += 1
                if cards == 10:
                    yplace -= 100
                    num = 0
        data.xyTurnCards = newCoords
        else:
            yplace = data.height - 60
            for i in range(len(data.playerHand)):
                data.newCoords.append((data.margin + (i*data.cardWidth), yplace))
            data.xyTurnCards = newCoords
    else:
        if len(data.compHand) > 10: 
            cards = len(data.compHand)
            yplace = data.height - 60
            num = 0 
            index = 0
            while cards > 0: 
                data.newCoords.append((data.margin + (i*cardWidth), yplace))
                cards -= 1
                num += 1
                index += 1
                if cards == 10:
                    yplace -= 100
                    num = 0
        data.xyTurnCards = newCoords
        else:
            yplace = data.height - 60
            for i in range(len(data.compHand)):
                data.newCoords.append((data.margin + (i*data.cardWidth), yplace))
            data.xyTurnCards = newCoords
    
    
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


    
# def onMouseReleased(event, data):
#     nX, nY = data.nXY[0]
#     sX, sY = data.sXY[0]
#     eX, eY = data.eXY[0]
#     wX, wY = data.wXY[0]
#     # has to be on a pile and a valid move; MAKE VALID MOVE FUNCTION
#     if (nX-data.cardW <= event.x <= nX+data.cardW and
#             nY-data.cardH <= event.y <= nY+data.cardH and validMove()):
#         #add card to the pile 
#         pass
#                 
#     elif (sX-data.cardW <= event.x <= sX+data.cardW and
#             sY-data.cardH <= event.y <= sY+data.cardH and validMove()):
#         #add card to pile
#         pass
#                 
#     elif (wX-data.cardW <= event.x <= wX+data.cardW and
#             wY-data.cardH <= event.y <= wY+data.cardH and validMove()):
#         #add card to pile
#         pass
#     elif (eX-data.cardW <= event.x <= eX+data.cardW and
#             eY-data.cardH <= event.y <= eY+data.cardH and validMove()):
#         #add card to pile 
#         pass
#     elif (neX-data.cardW <= event.x <= neX+data.cardW and
#             neY-data.cardH <= event.y <= neY+data.cardH and validMove()):
#         #add card to pile 
#         pass
#     elif (seX-data.cardW <= event.x <= seX+data.cardW and
#             seY-data.cardH <= event.y <= seY+data.cardH and validMove()):
#         #add card to pile 
#         pass
#     elif (swX-data.cardW <= event.x <= swX+data.cardW and
#             swY-data.cardH <= event.y <= swY+data.cardH and validMove()):
#         #add card to pile 
#         pass
#     elif (nwX-data.cardW <= event.x <= nwX+data.cardW and
#             nwY-data.cardH <= event.y <= nwY+data.cardH and validMove()):
#         #add card to pile 
#         pass
#     
#     else: #add card back into player's hand 
#         data.playerHand.insert(data.origIndex, data.card)
#         data.xyPlayerCards.insert(data.origIndex, (data.oldX, data.oldY))
#         data.dragImg["card"] = None
#         data.dragImg["x"] = 0
#         data.dragImg["y"] = 0
# 
# 
# def onMouseMoved(event, canvas, data):
#     print(data.dragImg)
#     '''Handle dragging of an object'''
#     # compute mouse movement 
#     deltaX = event.x - data.dragImg["x"]
#     deltaY = event.y - data.dragImg["y"]
#     # move the object by deltaX and deltaY
#     canvas.move(data.dragImg["card"], deltaX, deltaY)
#     # record the new position
#     data.dragImg["x"] = event.x
#     data.dragImg["y"] = event.y
    
def mousePressed(event, canvas, data):
    # for i in range(len(data.xyPlayerCards)):
    #     x, y = data.xyPlayerCards[i]
    #     
    #     if (x-data.cardW <= event.x <= x+data.cardW and
    #             y-data.cardH <= event.y <= y+data.cardH):
    #         data.origIndex = i 
    #         data.oldX = x 
    #         data.oldY = y
    #         data.card = data.playerHand.pop(i)
    #         print(card)
    #         data.dragImg["card"] = card
    #         data.dragImg["x"] = event.x
    #         data.dragImg["y"] = event.y
    #         drawCard(event.x, event.y, card)
    for i in range(len(data.xyTurnCards)):
        x,y = data.xyTurnCards[i]     
        card = data.playerHand[i]
        if (x-data.cardW <= event.x <= x+data.cardW and
                y-data.cardH <= event.y <= y+data.cardH):
            data.selectedXY = data.xyTurnCards[i]
            data.selectedCard = card
            print(data.selectedXY)
            print(data.selectedCard)
    x, y = data.nXY[0]
    if (x-data.cardW <= event.x <= x+data.cardW and
                y-data.cardH <= event.y <= y+data.cardH):
        data.deckSelXY = data.nXY[0]
        data.deckSelCard = data.nPile[-1]
    
    x,y = data.eXY[0]
    if (x-data.cardW <= event.x <= x+data.cardW and
                y-data.cardH <= event.y <= y+data.cardH):
        data.deckSelXY = data.eXY[0]
        data.deckSelCard = data.ePile[-1]
    
    x,y = data.sXY[0]
    if (x-data.cardW <= event.x <= x+data.cardW and
                y-data.cardH <= event.y <= y+data.cardH):
        data.deckSelXY = data.sXY[0]
        data.deckSelCard = data.sPile[-1]
    
    x,y = data.wXY[0]
    if (x-data.cardW <= event.x <= x+data.cardW and
                y-data.cardH <= event.y <= y+data.cardH):
        data.deckSelXY = data.wXY[0]
        data.deckSelCard = data.wPile[-1]
            
            
def keyPressed(event, data):
    if event.keysym == "p":
        data.home = False
        data.game = True
        data.rules = False
    if event.keysym == "h":
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
        canvas.create_rectangle(0, 0, data.width, data.height, fill="black")
        canvas.create_text(data.width, data.height, text="Rules screen", fill="black")
        
    if  data.game: # game state
        canvas.create_rectangle(0, 0, data.width, data.height,
            fill="#076324")
        if data.gameDeck != []: #stockpile image
            image = getPlayingCardImage(data, 1, "Xtras")
            canvas.create_image(data.width//2, data.height//2, image=image)
        
        if data.nPile != []: #display card north of stock @ pile 2
            nCard = data.nPile[0]
            suit = getCardSuit(nCard)
            rank = getCardRank(nCard)
            img = getPlayingCardImage(data, rank, suit)
            canvas.create_image(data.width//2, data.height//2 -100,
                image=img)
            for i in range(1, len(data.nPile)):
                suit = getCardSuit(nCard)
                rank = getCardRank(nCard)
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.width//2, data.height//2 - 110,
                    image=img)
        
        if data.ePile != []: #display card east of stock @ 5
            eCard = data.ePile[0]
            suit = getCardSuit(eCard)
            rank = getCardRank(eCard)
            img = getPlayingCardImage(data, rank, suit)
            canvas.create_image(data.width//2 + 100, data.height//2,
                image=img)
            for i in range(1, len(data.ePile)):
                suit = getCardSuit(eCard)
                rank = getCardRank(eCard)
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.width//2 + 110, data.height//2,
                    image=img)
       
        if data.sPile != []: #display card south of stock @ 7
            sCard = data.sPile[0]
            suit = getCardSuit(sCard)
            rank = getCardRank(sCard)
            img = getPlayingCardImage(data, rank, suit)
            canvas.create_image(data.width//2, data.height//2+100,
                image=img)
            for i in range(1, len(data.sPile)):
                suit = getCardSuit(sCard)
                rank = getCardRank(sCard)
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.width//2, data.height//2 + 110,
                    image=img)
        
        if data.wPile != []: #display card west of stock @ 4
            wCard = data.wPile[0]
            suit = getCardSuit(wCard)
            rank = getCardRank(wCard)
            img = getPlayingCardImage(data, rank, suit)
            canvas.create_image(data.width//2 - 100, data.height//2,
                image=img)
            for i in range(1, len(data.ePile)):
                suit = getCardSuit(wCard)
                rank = getCardRank(wCard)
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.width//2 - 110, data.height//2,
                    image=img)
        
        if data.nwPile != []: # display north west of stock pile @ 1
            nwCard = data.nwPile[0]
            suit = getCardSuit(nwCard)
            rank = getCardRank(nwCard)
            img = getPlayingCardImage(data, rank, suit)
            canvas.create_image(data.width//2 - 100, data.height//2 -100,
                image=img)
            for i in range(1, len(data.nwPile)):
                suit = getCardSuit(data.nwcard[i])
                rank = getCardRank(data.nwPile[i])
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.width//2 - 100, data.height//2 -110,
                    image=img)
        if data.nePile != []: # north east of stock @ 3
            neCard = data.nePile[0]
            suit = getCardSuit(neCard)
            rank = getCardRank(neCard)
            img = getPlayingCardImage(data, rank, suit)
            canvas.create_image(data.width//2 + 100, data.height//2 - 100,
                image=img)
            for i in range(1, len(data.nePile)):
                suit = getCardSuit(data.necard[i])
                rank = getCardRank(data.nePile[i])
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.width//2 + 100, data.height//2 - 110,
                    image=img)
        if data.swPile != []: # south west of stock @ 6
            swCard = data.swPile[0]
            suit = getCardSuit(neCard)
            rank = getCardRank(neCard)
            img = getPlayingCardImage(data, rank, suit)
            canvas.create_image(data.width//2 - 100, data.height//2 + 100,
                image=img)
            for i in range(1, len(data.swPile)):
                suit = getCardSuit(data.swcard[i])
                rank = getCardRank(data.swPile[i])
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.width//2 - 100, data.height//2 + 110,
                    image=img)
        if data.sePile != []: # south east of stock @ 8
            seCard = data.sePile[0]
            suit = getCardSuit(neCard)
            rank = getCardRank(neCard)
            img = getPlayingCardImage(data, rank, suit)
            canvas.create_image(data.width//2 + 100, data.height//2 + 100,
                image=img)
            for i in range(1, len(data.sePile)):
                suit = getCardSuit(data.secard[i])
                rank = getCardRank(data.sePile[i])
                img = getPlayingCardImage(data, rank, suit)
                canvas.create_image(data.width//2 + 100, data.height//2 + 110,
                    image=img)
                    
        if data.selectedXY != None:
            x, y = data.selectedXY
            canvas.create_rectangle(x-data.cardW-2, y-data.cardH-2, 
                            data.cardW+x+2, data.cardH+y+2, outline="yellow", width="3")
        if data.humTurn:
            # FOR NOW IT JUST DISPLAY'S THE CARDS OF WHOSE EVER TURN IT IS THERE IS NO 
            # HUMAN AND COMPUTER BUT JUST A PLAYER 1 AND PLAYER 2 BUT THEY ARE NAMED
            # COMPUTER AND HUMAN FOR FUTURE REFERENCE 
            #display human cards/player 1 
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
        else:
            #display comp hand cards/player 2
            if len(data.compHand) > 10: 
            #dispays 10 cards per line so the cards don't run off the board
                cards = len(data.compHand)
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
                for i in range (len(data.compHand)):
                    suit = getCardSuit(data.compHand[i])
                    rank = getCardRank(data.compHand[i])
                    img = getPlayingCardImage(data, rank, suit)
                    canvas.create_image(data.margin + (i*data.cardWidth), yplace, image=img)
        
            #display computer cards backs     
            if len(data.playerHand) > 10:
                cards = len(data.playerHand)
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
                for i in range (len(data.playerHand)):
                    img = getPlayingCardImage(data, 1, "Xtras")
                    canvas.create_image(data.margin + (i*data.cardWidth), yplace,
                        image=img)
        # if data.humTurn == True:
        #     humanTurn()
        # 
        


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
        mousePressed(event, canvas, data)
        redrawAllWrapper(canvas, data)
    
    # def onMouseMovedWrapper(event, canvas, data):
    #     onMouseMoved(event, canvas, data)
    #     redrawAllWrapper(canvas, data)
    #     
    # def onMouseReleasedWrapper(event, canvas, data):
    #     onMouseReleased(event, data)
    #     redrawAllWrapper(canvas, data)

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
                            
    # root.bind("<B1-Motion>", lambda event:
    #                         onMouseMovedWrapper(event, canvas, data))
    # root.bind("<ButtonRelease-1>", lambda event:
    #                         onMouseReleasedWrapper(event, canvas, data))
                            
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(900, 800)