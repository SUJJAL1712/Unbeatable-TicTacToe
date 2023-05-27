import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_x = 0
    count_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            if cell == O:
                count_o += 1
    if count_x > count_o:
        return O
    else:
        return X


def actions(board):
    s = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                s.add((i, j))
    return s


def result(board, action):
    if terminal(board) or action not in actions(board):
        raise Exception("Invalid action")
    i, j = action
    temp = deepcopy(board)
    temp[i][j] = player(board)
    return temp


def winner(board):
    for i in board:
        if i[0] == i[1] == i[2] == X:
            return X
        if i[0] == i[1] == i[2] == O:
            return O
    if board[0][0] == board[1][0] == board [2][0] == X:
        return X
    if board[0][1] == board[1][1] == board [2][1] == X:
        return X
    if board[0][2] == board[1][2] == board [2][2] == X:
        return X
    if board[0][0] == board[1][0] == board [2][0] == O:
        return O
    if board[0][1] == board[1][1] == board [2][1] == O:
        return O
    if board[0][2] == board[1][2] == board [2][2] == O:
        return O
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O


def terminal(board):
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
        if v == 1:
            return v
    return v


def minvalue(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
        if v == -1:
            return v
    return v


def minimax(board):
    if terminal(board):
        return None
    possible_actions = actions(board)
    optimal_action = None
    if player(board) == X:
        tmp = float("-inf")
        for action in possible_actions:
            v = minvalue(result(board, action))
            if v > tmp:
                tmp = v
                optimal_action = action
            if tmp == 1:
                return optimal_action
    else:
        tmp = float("inf")
        for action in possible_actions:
            v = maxvalue(result(board, action))
            if v < tmp:
                tmp = v
                optimal_action = action
            if tmp == -1:
                return optimal_action
    return optimal_action
