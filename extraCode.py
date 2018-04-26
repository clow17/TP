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

#def mousePressed(event, canvas, data):
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
    # x, y = data.nXY[0]
    # if (x-data.cardW <= event.x <= x+data.cardW and
    #             y-data.cardH <= event.y <= y+data.cardH):
    #     data.deckSelXY = data.nXY[0]
    #     data.deckSelCard = data.nPile[-1]
    # 
    # x,y = data.eXY[0]
    # if (x-data.cardW <= event.x <= x+data.cardW and
    #             y-data.cardH <= event.y <= y+data.cardH):
    #     data.deckSelXY = data.eXY[0]
    #     data.deckSelCard = data.ePile[-1]
    # 
    # x,y = data.sXY[0]
    # if (x-data.cardW <= event.x <= x+data.cardW and
    #             y-data.cardH <= event.y <= y+data.cardH):
    #     data.deckSelXY = data.sXY[0]
    #     data.deckSelCard = data.sPile[-1]
    # 
    # x,y = data.wXY[0]
    # if (x-data.cardW <= event.x <= x+data.cardW and
    #             y-data.cardH <= event.y <= y+data.cardH):
    #     data.deckSelXY = data.wXY[0]
    #     data.deckSelCard = data.wPile[-1]
    
    # def onMouseMovedWrapper(event, canvas, data):
    #     onMouseMoved(event, canvas, data)
    #     redrawAllWrapper(canvas, data)
    #     
    # def onMouseReleasedWrapper(event, canvas, data):
    #     onMouseReleased(event, data)
    #     redrawAllWrapper(canvas, data)
    
    # root.bind("<B1-Motion>", lambda event:
    #                         onMouseMovedWrapper(event, canvas, data))
    # root.bind("<ButtonRelease-1>", lambda event:
    #                         onMouseReleasedWrapper(event, canvas, data))
    
    # data.origIndex = None
    # data.oldX = None
    # data.oldY = None
    # data.card = None
    # data.dragImg = {"x": 0, "y": 0, "card": None}
    
    # data.nXY = [(data.width//2, data.height//2 - 100)] # (x,y) coords of cards on pile 
    # data.eXY = [(data.width//2 + 100, data.height//2)]
    # data.sXY = [(data.width//2, data.height//2 + 100)]
    # data.wXY = [(data.width//2 - 100, data.height//2)]
    # data.neXY = [(data.width//2 -100,data.height//2 + 100)] #position of ne pile
    # data.seXY = [(data.width//2 +100, data.height//2 +100)]
    # data.swXY = [(data.width//2 -100, data.height//2 + 100)]
    # data.nwXY = [(data.width//2 -100, data.height//2 -100)]

# def drawCard(x, y, card):
#     suit = getCardSuit(card)
#     rank = getCardRank(card)
#     img = getPlayingCardImage(data, rank, suit)
#     canvas.create_image(x, y, image=img)