# Caitlyn Low caitlynl Section N
# Kings in the Corner (Card Game)
from DeckDeal import *
from actions import *
from drawPiles import *
###############################

#######################################
# COMPUTER PLAYER

def compTurn(data):
    for i in range(len(data.compHand)):
        playCard = data.compHand[i]
        for j in range(1,9):
            pile = j
            if (pile == 1 or pile == 3 or pile == 6 or pile == 8) and rank == 13:
                if placeKing(data, pile, card, xy) == True:
                    if pile == 1: 
                        data.nwPile.append(playCard)
                        data.compHand.remove(card)
                        data.xyTurnCards.remove(xy)
                    if pile == 3:
                        data.nePile.append(card)
                        if data.humTurn:
                            data.playerHand.remove(card)
                        else:
                            data.compHand.remove(card)
                        data.xyTurnCards.remove(xy)
                    if pile == 6:
                        data.swPile.append(card)
                        if data.humTurn:
                            data.playerHand.remove(card)
                        else:
                            data.compHand.remove(card)
                        data.xyTurnCards.remove(xy)
                    if pile == 8:
                        data.sePile.append(card)
                        if data.humTurn:
                            data.playerHand.remove(card)
                        else:
                            data.compHand.remove(card)
                        data.xyTurnCards.remove(xy)
            if validPlay(pile, playCard, data):
                
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
            
        while card-1 < 0 or card-1 > numCards: #makes sure card input is valid
            print("Invalid card choice")
            card = int(input("Type in the number for the card you want to put in. From top left to bottom right. Starting from 1.\n")) 
        xy = None
        if data.humTurn: # selects a card and it's x,y coords
            xy = data.xyTurnCards[card-1]
            card = data.playerHand[card-1]
        else:
            xy = data.xyTurnCards[card-1]
            card = data.compHand[card-1]
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
                if pile == 1: 
                    data.nwPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 3:
                    data.nePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 6:
                    data.swPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 8:
                    data.sePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
        else: #just regular move, not a king move
            if validPlay(pile, card, data) == False:
                print("That's not a valid move.")
            else:
                if pile == 2:
                    data.nPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 4:
                    data.wPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 5:
                    data.ePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 7:
                    data.sPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 1:
                    data.nwPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 3:
                    data.nePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 6:
                    data.swPile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
                if pile == 8:
                    data.sePile.append(card)
                    if data.humTurn:
                        data.playerHand.remove(card)
                    else:
                        data.compHand.remove(card)
                
                    
    if action == "move": #move one deck on top of another deck
        deckTop = int(input("Which deck do you want to move? \n1 2 3\n4   5\n6 7 8\n"))
        deckBot = int(input("Which pile would you like to move the deck you've selected to? \n1 2 3\n4   5\n6 7 8\n"))
        if validMove(data, deckTop, deckBot): #NEEEEEDS TO CHECK WHEN HAVE KING ON BOARD
            if deckTop == 2: #the deck you're putting on top/ From 2-North  
                if deckBot == 4: #the deck under the one you're moving/ to 4-west
                    data.wPile += data.nPile
                    data.nPile = []
                if deckBot == 5: # to 5-east
                    data.ePile += data.nPile
                    data.nPile = []
                if deckBot == 7: # to 7-south
                    data.sPile += data.nPile
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
                    data.wPile = []
                if deckBot == 5: # to 5 - east
                    data.ePile += data.wPile
                    data.wPile = []
                if deckBot == 7: # to 7 - south
                    data.sPile += data.wPile
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
                    data.ePile = [] 
                if deckBot == 4: # to 4 - west
                    data.wPile += data.ePile
                    data.ePile = [] 
                if deckBot == 7: # to 7 - south
                    data.sPile += data.ePile
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
                    data.sPile = []
                if deckBot == 4: # to 4 - west
                    data.wPile += data.sPile
                    data.sPile = []
                if deckBot == 5: # to 5 - east
                    data.ePile += data.sPile
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
        else: # increase round at end of comp turn
            data.compRound += 1
        data.humTurn = not data.humTurn
        data.compTurn = not data.compTurn
        data.xyTurnCards = getTurnCoords(data) #change xyTurnCard coords to the ones on the next person
        if data.compTurn: # if comp turn
            if data.compRound != 0: 
        #after first round you get delt a single card every round @ begin
                addCard = PlayingCard.dealCard(data.gameDeck)
                data.compHand.append(addCard)
                data.xyTurnCards = getTurnCoords(data)
        else:
            if data.playerRound != 0:
                addCard = PlayingCard.dealCard(data.gameDeck)
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
        data.home = False
        data.game = True
        data.rules = False
    if event.keysym == "r": # enter rules screen
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
            humanTurn(action, data)
        else: 
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
                root.destroy() 

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.home: #home screen 
        canvas.create_rectangle(0, 0, data.width, data.height, fill="#b3b3ff")
        welX = data.width//2
        welY = data.height//4
        canvas.create_text(welX, welY, fill="black", 
            text="Welcome to Kings\n     in the Corner", font=" Arial 50 bold")
        gameX = data.width//2
        gameY = data.height//2
        canvas.create_text(gameX, gameY, fill="black", 
            text="To start the game press 'p'.", font=" Arial 30 bold")
        canvas.create_text(gameX, gameY + 50, fill="black", text="To see the game rules press 'r'.", font="Arial 30 bold")
    if data.rules: # rules screen 
        canvas.create_rectangle(0, 0, data.width, data.height, fill="black")
        canvas.create_text(data.width, data.height, text="Rules screen", fill="black")
        obj = ("The objective of the game is to get rid of all your cards before the other player.") 
        gamePlay = ("At the start of the game 8 cards are dealt to each player. The rest of the deck is placed in the center of the table as\na stockpile. Then the top 4 cards are flipped over and placed north, east, south and west of the stockpile, these piles are\nreferred to as the foundational piles. Who's ever turn it is first will make as many valid moves as possible with the cards\nin their hand and 'knock' when they are finished. After the first round each player is deal a single card at the beginning\nof their turn.")
        cardPlay = ("Play a card or multiple cards on a foundational pile. Card play works a little like solitare in that you can only\nplay a card on another card if that card if ranked one lower that the one you're playing on top of. They also\nhave to be different suit colors. So if there is a black card on the top of the foundational pile you wish to put\nyour card, your card must be red and vise versa. Ex)You can play a '7 of Hearts' only on an '8 of Clubs' or\nan '8 of Spades'. \n\nAces are considered the lowest card and therefore no cards can be played on top of an ace.\n\nYou can also literally play a King in the corner. In the north east, north west, south west and south east\ndirections of the stockpile. Only Kings are allowed to be placed in the corners. Once a King has been\nplaced in the corner, players can then lay other cards on the pile as if it were another foundational pile.\nMoving an entire foundational pile onto another pile is also an option. If the move is valid play, you can make\nthe move and afterwards place any card from your hand in that spot.")
        gameSpecs = ("To initiate a play press the space bar. The consol will prompt you to type in 'play' to play a card,\n 'move' to move one pile to another, or 'knock' and end your turn. To see the rules of the game at\nany time press 'r'. To reset the game press 'z'. To play press 'p'.")  
        canvas.create_text(450, 50, text="How to Play Kings in the Corner", font="Arial 50  bold", fill="#80ccff")
        canvas.create_text(50, 120, text="Objective:", font="Arial 18 underline", fill="#ff9933")
        canvas.create_text(350, 115, text=obj, font="Arial 15", fill="white", anchor=N)
        canvas.create_text(55, 165, text="Game play:", font="Arial 18 underline", fill="#ff9933", anchor=N)
        canvas.create_text(500, 170, text=gamePlay, font="Arial 15", fill="white", anchor=N)
        canvas.create_text(85, 290, text="How to Play Cards:", font="Arial 18 underline", fill="#ff9933", anchor=N)
        canvas.create_text(170, 295, text=cardPlay, font="Arial 15", fill="white",anchor=NW)
        canvas.create_text(10, 550, text="Game specific directions:", font="Arial 18 underline", fill="#ff9933", anchor=NW)
        canvas.create_text(220, 555, text=gameSpecs, font="Arial 15", fill="white", anchor=NW) 
        canvas.create_text(450, 700, text="Happy playing!!", font="Arial 50", fill="#ff0066")
        canvas.create_text(450, 750, text="For my homie Hannah.", font="Arial 8", fill="white")
        
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