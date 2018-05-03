########################
# File contains testing of a valid move of piles to other pile, 
# valid playing of card, and tesing if play is a valid move if it's a king
# All return True or False for whether the move or play is a valid one 
#########################
from DeckDeal import *
def validPlay(pile, card, data):
    suit = getCardSuit(card)
    rank = getCardRank(card)
    reds = ["Hearts", "Diamonds"]
    blacks = ["Clubs", "Spades"]
    playColor = None
    if suit in reds:
        playColor = "red"
    else: 
        playColor = "black"
    if pile == 2:
        if data.nPile == []:
            return True
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
        if data.wPile == []:
            return True
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
        if data.ePile == []:
            return True
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
        
    elif pile == 7:
        if data.sPile == []:
            return True
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
    elif pile == 1:
        if data.nwPile == []:
            return False
        else:
            deckSuit = getCardSuit(data.nwPile[-1])
            deckRank = getCardRank(data.nwPile[-1])
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
    elif pile == 3:
        if data.nePile == []:
            return False
        else:
            deckSuit = getCardSuit(data.nePile[-1])
            deckRank = getCardRank(data.nePile[-1])
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
    elif pile == 6:
        if data.swPile == []:
            return False
        else:
            deckSuit = getCardSuit(data.swPile[-1])
            deckRank = getCardRank(data.swPile[-1])
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
    else: # pile == 8
        if data.sePile == []:
            return False
        else:
            deckSuit = getCardSuit(data.sePile[-1])
            deckRank = getCardRank(data.sePile[-1])
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
    
def placeKing(data, pile, card, xy):
    if "King" not in str(card):
        return False
    else:
        if data.humTurn:
            if pile == 1:
                if data.nwPile != []:
                    return False
                else:
                    return True
            elif pile == 3:
                if data.nePile != []:
                    return False
                else:
                    return True
            elif pile == 6:
                if data.swPile != []:
                    return False
                else:
                    return True
            else:
                if data.sePile != []:
                    return False
                else:
                    return True
        else:
            if pile == 1:
                if data.nwPile != []:
                    return False
                else:
                    return True
            elif pile == 3:
                if data.nePile != []:
                    return False
                else:
                    return True
            elif pile == 6:
                if data.swPile != []:
                    return False
                else:
                    return True
            else:
                if data.sePile != []:
                    return False
                else:
                    return True

