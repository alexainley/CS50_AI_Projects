"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    XCount = 0
    OCount = 0
    ECount = 0

    #Count the number of X and Os
    for row in board:
        XCount += row.count(X)
        OCount += row.count(O)
        ECount += row.count(EMPTY)
    
    #if Xcount is higher than Os, return O, else must be X
    if XCount > OCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Actions = set()
    # if a spot in board is EMPTY, add to the set
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                Actions.add((i,j))
    return Actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    return board(action[0], action[1])


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #winner in a row...
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
        
    #Winner in column... 
    for i in range(3):
        column = ''
        for j in range(3):
             #read board and fill column
             column += str(board[j][i])

        #Check if the column is full
        if column == 'XXX':
            return X                
        elif column == 'OOO':
            return O

    diagT2B = ''
    diagB2T = ''
    # search diag from top left to bottom right 
    for i in range(3):
        j = i 
        diagT2B += str(board[j][i])
        print(diagT2B)
    
    # search diag from bottom left to top right
    j = 0
    for i in reversed(range(3)):
        diagB2T += str(board[i][j])
        j += 1

    #check if either have a set of 3 
    if diagT2B == 'XXX' or diagB2T == 'XXX':
        return X
    
    if diagT2B == 'OOO' or diagB2T == 'OOO':
        return O

    # No winner found
    return None
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Empty = 0
    #if either has won return true
    if (winner(board) == X) or (winner(board) == O):

        return True 
    #if any empty spots then game is stil true 
    for row in board:
        Empty += row.count(EMPTY)
    #no empty spots left 
    if Empty == 0:
        return True
    
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #get result
    result = winner(board)

    #return based on result
    if result == O:
        return -1
    elif result == X:
        return 1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # First check the game hasn't finished
    if terminal(board):
        return None
    
    else:
        #if player is x, get move from Max function
        if player(board) == X:
            value, move = Min(board)
            return move
        #if player is o, get move from min function
        if player(board) == O:
            value, move = Max(board)
            return move
    
    def Max(board):
        if terminal(board):
            return utility(board), None
        v = float('inf')
        next_move = None
        for action in actions(board):
            act = Min(result(board, action))
            if act> v:
                v = act
                move = action 
                if v == 1:
                    return v, move
        return v, move
                
    def Min(board):
        if terminal(board):
            return utility(board), None
        v = float('inf')
        next_move = None
        for action in actions(board):
            act = Max(result(board, action))
            if act > v:
                v = act
                move = action 
                if v == 1:
                    return v, move
        return v, move