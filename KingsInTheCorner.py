# Caitlyn Low caitlynl Section N
# Kings in the Corner (Card Game)
from DeckDeal import *
from actions import *
from drawPiles import *
###############################

#######################################
# COMPUTER PLAYER
#######################################

#######################################
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
                
def humanTurn(action, data):        
    if action == "play": #play a card from hand onto table piles
        # asks which card you want to place down
        card = int(input("Type in the number for the card you want to put in. From top left to bottom right. Starting from 1.\n"))
        # asks where you want to put that card
        pile = int(input("Which pile would you like to play your selected card on?\n1 2 3\n4   5\n6 7 8\n"))
        
        numCards = 0
        if data.humTurn:
            numCards = len(data.playerHand)
        if data.compTurn:
            numCards = len(data.playerHand)
            
        while card-1 < 0 and card-1 > numCards: #makes sure card input is valid
            print("Invalid card choice")
            card = int(input("Type in the number for the card you want to put in. From top left to bottom right. Starting from 1.\n")) 
        xy = None
        if data.humTurn: # selects a card and it's x,y coords
            xy = data.xyTurnCards[card-1]
            card = data.playerHand[card-1]
        else:
            xy = data.xyTurnCards[card-1]
            card = data.compHand[card-1]
        print(card)
        while pile not in [1,2,3,4,5,6,7,8]:
            print("Invalid pile inputted")
            pile = int(input("Which pile would you like to play your selected card on?\n1 2 3\n4   5\n6 7 8\n"))
        rank = getCardRank(card)
        if (pile == 1 or pile == 3 or pile == 6 or pile == 8) and rank == 13:
            # runs this code if the card you select is a king and you're 
            # trying to move it to a corner
            if placeKing(data, pile, card, xy) == False:
                print("The pile you selected is invalid. Either you are trying to put a card that is not a king in the corners or there is already a king there.")
            else:
                print("begin valid play of move king")
                print(data.xyTurnCards)
                print()
                if pile == 1: 
                    data.nwPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 3:
                    data.nePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 6:
                    data.swPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 8:
                    data.sePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
        else: #just regular move, not a king move
            if validPlay(pile, card, data) == False:
                print("That's not a valid move.")
            else:
                print("begin valid play not a king")
                print(data.xyTurnCards)
                print()
                if pile == 2:
                    data.nPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 4:
                    data.wPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 5:
                    data.ePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 7:
                    data.sPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 1:
                    data.nwPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 3:
                    data.nePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 6:
                    data.swPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                if pile == 8:
                    data.sePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                    print(data.xyTurnCards)
                
                    
    if action == "move": #move one deck on top of another deck
        deckTop = int(input("Which deck do you want to move? \n1 2 3\n4   5\n6 7 8\n"))
        deckBot = int(input("Which pile would you like to move the deck you've selected to? \n1 2 3\n4   5\n6 7 8\n"))
        if validMove(data, deckTop, deckBot): #NEEEEEDS TO CHECK WHEN HAVE KING ON BOARD
            if deckTop == 2: #the deck you're putting on top/ From 2-North  
                if deckBot == 4: #the deck under the one you're moving/ to 4-west
                    data.wPile += data.nPile
                    print(data.wPile)
                    data.nPile = []
                if deckBot == 5: # to 5-east
                    data.ePile += data.nPile
                    print(data.ePile)
                    data.nPile = []
                if deckBot == 7: # to 7-south
                    data.sPile += data.nPile
                    print(data.sPile)
                    data.nPile = []
                
                if deckBot == 1: # to 1 - north west
                    botCard = data.nPile[0]
                    rank = getCardRank(botCard)
                    data.nwPile += data.nPile
                    data.nPile = []
                if deckBot == 3:# to 3 - north east
                    botCard = data.nPile[0]
                    rank = getCardRank(botCard)
                    data.nePile += data.nPile
                    data.nPile = []
                if deckBot == 6: # to 6 - south west
                    botCard = data.nPile[0]
                    rank = getCardRank(botCard)
                    data.swPile += data.nPile
                    data.nPile = []   
                if deckBot == 8: # to 8 - south east
                    botCard = data.nPile[0]
                    rank = getCardRank(botCard)
                    data.sePile += data.nPile
                    data.nPile = []
            
            if deckTop == 4: # From 4 - west 
                if deckBot == 2: # to 2 - north
                    data.nPile += data.wPile
                    print(data.nPile)
                    data.wPile = []
                if deckBot == 5: # to 5 - east
                    data.ePile += data.wPile
                    print(data.ePile)
                    data.wPile = []
                if deckBot == 7: # to 7 - south
                    data.sPile += data.wPile
                    print(data.sPile)
                    data.wPile = []

                if deckBot == 1: # to 1 - north west
                    botCard = data.wPile[0]
                    rank = getCardRank(botCard)
                    data.nwPile += data.wPile
                    data.wPile = []
                if deckBot == 3: # to 3 - north east
                    botCard = data.wPile[0]
                    rank = getCardRank(botCard)
                    data.nePile += data.wPile
                    data.wPile = []
                if deckBot == 6: # to 6 - south west
                    botCard = data.wPile[0]
                    rank = getCardRank(botCard)
                    data.swPile += data.wPile
                    data.wPile = []   
                if deckBot == 8: # to 8 - south east
                    botCard = data.wPile[0]
                    rank = getCardRank(botCard)
                    data.sePile += data.wPile
                    data.wPile = []
                    
            if deckTop == 5: # from 5 - east
                if deckBot == 2: # to 2 - north
                    data.nPile += data.ePile
                    print(data.nPile)
                    data.ePile = [] 
                if deckBot == 4: # to 4 - west
                    data.wPile += data.ePile
                    print(data.wPile)
                    data.ePile = [] 
                if deckBot == 7: # to 7 - south
                    data.sPile += data.ePile
                    print(data.sPile)
                    data.ePile = [] 
                
                if deckBot == 1: # to 1 - north west
                    botCard = data.ePile[0]
                    rank = getCardRank(botCard)
                    data.nwPile += data.ePile
                    data.ePile = []
                if deckBot == 3: # to 3 - north east
                    botCard = data.ePile[0]
                    rank = getCardRank(botCard)
                    data.nePile += data.ePile
                    data.ePile = []
                if deckBot == 6: # to 6 - south west
                    botCard = data.ePile[0]
                    rank = getCardRank(botCard)
                    data.swPile += data.ePile
                    data.ePile = []   
                if deckBot == 8: # to 8 - south east
                    botCard = data.ePile[0]
                    rank = getCardRank(botCard)
                    data.sePile += data.ePile
                    data.ePile = []
            
            if deckTop == 7: # from 7 - south
                if deckBot == 2: # to 2 - north
                    data.nPile += data.sPile
                    print(data.nPile)
                    data.sPile = []
                if deckBot == 4: # to 4 - west
                    data.wPile += data.sPile
                    print(data.wPile)
                    data.sPile = []
                if deckBot == 5: # to 5 - east
                    data.ePile += data.sPile
                    print(data.ePile)
                    data.sPile = []
                
                if deckBot == 1: # to 1 - north west
                    botCard = data.sPile[0]
                    rank = getCardRank(botCard)
                    data.nwPile += data.sPile
                    data.sPile = []
                if deckBot == 3: # to 3 - north east
                    botCard = data.sPile[0]
                    rank = getCardRank(botCard)
                    data.nePile += data.sPile
                    data.sPile = []
                if deckBot == 6: # to 6 - south west
                    botCard = data.sPile[0]
                    rank = getCardRank(botCard)
                    data.swPile += data.sPile
                    data.sPile = []   
                if deckBot == 8: # to 8 - south east
                    botCard = data.sPile[0]
                    rank = getCardRank(botCard)
                    data.sePile += data.sPile
                    data.sPile = []
        else:
            print("Not a valid move")
            
    if action == "knock": #switch player turns
        print("You've knocked and indicated the end of your turn.")
        print()
        if data.humTurn: #increase round at end of hum turn
            data.playerRound += 1
            print("player round added:" + str(data.playerRound))
        else: # increase round at end of comp turn
            data.compRound += 1
            print("comp round added:" + str(data.compRound))
       
        print("before: " + str(data.humTurn))
        print("before: " + str(data.compTurn))
        data.humTurn = not data.humTurn
        data.compTurn = not data.compTurn
        print("after: " + str(data.humTurn))
        print("after: " + str(data.compTurn))
        print("Turns have been changed")
        data.xyTurnCards = getTurnCoords(data) #change xyTurnCard coords to the ones on the next person
        print(data.xyTurnCards)
        if data.compTurn: # if comp turn
            if data.compRound != 0: 
        #after first round you get delt a single card every round @ begin
                addCard = PlayingCard.dealCard(data.gameDeck)
                print("card has been added to comp hand/player2")
                data.compHand.append(addCard)
                data.xyTurnCards = getTurnCoords(data)
        else:
            if data.playerRound != 0:
                addCard = PlayingCard.dealCard(data.gameDeck)
                print("card has been added to player hand/player1")
                data.playerHand.append(addCard)
                data.xyTurnCards = getTurnCoords(data)
                    
