import copy

def checkWin(board):
    for row in board:
        for val in row:
            if val==0:
                return False
    return True


#state represented as [board,[i,j],parentState]
def moveHorizontal(currState,h,rows,cols):
    curr=currState[1]
    board=currState[0]
    new_curr=[curr[0],curr[1]+h]
    new_board=copy.deepcopy(board)
    new_board[new_curr[0]][new_curr[1]]=1
    new_parent=currState
    new_state=[new_board,new_curr,new_parent]
    return new_state


def moveVertical(currState,v,rows,cols):
    curr=currState[1]
    board=currState[0]
    new_curr=[curr[0]+v,curr[1]]
    new_board=copy.deepcopy(board)
    new_board[new_curr[0]][new_curr[1]]=1
    new_parent=currState
    new_state=[new_board,new_curr,new_parent]
    return new_state



def getChildren(state,rows,cols):
    children=[]
    board=state[0]
    curr=state[1]
    if ((curr[1]-1)>=0) and (board[curr[0]][curr[1]-1] == 0): #move left condition
        new_state=moveHorizontal(state,-1,rows,cols)
        children.append(new_state)
    if ((curr[1]+1)<cols) and (board[curr[0]][curr[1]+1] == 0) : # move right
        new_state=moveHorizontal(state,1,rows,cols)
        children.append(new_state)
    if ((curr[0]-1)>=0) and (board[curr[0]-1][curr[1]] == 0) :   #move top
        new_state=moveVertical(state,-1,rows,cols)
        children.append(new_state)
    if ((curr[0]+1)<rows) and (board[curr[0]+1][curr[1]] == 0) : #move bottom
        new_state=moveVertical(state,1,rows,cols)
        children.append(new_state)
    return children


def getAllStartPoints(board,rows,cols):
    starts=[]
    for i in range(rows):
        for j in range(cols):
            if board[i][j]==0 :
                new_board=copy.deepcopy(board)
                new_board[i][j]=1
                starts.append([new_board,[i,j],None])
    return starts



def getPath(winState):
    path=[]
    path.append(winState[1])
    parent=winState[2]
    while parent != None :
        path.append(parent[1])
        parent=parent[2]
    path.reverse()
    return path

def getPointDirection(curr,Next):
    if ((curr[0]+1)==Next[0]) and (curr[1]==Next[1]):
        return "down"
    elif ((curr[0]-1)==Next[0]) and (curr[1]==Next[1]):
        return "up"
    elif (curr[0]==Next[0]) and ((curr[1]+1)==Next[1]):
        return "right"
    elif (curr[0]==Next[0]) and ((curr[1]-1)==Next[1]):
        return "left"

def gelDirections(start,path):
    directions=[]
    curr=start
    for pos in path:
        directions.append(getPointDirection(curr,pos))
        curr=pos
    return directions

def search(rows,cols,obstacles):
    board= [[0 for x in range(cols)] for y in range(rows)]
    for obs in obstacles:
        board[obs[0]][obs[1]]=-1
    openList= getAllStartPoints(board,rows,cols)
    print(openList)
    successNode=None
    #closedList = []
    while len(openList)>0 :
        state = openList.pop()
        if checkWin(state[0]) :
            successNode=state
            break
        children=getChildren(state,rows,cols)
        openList+=children
    path=getPath(successNode)
    intial=path[0]
    directions=gelDirections(intial,path[1:])
    return [intial,directions]


        
    

