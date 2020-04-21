"""
Tic Tac Toe Player
"""

import math
import copy

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
    # Looks for total number of X and O and returns max
    if any(None in row for row in board):
        XTotal = sum((row.count(X)for row in board))
        OTotal = sum((row.count(O)for row in board))
        
        if XTotal == OTotal:
            return X
        else:
            return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Returns location of all EMPTY spaces
    moves = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append([i, j])
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    i = action[0]
    j = action[1]
    
    if (i < 3 and j < 3) and board[i][j] == EMPTY:
        player_turn = player(board)
        new_board = copy.deepcopy(board)
        new_board[i][j] = player_turn
        return new_board
    
    else:
        return Exception('Invalid Move')   
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
# checks for winner across rows, columns and diagonals
    for i in range(3):
        # checks horizontals
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return O
    for i in range(3):    
        # Checks verticals
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O
        
    # Checks diagonals
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
        
    # If no winner return none
    return None 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks winner function for winner
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.    
    """
    if winner(board) == X:
        return 1
    
    elif winner(board) == O:
        return -1
    
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    which_player = player(board)
    
    for row in board:
        OTotal = sum((row.count(O)for row in board))
        XTotal = sum((row.count(X)for row in board))
        
        if OTotal == 0 and XTotal == 0:
            best_move = (-1, -1)
            return best_move   

    # if maximizing player (X Player)
    if which_player == X:      
        best_val = -math.inf
        for action in actions(board):
            value = MINPLAYER(result(board, action))
            if value > best_val:
                best_val = value
                best_move = action

    
    # if minimizing player (O Player)
    else:
        best_val = math.inf
        for action in actions(board):
            value = MAXPLAYER(result(board, action))
            if value < best_val:
                best_val = value
                best_move = action
                
    return best_move                


# Creating recursive MINIMAX functions
    
def MINPLAYER(board):
    if terminal(board):
        return utility(board)
    best_val = math.inf
    for action in actions(board):
        best_val = min(best_val, MAXPLAYER(result(board, action)))
        # if best_val <= alpha:
        #     beta = min(beta, best_val)
        #     break;
    
    return best_val    
    
def MAXPLAYER(board):
    if terminal(board):
        return utility(board)
    best_val = -math.inf
    for action in actions(board):
        best_val = max(best_val, MINPLAYER(result(board, action)))
        # if best_val >= beta:
        #     alpha = max(alpha, best_val)
            
    
    return best_val  
