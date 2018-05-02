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
        if pileMove == 2: # moving north pile
            bottom = data.nPile[0] # bottom card of the north pile
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4: # moving to west pile 
                top = data.wPile[-1] # top card of the west pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("Same color. 2 > 4.")
                    return False
                if tRank - 1 != bRank:
                    print("Not right ranks. 2>4")
                    return False
                return True
                
            if pilePut == 5: # moving to east pile 
                top = data.ePile[-1] # top card of east pile 
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("same color. 2 > 5")
                    return False
                if tRank - 1 != bRank:
                    print("not right ranks, 2>5")
                    return False
                return True
        
            if pilePut == 7: # moving to south pile 
                top = data.sPile[-1] # top card of south pile 
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("same color. 2 > 7")
                    return False
                if tRank - 1 != bRank:
                    print("not right rank 2 >7")
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
                            print("same color. 2 > 8")
                            return False
                        if tRank - 1 != bRank:
                            print("not right rank, 2 >8")
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
                            print("same color, 2 >6")
                            return False
                        if tRank - 1 != bRank:
                            print("not right rank, 2>6")
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
                            print("same color 2>3")
                            return False
                        if tRank - 1 != bRank:
                            print("not right ranks, 2>3")
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
                            print("same color 2>1")
                            return False
                        if tRank - 1 != bRank:
                            print("wrong ranks 2>1")
                            return False
                        return True
        if pileMove == 4: # moving west pile 
            bottom = data.wPile[0] # bottom card of the west pile  
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 2: # moving to north pile 
                top = data.nPile[-1] # top card of the north pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("sm col 4 >2")
                    return False
                if tRank - 1 != bRank:
                    print("wrg rank 4 >2")
                    return False
                return True
                
            if pilePut == 5: # moving to east pile
                top = data.ePile[-1] # top card of the east pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("color 4>5")
                    return False
                if tRank - 1 != bRank:
                    print("rank 4>5")
                    return False
                return True
        
            if pilePut == 7: # moving to south pile
                top = data.sPile[-1] # top card of south pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("col 4>7")
                    return False
                if tRank - 1 != bRank:
                    print("rank 4>7")
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
                            print("col 4>8")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 4>8")
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
                            print("col 4>6")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 4>6")
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
                            print("col 4>3")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 4>3")
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
                            print("col 4>1")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 4 >1")
                            return False
                        return True
            
        if pileMove == 5: # moving east pile
            bottom = data.ePile[0] # bottom card of the east pile 
            bSuit = getCardSuit(bottom)
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4: # moving to west pile 
                top = data.wPile[-1] # top card of the west pile 
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("col 5>4")
                    return False
                if tRank - 1 != bRank:
                    print("rank 5>4")
                    return False
                return True
                
            if pilePut == 2: # move to north pile
                top = data.nPile[-1] # top card of north pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("col 5>2")
                    return False
                if tRank - 1 != bRank:
                    print("rank 5>2")
                    return False
                return True
        
            if pilePut == 7: # move to south pile
                top = data.sPile[-1] # top card of south pile
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("col 5>7")
                    return False
                if tRank - 1 != bRank:
                    print("col 5>7")
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
                            print("col 5>8")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 5>8")
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
                            print("col 5>6")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 5>6")
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
                            print("col 5>3")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 5>3")
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
                            print("col 5>1")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 5>1")
                            return False
                        return True
                        
        if pileMove == 7: # South pile chosen to move
            bottom = data.sPile[0] # bottom card of south pile you're moving 
            bSuit = getCardSuit(bottom) 
            bRank = getCardRank(bottom)
            bCol = None
            if bSuit in ["Hearts", "Diamonds"]:
                bCol = "red"
            else:
                bCol = "black"
            if pilePut == 4: # move to west pile
                top = data.wPile[-1] # top card of the west pile you're moving ON TO
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("col 7>4")
                    return False
                if tRank - 1 != bRank:
                    print("rank 7>4")
                    return False
                return True
                
            if pilePut == 5: # move to east pile 
                top = data.ePile[-1]# top card of the east pile you're moving ON TO
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("col 7>5")
                    return False
                if tRank - 1 != bRank:
                    print("rank 7>5")
                    return False
                return True
        
            if pilePut == 2:#move to north pile
                top = data.nPile[-1]  # top card of the north pile you're moving ON TO
                tSuit = getCardSuit(top)
                tRank = getCardRank(top)
                tCol = None
                if tSuit in ["Hearts", "Diamonds"]:
                    tCol = "red"
                else:
                    tCol = "black"
                if tCol == bCol:
                    print("col 7>2")
                    return False
                if tRank - 1 != bRank:
                    print("rank 7>2")
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
                            print("col 7>8")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 7>8")
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
                            print("col 7>6")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 7>6")
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
                            print("col 7>3")
                            return False
                        if tRank - 1 != bRank:
                            print("rank 7>3")
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
                            print("fail col 7>1")
                            return False
                        if tRank - 1 != bRank:
                            print("fail rank 7>1")
                            return False
                        return True