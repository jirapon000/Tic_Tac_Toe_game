# -----------------------------
# TIC-TAC-TOE (Console Version)
# -----------------------------

def print_board(board):
    print("\n")
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("___|___|___")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("___|___|___")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("   |   |")
    print("\n")


def check_win(board, mark):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(board[i] == board[j] == board[k] == mark for i, j, k in win_combos)


def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)


def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] not in ['X', 'O']:
                return move
            else:
                print("That space is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")


def play_game():
    board = [str(i+1) for i in range(9)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!\n")
    print_board(board)

    while True:
        move = get_move(board, current_player)
        board[move] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()
