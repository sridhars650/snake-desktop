import pyautogui as pg
import array

pg.FAILSAFE = True

class GameBoard:
    def __init__(self):
        self.createGridCoords()

    def makeGameBoard(self):
        global gameBoard
        gameBoard = array.array('i',[1730,940])
        
    def createGridCoords(self):
        gameHeight = 1730
        numGameHeight = 17
        global rowCoords
        rowCoords = array.array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
        for i in range(17):
            rowCoords[i] = int(gameHeight/(numGameHeight*2) + i*(gameHeight/numGameHeight))
        # create the columns now
        gameWidth = 940
        numGameWidth = 12
        global colCoords
        colCoords = array.array('i', [1,2,3,4,5,6,7,8,9,10,11,12])
        for i in range(12):
            colCoords[i] = int(gameWidth/(numGameWidth/2) + i*(gameWidth/numGameWidth))
        print("Grid Created!")

    def getGridRowCoords(self, gridRow):
        if (gridRow >= 17 or gridRow <= -1):
            return -1
        try:
            rowCoord = rowCoords[gridRow]
            return rowCoord
        except:
            print("Didn't create GridRow!")
            return -1
        
    def getGridColCoords(self, gridCol):
        if (gridCol >= 12 or gridCol <= -1):
            return -1
        try:
            colCoord = colCoords[gridCol]
            return colCoord
        except:
            print("Didn't create GridCol!")
            return -1


gameBoard = GameBoard()
folderCount = 0

pg.PAUSE = 0.25

def createFolder(gridRow, gridCol):
    global folderCount
    rowCoord = gameBoard.getGridRowCoords(gridRow)
    colCoord = gameBoard.getGridColCoords(gridCol)
    pg.moveTo(rowCoord,colCoord)
    pg.rightClick()
    pg.click(x=pg.position().x+10,y=pg.position().y+10)
    for i in range(folderCount+2):
        pg.write(' ')
    pg.press('enter')
    folderCount += 1

createFolder(0,0)
createFolder(0,1)
createFolder(1,0)
createFolder(1,1)
createFolder(1,2)