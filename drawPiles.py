##################
# File draws all the piles on the table
##################

from KingsInTheCorner import *
def drawPiles(canvas, data):
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
            canvas.create_image(data.width//2 - 100, data.height//2
                -110,image=img)
                
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
            canvas.create_image(data.width//2 + 100, data.height//2 -
                110, image=img)
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
            canvas.create_image(data.width//2 - 100, data.height//2 + 
                110, image=img)
                
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
            canvas.create_image(data.width//2 + 100, data.height//2 +
                110, image=img)