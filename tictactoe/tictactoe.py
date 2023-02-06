"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

board_state = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

board_state_test_x = [
    [X, O, O],
    [EMPTY, X, EMPTY],
    [EMPTY, O, X]
]

board_state_test_o = [
    [O, O, O],
    [EMPTY, X, EMPTY],
    [EMPTY, O, X]
]

board_state_test_draw = [
    [O, X, O],
    [O, X, X],
    [X, O, X]
]

winning_positons_list = [
    [(0,0),(1,1),(2,2)], # diagonal
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)], # vertical
    [(0,2),(1,2),(2,2)],
    [(0,2),(1,1),(2,0)], # diagonal
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)], # horizontal
    [(2,0),(2,1),(2,2)],
]

def initial_state():
    """
    Returns starting state of the board.
    """
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
            ]

def player(board):

    """
    Returns player who has the next turn on a board.
    """

    x_counter = 0
    o_counter = 0

    for row in board:
        for column in row:
            if column == X:
                x_counter = x_counter+1
            if column == O:
                 o_counter = o_counter+1

    if x_counter and o_counter == 0:
        return X
    if ((x_counter+o_counter)%2 != 0):
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i = rows
    j = columns
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    without modifying the original board.
    board = []
    action = (i,j)
    """

    try:
        if action not in actions(board):
            return Exception
        else:
            new_board = copy.deepcopy(board)
            new_board[action[0]].pop(action[1])
            new_board[action[0]].insert(action[1], player(board))
            return new_board
    except:
        return Exception

def winner(board):
    """
    Returns the winner of the game, if there is one.
    It shall be compared per cell instead of state,
    it verifies if the possible winning actions are not in the actions
    array
    """

    for pos_list in winning_positons_list:
        if all(board[pos[0]][pos[1]] == X for pos in pos_list):
            return X
        if all(board[pos[0]][pos[1]] == O for pos in pos_list):
            return O
    return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    winner_player = winner(board)
    if winner_player == X:
        return True
    if winner_player == O:
        return True
    if actions(board) == []:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    The board parameter is equal to utility(terminal(board))
    """

    winner_player = winner(board)
    if winner_player == X :
        return 1
    if winner_player == O :
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Uses recursivity to achieve its goal.
    The minimax function should take a board as input, and return the optimal move for the player to move on that board.
The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
If the board is a terminal board, the minimax function should return None.
    """

    def min_value(board):
        if terminal(board):
            return utility(board)
        value = 1000000
        for action in actions(board):
            value = min(value, max_value(result(board, action)))
            if value == -1:
                break
        return value

    def max_value(board):
        if terminal(board):
            return utility(board)
        value = -1000000
        for action in actions(board):
            value = max(value, min_value(result(board, action)))
            if value == 1:
                break
        return value
        

    if board == terminal(board):
        return None

    best_move = None

    if player(board) == X:
        best_value = -1
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    else:
        best_value = 1
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

    return best_move

if __name__ == "__main__":
    print('Script Test Running...')