# tic_tac_toe.py
from ai import best_move

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    return any(" " in row for row in board)

def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"

    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)

    while is_moves_left(board) and not check_winner(board):
        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = human
        else:
            print("Invalid move, try again.")
            continue

        print_board(board)

        if check_winner(board) or not is_moves_left(board):
            break

        # AI move
        move = best_move(board, ai, human)
        board[move[0]][move[1]] = ai
        print("AI played:")
        print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