########################################
# Table display 
########################################
from tkinter import *

def init(data):
    loadPlayingCardImages(data) # always load images in init!
    resetGame(data)
    data.home = True
    data.rules = False
    data.game = False
    data.gameOver = False
    data.winner = None
    data.cardW = data.cardWidth//2 # half card w
    data.cardH = data.cardHeight//2 # half card h
    
def resetGame(data):
    data.home = False
    data.rules = False
    data.game = True
    data.gameOver = False
    data.winner = None
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
    print("player:" + str(data.playerHand))
    print("comp: " + str(data.compHand))
    data.nPile = [PlayingCard.dealCard(data.gameDeck)] #cards to display on north deck
    data.ePile = [PlayingCard.dealCard(data.gameDeck)]   
    data.sPile = [PlayingCard.dealCard(data.gameDeck)]   
    data.wPile = [PlayingCard.dealCard(data.gameDeck)]
    data.nePile = []   
    data.sePile = []   
    data.swPile = []   
    data.nwPile = []
    data.playerRound = 0
    data.compRound = 0
    data.xyTurnCards = [] #list containing tuples of the (x,y) coords of cards of the player whose turn it is
    data.margin = data.width//10
    data.cardHeight = 96
    data.cardWidth = 71
    data.xyTurnCards = getTurnCoords(data)
    
