"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None
Infinity = 10000

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
    x_count=0
    o_count=0
    for row in board:
        for elem in row:
            if elem == X:
                x_count+=1
            if elem == O:
                o_count+=1
    if o_count < x_count: 
        return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = list()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] ==EMPTY:
                action_list.append((i,j))
    return action_list

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = initial_state()
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[i][j]=board[i][j]

    val = player(new_board)
    new_board[action[0]][action[1]]=val
    # print(new_board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = None
    # Horizontal check
    for i in range(len(board)):
        if board[i][0]!=EMPTY and board[i][0] == board[i][1] and  board[i][1]== board[i][2]:
            win = board[i][0]
            return win

    # Vertical check
    for i in range(len(board[0])):
        if board[0][i]!=EMPTY and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            win = board[0][i]
            return win
    
    # Diagonal check
    if board[0][0]!=EMPTY and board[0][0] == board[1][1] and board[1][1]== board[2][2]:
        win = board[0][0]
        return win
    if board[0][2]!=EMPTY and board[0][2] == board[1][1] and board[1][1]== board[2][0]:
        win = board[0][2]
        return win

    return win

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) !=None:
        return True
    if len(actions(board)) ==0:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win  = winner(board)
    if win ==X:
        return 1
    if win ==O:
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player_turn = player(board)
    action_list = actions(board)
    action_values = list()
    # Max_player
    if player_turn == X:
        for action in action_list:
            action_values.append(Min_Value(result(board,action)))
        """
        Original action as per minmiax algorithm
        """
        # return action_list[action_values.index(max(action_values))]   
        """
        Randomised action of the max values actions if maxvalue actions are more than one
        """
        return getAction(action_list,action_values,max(action_values))
    # Min Player
    if player_turn == O:
        for action in action_list:
            action_values.append(Max_Value(result(board,action)))
        """
        Original action as per minmiax algorithm
        """
        # return action_list[action_values.index(min(action_values))]   
        """
        Randomised action of the min values actions if minvalue actions are more than one
        """
        return getAction(action_list,action_values,min(action_values))
 
def Min_Value(board):
    """
    Returns the min val of all possible actions on board 
    """
    if terminal(board):
        return utility(board)   
    v = Infinity    
    for action in actions(board):
        v = min(v,Max_Value(result(board,action)))
    return v

def Max_Value(board):
    """
    Returns the max val of all possible actions on board 
    """
    if terminal(board):
        return utility(board)
    v = -Infinity
    for action in actions(board):
        v = max(v,Min_Value(result(board,action)))
    return v

def getAction(action_list,action_values,minimax_val):
    """
    Returns a random action of the actions with minmax_val
    """
    req_actions = list()
    min_val_indexs = [i  for i in range(len(action_values)) if action_values[i]==minimax_val]
    for i in range(len(min_val_indexs)):
        req_actions.append(action_list[min_val_indexs[i]])
    random.shuffle(req_actions)
    return req_actions[0]