def validMove(data, pileMove, pilePut): 
#checks if moving one pile on top of another is legals
    if 0 > pileMove or pileMove > 8 or 0 > pilePut or pilePut > 8 or pileMove == pilePut:
        print("Not a valid pile input.")
        return False
        
    else:
        if pileMove == 2: # moving north pile
            if data.nPile == []:
                return False
            bottom = data.nPile[0] # bottom card of the north pile
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4: # moving to west pile
                if data.wPile == []:
                    return False
                top = data.wPile[-1] # top card of the west pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
                
            if pilePut == 5: # moving to east pile
                if data.ePile == []:
                    return False
                top = data.ePile[-1] # top card of east pile 
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
        
            if pilePut == 7: # moving to south pile 
                if data.sPile == []:
                    return False
                top = data.sPile[-1] # top card of south pile 
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
            
            if pilePut in [1, 3, 6, 8]: # want to move card to a corner 
            #test if a king is in the cardinal dirs can move to corners
                if bRank == 13: # if the rank of the card you're moving is 13
                    if pilePut == 1 and data.nwPile == []: # noking there
                        return True
                    if pilePut == 3 and data.nePile == []:
                        return True
                    if pilePut == 6 and data.swPile == []:
                        return True
                    if pilePut == 8 and data.sePile == []:
                        return True
                else: # want to move something onto a king 
                    if pilePut == 8: # move to south east pile
                        top = data.sePile[-1] # top card of south east pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 6: # move to south west pile 
                        top = data.swPile[-1] # top card of south west pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 3: #move to north east pile
                        top = data.nePile[-1] #top card of the north east pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 1: # move to north west pile
                        top = data.nwPile[-1] # top card of the north east pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
        if pileMove == 4: # moving west pile 
            if data.wPile == []:
                return False
            bottom = data.wPile[0] # bottom card of the west pile  
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 2: # moving to north pile 
                if data.nPile == []:
                    return False
                top = data.nPile[-1] # top card of the north pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
                
            if pilePut == 5: # moving to east pile
                if data.ePile == []:
                    return False
                top = data.ePile[-1] # top card of the east pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
        
            if pilePut == 7: # moving to south pile
                if data.sPile == []:
                    return False
                top = data.sPile[-1] # top card of south pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
            
            if pilePut in [1, 3, 6, 8]: 
            #test if a king is in the cardinal dirs can move to corners
                if bRank == 13:
                    if pilePut == 1 and data.nwPile == []:
                        return True
                    if pilePut == 3 and data.nePile == []:
                        return True
                    if pilePut == 6 and data.swPile == []:
                        return True
                    if pilePut == 8 and data.sePile == []:
                        return True
                else:
                    if pilePut == 8: # move to south east pile
                        top = data.sePile[-1] # top card of the south east pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 6: # move to south west pile
                        top = data.swPile[-1] # top card of the south west pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 3: #move to north east pile
                        top = data.nePile[-1] # top card of north east pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 1: # move to north west pile
                        top = data.nwPile[-1] # top card of north west pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
            
        if pileMove == 5: # moving east pile
            if data.ePile == []:
                return False
            bottom = data.ePile[0] # bottom card of the east pile 
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4: # moving to west pile 
                if data.wPile == []:
                    return False
                top = data.wPile[-1] # top card of the west pile 
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
                
            if pilePut == 2: # move to north pile
                if data.nPile == []:
                    return False
                top = data.nPile[-1] # top card of north pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
        
            if pilePut == 7: # move to south pile
                if data.sPile == []:
                    return False
                top = data.sPile[-1] # top card of south pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
                
            if pilePut in [1, 3, 6, 8]: # want to move card to a corner 
            #test if a king is in the cardinal dirs can move to corners
                if bRank == 13:
                    if pilePut == 1 and data.nwPile == []:
                        return True
                    if pilePut == 3 and data.nePile == []:
                        return True
                    if pilePut == 6 and data.swPile == []:
                        return True
                    if pilePut == 8 and data.sePile == []:
                        return True
                else:
                    if pilePut == 8: # move to south east pile
                        top = data.sePile[-1] # top card of south east pile 
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 6: # move to south west pile
                        top = data.swPile[-1] # top card of south west pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 3: # move to north east pile 
                        top = data.nePile[-1] # top card of north east pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 1: # move to north west pile 
                        top = data.nwPile[-1] # top card of north west pile 
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                        
        if pileMove == 7: # South pile chosen to move
            if data.sPile == []:
                return False
            bottom = data.sPile[0] # bottom card of south pile you're moving 
            bSuit = getCardSuit(bottom) 
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4: # move to west pile
                if data.wPile == []:
                    return False 
                top = data.wPile[-1] # top card of the west pile you're moving ON TO
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
                
            if pilePut == 5: # move to east pile
                if data.ePile == []:
                    return False
                top = data.ePile[-1]# top card of the east pile you're moving ON TO
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
        
            if pilePut == 2:#move to north pile
                if data.nPile == []:
                    return False
                top = data.nPile[-1]  # top card of the north pile you're moving ON TO
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    return False
                if tRank - 1 != bRank:
                    return False
                return True
            
            if pilePut in [1, 3, 6, 8]: # want to move card to a corner 
            #test if a king is in the cardinal dirs can move to corners
                if bRank == 13:
                    if pilePut == 1 and data.nwPile == []:
                        return True
                    if pilePut == 3 and data.nePile == []:
                        return True
                    if pilePut == 6 and data.swPile == []:
                        return True
                    if pilePut == 8 and data.sePile == []:
                        return True
                else:
                    if pilePut == 8: #move to south east pile
                        top = data.sePile[-1] # top card of south east pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 6: # move to south west pile
                        top = data.swPile[-1] # top card of south west pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 3: #move to north east pile
                        top = data.nePile[-1] #top card of north east pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True
                    if pilePut == 1: # move to north west pile 
                        top = data.nwPile[-1] # top card of north west pile
                        tSuit = getCardSuit(top)
                        tRank = getCardRank(top)
                        tCol = None
                        if tSuit in ["Hearts", "Diamonds"]:
                            tCol = "red"
                        else:
                            tCol = "black"
                        if tCol == bCol:
                            return False
                        if tRank - 1 != bRank:
                            return False
                        return True