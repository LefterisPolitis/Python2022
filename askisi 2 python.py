import random

finishcount=0
steps=0

kapakia=[1,2,3,]*9
grid=[[]]*3
for i in range(0,len(grid)):
    grid[i]=[0]*3

# grid [grammi][stili]

def GameIsFinished():
    global finishcount
    for i in range(0,3):
        if (grid[i][0]==grid[i][1] and grid[i][1]==grid[i][2] and not grid[i][2]==0):#katheta
            finishcount+=1
            return True
        if (grid[0][i]==grid[1][i] and grid[1][i]==grid[2][i]and not grid[2][i]==0):#orizodia
            finishcount+=1
            return True
    #diagonia
    if (grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2] and not grid[2][2]==0):
        finishcount+=1
        return True

    for i in range(0,3):
        if (grid[i][0]<grid[i][1] and grid[i][1]<grid[i][2] and not grid[i][0]==0):#katheta
            finishcount+=1
            return True
        if (grid[0][i]<grid[1][i] and grid[1][i]<grid[2][i]and not grid[0][i]==0):#orizodia
            finishcount+=1
            return True
    #diagonia
    if (grid[0][0]<grid[1][1] and grid[1][1]<grid[2][2] and not grid[0][0]==0 and not grid[1][1]==0 and not grid[2][2]==0):
        finishcount+=1
        return True
      
    return False

while (not finishcount==100):
    #RESTART GAME
    kapakia=[1,2,3,]*9
    grid=[[]]*3
    for i in range(0,len(grid)):
        grid[i]=[0]*3

    while (not (len(kapakia)>0 and GameIsFinished())):
        stepCompleted=False
        while(not (stepCompleted)):
            rowIndex=random.randint(0,2)
            columnIndex=random.randint(0,2)
            kapakiIndex=random.randint(0,len(kapakia)-1)
            if (grid[rowIndex][columnIndex]<kapakia[kapakiIndex]):
                print("MOVING "+str(kapakia[kapakiIndex])+" to ["+str(rowIndex)+","+str(columnIndex)+"] previously "+str(grid[rowIndex][columnIndex]))
                grid[rowIndex][columnIndex]=kapakia[kapakiIndex]
                print(grid)
                kapakia.pop(kapakiIndex) #vgazoume to xrisimopoihmeno kapaki apo tin lista mas
                stepCompleted=True 
        steps+=1
    print(steps)

print("MESOS OROS :"+str(steps/float(finishcount)))
