########################
# File contains testing of a valid move of piles to other pile, 
# valid playing of card, and tesing if play is a valid move if it's a king
# All return True or False for whether the move or play is a valid one 
#########################
from DeckDeal import *
def validPlay(pile, card, data):
    suit = getCardSuit(card)
    rank = getCardRank(card)
    print("suit:" + str(suit))
    print("rank:" + str(rank))
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
        print("Deck suit:" + str(deckSuit))
        print("deck rank:" + str(deckRank))
        deckColor = None
        if deckSuit in reds:
            deckColor = "red"
        else: 
            deckColor = "black"
        if deckColor == playColor:
            print("failed on same color 2222")
            return False
        else:
            if deckRank - 1 != rank:
                print("failed on card rank being one below deck rank 2222")
                return False
            else:
                return True
    elif pile == 4:
        if data.wPile == []:
            return True
        deckSuit = getCardSuit(data.wPile[-1])
        deckRank = getCardRank(data.wPile[-1])
        print("Deck suit:" + str(deckSuit))
        print("deck rank:" + str(deckRank))
        deckColor = None
        if deckSuit in reds:
            deckColor = "red"
        else: 
            deckColor = "black"
        if deckColor == playColor:
            print("failed on same color 4444")
            return False
        else:
            if deckRank - 1 != rank:
                print("failed on card rank being one below deck rank 4444")
                return False
            else:
                return True
    elif pile == 5:
        if data.ePile == []:
            return True
        deckSuit = getCardSuit(data.ePile[-1])
        deckRank = getCardRank(data.ePile[-1])
        print("Deck suit:" + str(deckSuit))
        print("deck rank:" + str(deckRank))
        deckColor = None
        if deckSuit in reds:
            deckColor = "red"
        else: 
            deckColor = "black"
        if deckColor == playColor:
            print("failed on same color 55555")
            return False
        else:
            if deckRank - 1 != rank:
                print("failed on card rank being one below deck rank 5555")
                return False
            else:
                return True
        
    elif pile == 7:
        if data.sPile == []:
            return True
        deckSuit = getCardSuit(data.sPile[-1])
        deckRank = getCardRank(data.sPile[-1])
        print("Deck suit:" + str(deckSuit))
        print("deck rank:" + str(deckRank))
        deckColor = None
        if deckSuit in reds:
            deckColor = "red"
        else: 
            deckColor = "black"
        if deckColor == playColor:
            print("failed on same color 777777")
            return False
        else:
            if deckRank - 1 != rank:
                print("failed on card rank being one below deck rank 7777")
                return False
            else:
                return True
    elif pile == 1:
        if data.nwPile == []:
            return False
        else:
            deckSuit = getCardSuit(data.nwPile[-1])
            deckRank = getCardRank(data.nwPile[-1])
            print("Deck suit:" + str(deckSuit))
            print("deck rank:" + str(deckRank))
            deckColor = None
            if deckSuit in reds:
                deckColor = "red"
            else: 
                deckColor = "black"
            if deckColor == playColor:
                print("failed on same color 1111")
                return False
            else:
                if deckRank - 1 != rank:
                    print("failed on card rank being one below deck rank 11111")
                    return False
                else:
                    return True
    elif pile == 3:
        if data.nePile == []:
            return False
        else:
            deckSuit = getCardSuit(data.nePile[-1])
            deckRank = getCardRank(data.nePile[-1])
            print("Deck suit:" + str(deckSuit))
            print("deck rank:" + str(deckRank))
            deckColor = None
            if deckSuit in reds:
                deckColor = "red"
            else: 
                deckColor = "black"
            if deckColor == playColor:
                print("failed on same color 33333")
                return False
            else:
                if deckRank - 1 != rank:
                    print("failed on card rank being one below deck rank 3333")
                    return False
                else:
                    return True
    elif pile == 6:
        if data.swPile == []:
            return False
        else:
            deckSuit = getCardSuit(data.swPile[-1])
            deckRank = getCardRank(data.swPile[-1])
            print("Deck suit:" + str(deckSuit))
            print("deck rank:" + str(deckRank))
            deckColor = None
            if deckSuit in reds:
                deckColor = "red"
            else: 
                deckColor = "black"
            if deckColor == playColor:
                print("failed on same color 66666")
                return False
            else:
                if deckRank - 1 != rank:
                    print("failed on card rank being one below deck rank 6666")
                    return False
                else:
                    return True
    else: # pile == 8
        if data.sePile == []:
            return False
        else:
            deckSuit = getCardSuit(data.sePile[-1])
            deckRank = getCardRank(data.sePile[-1])
            print("Deck suit:" + str(deckSuit))
            print("deck rank:" + str(deckRank))
            deckColor = None
            if deckSuit in reds:
                deckColor = "red"
            else: 
                deckColor = "black"
            if deckColor == playColor:
                print("failed on same color 8888")
                return False
            else:
                if deckRank - 1 != rank:
                    print("failed on card rank being one below deck rank 888")
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
                    data.nwPile.append(card)
                    data.playerHand.remove(card)
                    data.xyTurnCards.remove(xy)
            elif pile == 3:
                if data.nePile != []:
                    return False
                else:
                    return True
                    data.nePile.append(card)
                    data.playerHand.remove(card)
                    data.xyTurnCards.remove(xy)
            elif pile == 6:
                if data.swPile != []:
                    return False
                else:
                    return True
                    data.swPile.append(card)
                    data.playerHand.remove(card)
                    data.xyTurnCards.remove(xy)
            else:
                if data.sePile != []:
                    return False
                else:
                    return True
                    data.sePile.append(card)
                    data.playerHand.remove(card)
                    data.xyTurnCards.remove(xy)
        else:
            if pile == 1:
                if data.nwPile != []:
                    return False
                else:
                    return True
                    data.nwPile.append(card)
                    data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
            elif pile == 3:
                if data.nePile != []:
                    return False
                else:
                    return True
                    data.nePile.append(card)
                    data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
            elif pile == 6:
                if data.swPile != []:
                    return False
                else:
                    return True
                    data.swPile.append(card)
                    data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)
            else:
                if data.sePile != []:
                    return False
                else:
                    return True
                    data.sePile.append(card)
                    data.compHand.remove(card)
                    data.xyTurnCards.remove(xy)

def validMove(data, pileMove, pilePut): 
#checks if moving one pile on top of another is legals
    if 0 > pileMove or pileMove > 8 or 0 > pilePut or pilePut > 8 or pileMove == pilePut:
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