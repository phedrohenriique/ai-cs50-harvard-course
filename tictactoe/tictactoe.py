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

player_x = 'player x'
player_o = 'player o'

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
        return player_x
    if ((x_counter+o_counter)%2 != 0):
        return player_x
    else:
        return player_o

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


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
