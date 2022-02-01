import random
#option 1 move white tower
#option 2 move black bishop

totalPoints=[0,0]


def CreateGrid(i,j):
    grid=[[]]*i
    for g in range(0,i):
        grid[g]=[0]*j
    return grid

def CheckDiagonally(i,j,oldI,oldJ):
    # pirame to max number gia na min trexei gia pada
    # alliws den tha kserame pote tha prepei na stamatisei to for loop
    maxNumber=max([i,j,oldI,oldJ]) +1
    diagonalPositions=[]
    for o in range(1,maxNumber):
        diagonalPositions.append([oldI-o,oldJ-o])
        diagonalPositions.append([oldI-o,oldJ+o])
        diagonalPositions.append([oldI+o,oldJ+o])
        diagonalPositions.append([oldI+o,oldJ-o])
    return ([i,j] in diagonalPositions)
        

#GAME LOGIC
def Game(dimensionI,dimensionJ,totalGamess):
    totalGames=totalGamess
    while(totalGames>0):
        #print("GAME #"+str(totalGamess-totalGames))
        totalPoints=[0,0]
        grid=CreateGrid(dimensionI,dimensionJ)
        totalGames-=1
        whiteTowerLocation=[]
        blackBishopLocation=[]
        # create white Tower
        while(True):
            iRand=random.randint(0,dimensionI-1)
            jRand=random.randint(0,dimensionJ-1)
            if (grid[iRand][jRand]==0):
                whiteTowerLocation=[iRand,jRand]
                grid[iRand][jRand]=1
                break

        # create black Bishop
        while(True):
            iRand=random.randint(0,dimensionI-1)
            jRand=random.randint(0,dimensionJ-1)
            if (grid[iRand][jRand]==0):
                blackBishopLocation=[iRand,jRand]
                grid[iRand][jRand]=2
                break
        #print(" *  WT = ["+str(whiteTowerLocation[0])+"]["+str(whiteTowerLocation[1])+"]")
        #print(" *  BB = ["+str(blackBishopLocation[0])+"]["+str(blackBishopLocation[1])+"]")

        WhiteWin=False
        BlackWin=False
        # Check if white tower wins
        for i in range(0,max(dimensionI,dimensionJ)-1):
            try:
                if (grid[whiteTowerLocation[0]][i]==2):
                    WhiteWin=True
                if (grid[i][whiteTowerLocation[1]]==2):
                    WhiteWin=True
            except:
                continue
        #Check if black bishop wins;
        BlackWin=CheckDiagonally(whiteTowerLocation[0],whiteTowerLocation[1],blackBishopLocation[0],blackBishopLocation[1])
        if (WhiteWin):
            totalPoints[0]+=1
        if (BlackWin):
            totalPoints[1]+=1
    print("---------------------------------------------")
    print("CHESSBOARD ["+str(dimensionI)+"]["+str(dimensionJ)+"]")
    print("ROUNDS "+str(totalGamess))
    print("---------------------------------------------")
    print("TOTAL POINTS OF WHITE :" +str(totalPoints[0]))
    print("TOTAL POINTS OF BLACK :"+ str(totalPoints[1]))
    print("---------------------------------------------")

Game(8,8,100)
Game(7,7,100)
Game(7,8,100)