def getTurnCoords(data): 
#updates a list containing the position of the cards depending on whose turn it is
#function needs to be called every time it changes turns
    if data.humTurn:
        newCoords = []
        if len(data.playerHand) > 10: 
            cards = len(data.playerHand)
            yplace = data.height - 60
            num = 0 
            index = 0
            while cards > 0: 
                newCoords.append((data.margin + (i*cardWidth), yplace))
                cards -= 1
                num += 1
                index += 1
                if cards == 10:
                    yplace -= 100
                    num = 0
            return newCoords
        else:
            yplace = data.height - 60
            for i in range(len(data.playerHand)):
                newCoords.append((data.margin + (i*data.cardWidth), yplace))
            return newCoords
    else:
        newCoords = []
        if len(data.compHand) > 10: 
            cards = len(data.compHand)
            yplace = data.height - 60
            num = 0 
            index = 0
            while cards > 0: 
                newCoords.append((data.margin + (i*cardWidth), yplace))
                cards -= 1
                num += 1
                index += 1
                if cards == 10:
                    yplace -= 100
                    num = 0
            return newCoords
        else:
            yplace = data.height - 60
            for i in range(len(data.compHand)):
                newCoords.append((data.margin + (i*data.cardWidth), yplace))
            return newCoords
    
    
def mousePressed(event, canvas, data):
    pass

