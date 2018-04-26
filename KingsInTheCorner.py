# Caitlyn Low caitlynl Section N
# Kings in the Corner (Card Game)
from DeckDeal import *
from actions import *
from drawPiles import *
###############################
#Notes about current version
# when you run the program a window pops up and asks you for an action and then errors and says
# drawPiles isn't defined, if you exit that window and other one pops up won't have that error 
# and the second window the picture won't pop up until after you've inputted a turn 
# at that point it will either conjure the spinning wheel of death or it just will not 
# prompt you for anything
# IN SHORT SHIT DON'T WORK SORRY

#######################################
# COMPUTER PLAYER
#######################################



#######################################
# Human Player or do I even need a human player?????
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
                
def humanTurn(data):
    action = input("What do you want to do? \nTo play a card enter, 'play'.\nTo move a pile on the table enter, 'move'. \nTo knock and end your turn enter, 'knock'.\n")
    action = action.lower()
    
    while not action in ["play", "move", "knock"]: #checks for valid input
        print("Invalid input")
        action = input("What do you want to do? \nTo play a card enter, 'play'. \nTo move a pile on the table enter, 'move'. \nTo knock and end your turn enter, 'knock'.\n")
        action = action.lower()
        
        
    if action == "play": #play a card from hand onto table piles
        card = int(input("Type in the number for the card you want to put in. From top left to bottom right."))
        pile = int(input("Which pile would you like to play your selected card on?\n1 2 3\n4   5\n6 7 8"))
        numCards = 0
        if humTurn:
            numCards = len(data.playerHand)
        if compTurn:
            numCards = len(data.playerHand)
            
        while 1 < card > numCards:
            print("Invalid card choice")
            card = int(input("Type in the number for the card you want to put in. From top left to bottom right.")) 
            
        while pile not in [1,2,3,4,5,6,7,8]:
            print("Invalid pile inputted")
            pile = int(input("Which pile would you like to play your selected card on?\n1 2 3\n4   5\n6 7 8"))
        rank = getCardRank(data.selectedCard)
        if (pile == 1 or pile == 3 or pile == 6 or pile == 8) and rank == 13:
            # runs this code if the card you select is a king and you're 
            # trying to move it to a corner
            if placeKing(data, pile) == False:
                print("The pile you selected is invalid. Either you are trying to put a card that is not a king in the corners or there is already a king there.")
            else:
                print("begin valid play of move king")
                print(data.playerHand)
                print(data.xyTurnCards)
                print()
                if pile == 1: 
                    data.nwPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                    print(data.playerHand)
                    print(data.xyTurnCards)
                if pile == 3:
                    data.nePile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                    print(data.playerHand)
                    print(data.xyTurnCards)
                if pile == 6:
                    data.swPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                    print(data.playerHand)
                    print(data.xyTurnCards)
                if pile == 8:
                    data.sePile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                    print(data.playerHand)
                    print(data.xyTurnCards)
        else:
            if validPlay(data, pile) == False:
                print("That's not a valid move man.")
            else:
                print("begin valid play not a king")
                print(data.compHand)
                print(data.xyTurnCards)
                print()
                if pile == 2:
                    data.nPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                    print(data.compHand)
                    print(data.xyTurnCards)
                if pile == 4:
                    data.wPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                    print(data.compHand)
                    print(data.xyTurnCards)
                if pile == 5:
                    data.ePile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                    print(data.compHand)
                    print(data.xyTurnCards)
                if pile == 7:
                    data.sPile.append(data.selectedCard)
                    if data.humTurn:
                        data.playerHand.remove(data.selectedCard)
                    else:
                        data.compHand.remove(data.selectedCard)
                    data.xyTurnCards.remove(data.selectedXY)
                    print(data.compHand)
                    print(data.xyTurnCards)
                    
    if action == "move": #move one deck on top of another deck
        deckTop = int(input("Which deck do you want to move? \n1 2 3\n4   5\n6 7 8\n"))
        deckBot = int(input("Which pile would you like to move the deck you've selected to? \n1 2 3\n4   5\n6 7 8\n"))
        if validMove(data, deckTop, deckBot): 
            if deckTop == 2:
                if deckBot == 4:
                    data.wPile += data.nPile
                    data.nPile = []
                if deckBot == 5:
                    data.ePile += data.nPile
                    data.nPile = []
                if deckBot == 7:
                    data.sPile += data.nPile
                    data.nPile = []
            
            if deckTop == 4:
                if deckBot == 2:
                    data.nPile += data.wPile
                    data.wPile = []
                if deckBot == 5:
                    data.ePile += data.wPile
                    data.wPile = []
                if deckBot == 7:
                    data.sPile += data.wPile
                    data.wPile = []
                    
            if deckTop == 5:
                if deckBot == 2:
                    data.nPile += data.ePile
                    data.ePile = [] 
                if deckBot == 4:
                    data.wPile += data.ePile
                    data.ePile = [] 
                if deckBot == 7:
                    data.sPile += data.ePile
                    data.ePile = [] 
            
            if deckTop == 7:
                if deckBot == 2:
                    data.nPile += data.sPile
                    data.sPile = []
                if deckBot == 4:
                    data.wPile += data.sPile
                    data.sPile = []
                if deckBot == 5:
                    data.ePile += data.sPile
                    data.sPile = []
        else:
            print("Not a valid move")
            
    if action == "knock": #switch player turns
        print("You've knocked and indicated the end of your turn.")
        print()
        if data.humTurn:
            data.playerRound += 1
        if data.compTurn:
            data.compRound += 1
        data.humTurn = not data.humTurn
        data.compTurn = not data.compTurn
        print("Turns have been changed")
        getTurnCoords(data) #change xyTurnCard coords to the ones on the next person
        print(data.xyTurnCards)
                    
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
                
    
    data.cardW = data.cardWidth//2 # half card w
    data.cardH = data.cardHeight//2 # half card h
    
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
                newCoords.append((data.margin + (i*cardWidth), yplace))
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
                newCoords.append((data.margin + (i*data.cardWidth), yplace))
            data.xyTurnCards = newCoords
    else:
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
            data.xyTurnCards = newCoords
        else:
            yplace = data.height - 60
            for i in range(len(data.compHand)):
                newCoords.append((data.margin + (i*data.cardWidth), yplace))
            data.xyTurnCards = newCoords
    
    
