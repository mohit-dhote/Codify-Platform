def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {player_turn}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {player_turn}, enter column (0, 1, or 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = player_turn

        if check_winner(board, player_turn):
            print_board(board)
            print(f"Player {player_turn} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player_turn = "O" if player_turn == "X" else "X"

if __name__ == "__main__":
    main()
