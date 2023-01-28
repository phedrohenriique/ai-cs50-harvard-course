"""
Tic Tac Toe Player
"""

import math

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
    i_counter = 0
    j_counter = 0

    possible_actions = []
    if board:
        for row in board:
            for column in row:
                if column == EMPTY:
                    possible_actions.append((i_counter, j_counter))
                if j_counter < 2:
                    j_counter = j_counter + 1
                else:
                    j_counter = 0
                
            if i_counter < 2:
                i_counter = i_counter+1
            else:
                i_counter = 0

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    without modifying the original board.
    board = []
    action = (i,j)
    """

    try:
        if action in actions(board):
            new_board = board.copy()
            new_board.remove(action)
            return new_board
        else:
            Exception
    except:
        return Exception

def winner(board):
    """
    Returns the winner of the game, if there is one.
    It shall be compared per cell instead of state,
    it verifies if the possible winning actions are not in the actions
    array
    """
    # can use winning_positions_list
    board_winner = board.copy()
    actions_list = actions(board)
    #print('possible actions : ',actions_list)

    winner_x = 0
    winner_o = 0

    for position_list in winning_positons_list:
        #print('position list : ', position_list)
        player_winning_list = []
        for position in position_list:
            player_winning_list.append(board[position[0]][position[1]])
        ## counter variable
        #print('player winning list : ', player_winning_list)
        for player in player_winning_list:
            if player == X:
                winner_x = winner_x + 1
            if player == O:
                winner_o = winner_o + 1
        #print('x counter : ', winner_x)
        #print('o counter : ', winner_o)
        if winner_x == 3 :
            print('player x won')
            return
        if winner_o == 3 :
            print('player o won')
            return

        winner_x = 0
        winner_o = 0

    if winner_o == 0 and winner_x ==0 :
        print('no winner')  

    #print('player_winning_list : ', player_winning_list)
    # print('no winner')
    # return None
            
        
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

if __name__ == "__main__":
    #print('Testing Functions')
    #print(actions(board_state))
    print('Script Test Running...')
    winner(board_state_test_x)
    winner(board_state_test_o)
    winner(board_state_test_draw)