def mousePressed(event, canvas, data):
    for i in range(len(data.xyTurnCards)):
        x,y = data.xyTurnCards[i]
        if data.humTurn:     
            card = data.playerHand[i]
        else:
            card = data.compHand[i]
        if (x-data.cardW <= event.x <= x+data.cardW and
                y-data.cardH <= event.y <= y+data.cardH):
            data.selectedXY = data.xyTurnCards[i]
            data.selectedCard = card
            print(data.selectedXY)
            print(data.selectedCard)
            
def keyPressed(event, data):
    if event.keysym == "p":
        print("p was pressed")
        data.home = False
        data.game = True
        data.rules = False
    if event.keysym == "h":
        data.home = False
        data.game = False
        data.rules = True
    #if event.keysym == "a": #reset game play again
   
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
            data.selectedCard = data.playerHand[event.keysym]
            data.selectedXY = data.xyTurnCards[event.keysym]
            
    
    
    
    if data.compTurn: # who's ever turn 
        if data.compRound != 0: 
        #after first round you get delt a single card every round @ begin
            addCard = PlayingCard.dealCard(data.gameDeck)
            data.compHand.append(addCard)
        humanTurn(data)
    if data.humTurn:
        if data.playerRound != 0:
            addCard = PlayingCard.dealCard(data.gameDeck)
            data.playerHand.append(addCard)
        humanTurn(data)
    if event.keysym == "k": # check if display works for different player's cards
        data.humTurn = not data.humTurn
        data.compTurn = not data.compTurn
    ###run turns if turns are different store old turn

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
                    
        if data.selectedXY != None: #draws yellow around selected card
            x, y = data.selectedXY
            canvas.create_rectangle(x-data.cardW-2, y-data.cardH-2, 
                            data.cardW+x+2, data.cardH+y+2,
                            outline="yellow", width="3")
        
        if data.humTurn: #HUMAN TURN DISPLAY
            # FOR NOW IT JUST DISPLAY'S THE CARDS OF WHOSE EVER TURN IT IS THERE IS NO 
            # HUMAN AND COMPUTER BUT JUST A PLAYER 1 AND PLAYER 2 BUT THEY ARE NAMED
            # COMPUTER AND HUMAN FOR FUTURE REFERENCE 
            #display human cards/player 1 
            canvas.create_text(70, data.height - 300, text="Player 1's turn.",
                                fill="black")
                                
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
            canvas.create_text(70, data.height - 300, text="Player 2's turn.",
                                fill="black")
            #display comp hand cards/player 2
            if len(data.compHand) > 10: 
            #dispays 10 cards per line so the cards don't run off the board
                cards = len(data.compHand)
                yplace = data.height - 60
                num = 0 
                index = 0
                while cards > 0: #display cards in player 2/comp hand
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
   
    if data.gameOver: # prints the winner 
        print("The winner is: " + data.winner)
        print("To play again press 'a'")
        return 
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