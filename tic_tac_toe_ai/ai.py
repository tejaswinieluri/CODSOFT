# ai.py
import math

def evaluate(board, ai, human):
    # Check rows, cols, diagonals
    for row in board:
        if row[0] == row[1] == row[2] == ai:
            return 10
        if row[0] == row[1] == row[2] == human:
            return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == ai:
            return 10
        if board[0][col] == board[1][col] == board[2][col] == human:
            return -10

    if board[0][0] == board[1][1] == board[2][2] == ai:
        return 10
    if board[0][0] == board[1][1] == board[2][2] == human:
        return -10

    if board[0][2] == board[1][1] == board[2][0] == ai:
        return 10
    if board[0][2] == board[1][1] == board[2][0] == human:
        return -10

    return 0

def is_moves_left(board):
    return any(" " in row for row in board)

def minimax(board, depth, is_max, ai, human):
    score = evaluate(board, ai, human)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai
                    best = max(best, minimax(board, depth+1, False, ai, human))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = human
                    best = min(best, minimax(board, depth+1, True, ai, human))
                    board[i][j] = " "
        return best

def best_move(board, ai, human):
    best_val = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai
                move_val = minimax(board, 0, False, ai, human)
                board[i][j] = " "
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move
