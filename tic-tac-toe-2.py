import sys
import random

# Empty cell
EMPTY = "-"

# Player symbols
PLAYER_X = "X"
PLAYER_O = "O"

# Winning combinations
WINNING_COMBINATIONS = [
    # Rows
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # Columns
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # Diagonals
    [0, 4, 8],
    [2, 4, 6]
]


def print_board(board):
    """Prints the current state of the board."""
    for i in range(3):
        for j in range(3):
            print(board[i * 3 + j], end=" ")
        print()


def evaluate(board):
    """Evaluates the current state of the board using a heuristic evaluation function."""
    score = 0

    # Check rows and columns
    for combination in WINNING_COMBINATIONS:
        [a, b, c] = combination
        line = [board[a], board[b], board[c]]
        if line.count(PLAYER_X) == 3:
            score += 100  # Player X wins
        elif line.count(PLAYER_O) == 3:
            score -= 100  # Player O wins
        elif line.count(PLAYER_X) == 2 and line.count(EMPTY) == 1:
            score += 10  # Player X has two in a row
        elif line.count(PLAYER_O) == 2 and line.count(EMPTY) == 1:
            score -= 10  # Player O has two in a row

    # Check diagonals
    if board[0] == board[4] == board[8] == PLAYER_X:
        score += 100  # Player X wins
    elif board[0] == board[4] == board[8] == PLAYER_O:
        score -= 100  # Player O wins
    elif board[2] == board[4] == board[6] == PLAYER_X:
        score += 100  # Player X wins
    elif board[2] == board[4] == board[6] == PLAYER_O:
        score -= 100  # Player O wins

    return score


def minimax(board, depth, maximizing_player):
    """Minimax algorithm implementation with heuristic evaluation."""
    score = evaluate(board)

    if score != 0:
        return score

    if maximizing_player:
        best_score = -sys.maxsize
        for i in range(len(board)):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = sys.maxsize
        for i in range(len(board)):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    """Finds the best move for the AI player using the minimax algorithm."""
    best_score = -sys.maxsize
    best_move = None

    for i in range(len(board)):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            score = minimax(board, 0, False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# Empty Board
board = [EMPTY] * 9

# AI easy Win
board = ['X', EMPTY, 'X', 'O', EMPTY, EMPTY, 'O', 'O', 'X']
# 
# Player Win
board = ['O', EMPTY, EMPTY, EMPTY, 'X', EMPTY, 'X', EMPTY, 'O']

# # Draw
board = ['X', 'O', 'X', EMPTY, EMPTY, 'O', 'O', 'X', 'O']

# # AI Decision to Win
board = ['X', EMPTY, 'X', 'O', EMPTY, EMPTY, 'O', EMPTY, EMPTY]

# # AI Decision to Block Player's Winning Move
board = [EMPTY, EMPTY, 'X', 'X', 'O', EMPTY, EMPTY, EMPTY, EMPTY]

while True:
    print_board(board)

    # Player's move
    move = int(input("Enter your move (0-8): "))
    if board[move] != EMPTY or move < 0 or move > 8:
        print("Invalid move!")
        continue
    board[move] = PLAYER_O
    
    # # # Random Generator's move
    valid_moves = [i for i in range(9) if board[i] == EMPTY]
    if not valid_moves:
        print("No valid moves left. It's a draw!")
        break
    random_move = random.choice(valid_moves)
    print("Random Generator's move:", random_move)
    board[random_move] = PLAYER_O

    # Check game result
    result = evaluate(board)
    if result >= 100:
        print_board(board)
        print("Player X wins!")
        break
    elif result <= -100:
        print_board(board)
        print("Player O wins!")
        break
    elif EMPTY not in board:
        print_board(board)
        print("It's a draw!")
        break

    # AI's move
    print("AI's move:")
    best_move = find_best_move(board)
    board[best_move] = PLAYER_X

    # Check game result
    result = evaluate(board)
    if result >= 100:
        print_board(board)
        print("Player X wins!")
        break