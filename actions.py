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

def validMove(data, pileMove, pilePut): 
#checks if moving one pile on top of another is legals
    if 1 < pileMove > 8 or 1< pilePut > 8 or pileMove == pilePut:
        print("Not a valid pile input.")
        return False
        
    else:
        if pileMove == 2:
            bottom = data.nPile[0] # bottom card of the pile you're moving 
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4:
                top = data.wPile[-1] # top card of the pile you're moving ON TO
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
                
            if pilePut == 5:
                top = data.ePile[-1]
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
        
            if pilePut == 7:
                top = data.sPile[-1]
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
                if pileMove == 2:
                    if getCardRank(data.nPile[0]) == 13:
                        return True
                if pileMove == 4:
                    if getCardRank(data.wPile[0]) == 13:
                        return True
                if pileMove == 5:
                    if getCardRank(data.ePile[0]) == 13:
                        return True
                if pileMove == 7:
                    if getCardRank(data.sPile[0]) == 13:
                        return True
                return False
                        
                    
                top = data.wPile[-1] # top card of the pile you're moving ON TO
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
        
        if pileMove == 4:
            bottom = data.wPile[0] # bottom card of the pile you're moving 
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 2:
                top = data.nPile[-1] # top card of the pile you're moving ON TO
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
                
            if pilePut == 5:
                top = data.ePile[-1]
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
        
            if pilePut == 7:
                top = data.sPile[-1]
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
                if pileMove == 2:
                    if getCardRank(data.nPile[0]) == 13:
                        return True
                if pileMove == 4:
                    if getCardRank(data.wPile[0]) == 13:
                        return True
                if pileMove == 5:
                    if getCardRank(data.ePile[0]) == 13:
                        return True
                if pileMove == 7:
                    if getCardRank(data.sPile[0]) == 13:
                        return True
                return False
            
        if pileMove == 5:
            bottom = data.ePile[0] # bottom card of the pile you're moving 
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4:
                top = data.wPile[-1] # top card of the pile you're moving ON TO
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
                
            if pilePut == 2:
                top = data.nPile[-1]
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
        
            if pilePut == 7:
                top = data.sPile[-1]
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
                if pileMove == 2:
                    if getCardRank(data.nPile[0]) == 13:
                        return True
                if pileMove == 4:
                    if getCardRank(data.wPile[0]) == 13:
                        return True
                if pileMove == 5:
                    if getCardRank(data.ePile[0]) == 13:
                        return True
                if pileMove == 7:
                    if getCardRank(data.sPile[0]) == 13:
                        return True
                return False
        
        if pileMove == 7:
            bottom = data.sPile[0] # bottom card of the pile you're moving 
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4:
                top = data.wPile[-1] # top card of the pile you're moving ON TO
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
                
            if pilePut == 5:
                top = data.ePile[-1]
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
        
            if pilePut == 2:
                top = data.nPile[-1]
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
                if pileMove == 2:
                    if getCardRank(data.nPile[0]) == 13:
                        return True
                if pileMove == 4:
                    if getCardRank(data.wPile[0]) == 13:
                        return True
                if pileMove == 5:
                    if getCardRank(data.ePile[0]) == 13:
                        return True
                if pileMove == 7:
                    if getCardRank(data.sPile[0]) == 13:
                        return True
                return False