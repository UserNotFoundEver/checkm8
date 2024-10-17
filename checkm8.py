import chess
import random

# Initialize the chess board
board = chess.Board()

def display_board():
    print(board)

def player_move():
    move = input("Enter your move (e.g., e2 e4): ").replace(" ", "")
    
    try:
        # Validate and execute the player's move in UCI format (e.g., e2e4)
        if chess.Move.from_uci(move) in board.legal_moves:
            board.push_uci(move)
        else:
            print("Illegal move. Try again.")
    except ValueError:
        print("Invalid move format. Please use format like 'e2 e4'.")

def ai_move():
    legal_moves = list(board.legal_moves)
    if legal_moves:
        move = random.choice(legal_moves)
        board.push(move)
        try:
            # This line formats the move in SAN notation, but only if it's valid
            print(f"AI played {board.san(move)}.")
        except AssertionError as e:
            print(f"Error formatting AI move: {e}")
    else:
        print("No legal moves available for AI.")

def game_loop():
    print("Welcome to Chess!")
    display_board()

    while not board.is_game_over():
        player_move()  # Player makes a move
        display_board()  # Show updated board

        if board.is_game_over():  # Check if the game is over after player's move
            break

        ai_move()  # AI makes a move
        display_board()  # Show updated board after AI's move

    print("Game over!")
    print(board.result())  # Show the result of the game

if __name__ == "__main__":
    game_loop()