def keyPressed(event, data):
    if event.keysym == "p": # enter game mode
        print("p was pressed")
        data.home = False
        data.game = True
        data.rules = False
    if event.keysym == "h": # enter rules screen
        data.home = False
        data.game = False
        data.rules = True
    if event.keysym == "z": #reset game play again
        resetGame(data)
    # if space bar hit start who's ever turn it is
    # put input parts of turn in this loop
    # to make another move press space again 
    cards = 0 # select card by key press
    if data.compTurn:
        cards = len(data.compHand)
    else:
        cards = len(data.playerHand)
    indices = []    
    for i in range(1, cards):
            indices += [i] 
    if data.humTurn:
        if event.keysym in indices:
            data.selectedCard = data.playerHand[event.keysym-1]
            data.selectedXY = data.xyTurnCards[event.keysym-1]
    else:
        if event.keysym in indices:
            data.selectedCard = data.playerHand[event.keysym-1]
            data.selectedXY = data.xyTurnCards[event.keysym-1]
        
    if event.keysym == "space":
        action = input("What do you want to do? \nTo play a card enter, 'play'.\nTo move a pile on the table enter, 'move'. \nTo knock and end your turn enter, 'knock'.\n")
        action = action.lower()
    
        while not action in ["play", "move", "knock"]: #checks for valid input
            print("Invalid input")
            action = input("What do you want to do? \nTo play a card enter, 'play'. \nTo move a pile on the table enter, 'move'. \nTo knock and end your turn enter, 'knock'.\n")
            action = action.lower()
        if data.compTurn: # who's ever turn 
            print("Computer/player 2 turn")
            humanTurn(action, data)
        else: 
            print("human/player1")
            humanTurn(action, data)
        if data.playerHand == []: #if either player has 0 cards then they win
            data.gameOver = True
            data.game = False
            data.home = False
            data.rules = False
            data.winner = "Player 1"
            
        if data.compHand == []:
            data.gameOver = True
            data.game = False
            data.home = False
            data.rules = False
            data.winner = "Computer/Player 2"
        
        print("north: " + str(data.nPile))
        print("east: " + str(data.ePile))
        print("south: " + str(data.sPile))
        print("west: " + str(data.wPile))
        print("north west: " + str(data.nwPile))
        print("north east: " + str(data.nePile))
        print("south west: " + str(data.swPile))
        print("south east: " + str(data.sePile))
        print("play hand: " + str(data.playerHand))
        print("comp hand: " + str(data.compHand))
        
        if data.gameOver:
            print("The winner is: " + data.winner) 
            ans = input("Would you like to play again? yes or no?")
            ans = ans.lower()
            answers = ["no", "yes"]
            while ans not in answers:
                print("Please stick to yes or no.")
                ans = input("Would you like to play again? yes or no?")
                ans = ans.lower()
            if ans == "yes":
                resetGame(data)
            else:
                return 

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
            fill="#076324") # green table background
        
        drawPiles(canvas, data) # calls drawPiles file to draw all the piles on the board
                    
        # if data.selectedXY != None: #draws yellow around selected card
        #     x, y = data.selectedXY
        #     canvas.create_rectangle(x-data.cardW-2, y-data.cardH-2, 
        #                     data.cardW+x+2, data.cardH+y+2,
        #                     outline="yellow", width="3")
        
        if data.humTurn: #HUMAN TURN DISPLAY
            # FOR NOW IT JUST DISPLAY'S THE CARDS OF WHOSE EVER TURN IT IS THERE IS NO 
            # HUMAN AND COMPUTER BUT JUST A PLAYER 1 AND PLAYER 2 BUT THEY ARE NAMED
            # COMPUTER AND HUMAN FOR FUTURE REFERENCE 
            #display human cards/player 1 
            canvas.create_text(10, data.height - 300, text="Player 1's turn.\nPress the space bar to do something.",
                                fill="black", anchor=W)
                                
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
                    canvas.create_image(data.margin + (num*data.cardWidth), 
                            yplace, image=img)
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
                    canvas.create_image(data.margin + (i*data.cardWidth), 
                                yplace, image=img)
        
            #display computer/player 2 cards backs     
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
                
        else: #COMPUTER TURN DISPLAY
            canvas.create_text(10, data.height - 300, text="Player 2's turn.\nPress the space bar to do something.",
                                fill="black", anchor=W)
            #display comp hand cards/player 2
            if len(data.compHand) > 10: 
            #dispays 10 cards per line so the cards don't run off the board
                cards = len(data.compHand)
                yplace = data.height - 60
                num = 0 
                index = 0
                while cards > 0: #display cards in player 2/comp hand
                    suit = getCardSuit(data.compHand[index])
                    rank = getCardRank(data.compHand[index])
                    img = getPlayingCardImage(data, rank, suit)
                    canvas.create_image(data.margin + (num*data.cardWidth), 
                                yplace, image=img)
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
                    canvas.create_image(data.margin + (i*data.cardWidth), 
                                yplace, image=img)
        
            #display player 1/human cards backs     
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
   
    if data.gameOver: # prints the winner 
        txt = "%s is the winner! Congratulations.%(data.winner)"
        canvas.create_text(data.width//2, data.height-50, text=txt, fill="black", font="Arial 50 bold")
        
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

run(900, 800)