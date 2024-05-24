import math
from copy import deepcopy

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
    # the next player turn will be to who has less number of playing
    # for example: if the number of X is less than number of O, then the next player turn will be X
    # otherwise, O will be the next turn

    # get the number of X in board
    x_count = sum(row.count(X) for row in board)

    # get the number of O in board
    o_count = sum(row.count(O) for row in board)

    # X player played more than O player, O turn
    if x_count > o_count:
        return O
    # else, X turn
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # for i in range(len(x)):
    #     for j in range(len(x[i])):
    #         print(x[i][j])
    possible_action = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_action.add((i, j))

    return possible_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check if the action is possible, if not raise exception
    if action not in actions(board):
        raise Exception("Not valid action")

    # get i,j value from action
    i, j = action

    # get a copy from board
    copy_board = deepcopy(board)

    # on i,j value call player function
    copy_board[i][j] = player(board)

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_row(board, X) or check_column(board, X) or check_first_dig(board, X) or check_second_dig(board, X):
        return X
    elif check_row(board, O) or check_column(board, O) or check_first_dig(board, O) or check_second_dig(board, O):
        return O
    else:
        return None


def check_row(board, play):
    # [[0,0 , 0,1 , 0,2],
    #  [1,0 , 1,1 , 1,2],
    #  [2,0 , 2,1 , 2,2]]

    # check row to see if there a win
    for i in range(len(board)):
        if board[i][0] == play and board[i][1] == play and board[i][2] == play:
            return True


def check_column(board, play):
    # [[0,0 , 0,1 , 0,2],
    #  [1,0 , 1,1 , 1,2],
    #  [2,0 , 2,1 , 2,2]]

    # check column to see if there a win
    for i in range(len(board)):
        if board[0][i] == play and board[1][i] == play and board[2][i] == play:
            return True


def check_first_dig(board, play):
    # [[0,0 , 0,1 , 0,2],
    #  [1,0 , 1,1 , 1,2],
    #  [2,0 , 2,1 , 2,2]]

    # check first diagonal to see if there a win
    count = 0
    for i in range(len(board)):
        if board[i][i] == play:
            count += 1

    if count == 3:
        return True


def check_second_dig(board, play):
    # [[0,0 , 0,1 , 0,2],
    #  [1,0 , 1,1 , 1,2],
    #  [2,0 , 2,1 , 2,2]]

    # check second diagonal to see if there a win
    counter = 2
    count = 0
    for i in range(len(board)):
        if board[i][counter] == play:
            count += 1
            counter -= 1

    if count == 3:
        return True


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # winner(board) == X or winner(board) == O -> either X or O wins, game over
    if winner(board) == X or winner(board) == O:
        return True

    # len(actions(board)) == 0 -> there is no actions left , game over
    if len(actions(board)) == 0:
        return True


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


def min_value(board):
    v = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    v = -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # check if board is terminal
    if terminal(board):
        return None

    # maximizing player
    if player(board) == X:
        plays = []
        # loop through each action
        for action in actions(board):
            print(action)
            # add min_value and action that results to this min_value
            plays.append((min_value(result(board, action)), action))

        # get the max min_value with its action
        print(plays)
        temp = max(plays)
        # store the action
        code, action = temp
        # return it
        return action

    # minimizing player
    elif player(board) == O:
        plays = []
        # loop through each action
        for action in actions(board):
            print(action)
            # add max_value and action that results to this max_value
            plays.append((max_value(result(board, action)), action))
        print(plays)
        # get the min max_value with its action
        temp = min(plays)
        print(temp)
        # store the action
        code, action = temp
        # return it
        return action

