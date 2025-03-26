import chess
import numpy as np

# === Material Values ===
PIECE_VALUES = {
    'P': 100, 'N': 300, 'B': 330, 'R': 500, 'Q': 900, 'K': 20000,
    'p': -100, 'n': -300, 'b': -330, 'r': -500, 'q': -900, 'k': -20000
}

# === Piece-Square Tables ===
PIECE_SQUARE_TABLES = {
    'P': [  # White Pawn
        [0, 0, 0, 0, 0, 0, 0, 0],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [5, 5, 10, 25, 25, 10, 5, 5],
        [0, 0, 0, 20, 20, 0, 0, 0],
        [5, -5, -10, 0, 0, -10, -5, 5],
        [5, 10, 10, -20, -20, 10, 10, 5],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ],
    'N': [  # White Knight
        [-50, -40, -30, -30, -30, -30, -40, -50],
        [-40, -20, 0, 5, 5, 0, -20, -40],
        [-30, 5, 10, 15, 15, 10, 5, -30],
        [-30, 0, 15, 20, 20, 15, 0, -30],
        [-30, 5, 15, 20, 20, 15, 5, -30],
        [-30, 0, 10, 15, 15, 10, 0, -30],
        [-40, -20, 0, 0, 0, 0, -20, -40],
        [-50, -40, -30, -30, -30, -30, -40, -50]
    ],
    'B': [  # White Bishop
        [-20, -10, -10, -10, -10, -10, -10, -20],
        [-10, 5, 0, 0, 0, 0, 5, -10],
        [-10, 10, 10, 10, 10, 10, 10, -10],
        [-10, 0, 10, 10, 10, 10, 0, -10],
        [-10, 5, 5, 10, 10, 5, 5, -10],
        [-10, 0, 5, 10, 10, 5, 0, -10],
        [-10, 0, 0, 0, 0, 0, 0, -10],
        [-20, -10, -10, -10, -10, -10, -10, -20]
    ],
    'R': [  # White Rook
        [0, 0, 0, 5, 5, 0, 0, 0],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [5, 10, 10, 10, 10, 10, 10, 5],
        [0, 0, 0, 5, 5, 0, 0, 0]
    ],
    'Q': [  # White Queen
        [-20, -10, -10, -5, -5, -10, -10, -20],
        [-10, 0, 0, 0, 0, 0, 0, -10],
        [-10, 0, 5, 5, 5, 5, 0, -10],
        [-5, 0, 5, 5, 5, 5, 0, -5],
        [0, 0, 5, 5, 5, 5, 0, -5],
        [-10, 5, 5, 5, 5, 5, 0, -10],
        [-10, 0, 5, 0, 0, 0, 0, -10],
        [-20, -10, -10, -5, -5, -10, -10, -20]
    ],
    'K': [  # White King (middle game)
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-20, -30, -30, -40, -40, -30, -30, -20],
        [-10, -20, -20, -20, -20, -20, -20, -10],
        [20, 20, 0, 0, 0, 0, 20, 20],
        [20, 30, 10, 0, 0, 10, 30, 20]
    ]
}

# For black pieces, flip the white tables vertically.
for piece in ['P', 'N', 'B', 'R', 'Q', 'K']:
    PIECE_SQUARE_TABLES[piece.lower()] = PIECE_SQUARE_TABLES[piece][::-1]

# === Additional Heuristic Functions ===

def evaluate_mobility(board):
    """
    Evaluate mobility as the difference in the number of legal moves between
    White and Black, weighted by a factor.
    """
    board_white = board.copy()
    board_white.turn = chess.WHITE
    white_moves = board_white.legal_moves.count()

    board_black = board.copy()
    board_black.turn = chess.BLACK
    black_moves = board_black.legal_moves.count()

    return 10 * (white_moves - black_moves)

def evaluate_king_safety(board):
    """
    A basic king safety evaluation that penalizes a king in the center and 
    rewards positions that suggest castling (i.e. king not on its initial square).
    """
    safety_score = 0
    center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]

    white_king_sq = board.king(chess.WHITE)
    black_king_sq = board.king(chess.BLACK)

    if white_king_sq in center_squares:
        safety_score -= 30
    if black_king_sq in center_squares:
        safety_score += 30

    if not board.has_castling_rights(chess.WHITE) and white_king_sq != chess.E1:
        safety_score += 20
    if not board.has_castling_rights(chess.BLACK) and black_king_sq != chess.E8:
        safety_score -= 20

    return safety_score

def evaluate_pawn_structure(board):
    """
    Evaluate pawn structure by penalizing doubled and isolated pawns.
    """
    pawn_score = 0
    white_pawns = board.pieces(chess.PAWN, chess.WHITE)
    black_pawns = board.pieces(chess.PAWN, chess.BLACK)

    def doubled_penalty(pawns):
        files = {}
        for sq in pawns:
            file = chess.square_file(sq)
            files[file] = files.get(file, 0) + 1
        penalty = 0
        for count in files.values():
            if count > 1:
                penalty += (count - 1) * 15
        return penalty

    def isolated_penalty(pawns):
        penalty = 0
        for sq in pawns:
            file = chess.square_file(sq)
            adjacent = [file - 1, file + 1]
            has_adjacent = any(chess.square_file(other) in adjacent for other in pawns)
            if not has_adjacent:
                penalty += 10
        return penalty

    pawn_score -= doubled_penalty(white_pawns)
    pawn_score += doubled_penalty(black_pawns)
    pawn_score -= isolated_penalty(white_pawns)
    pawn_score += isolated_penalty(black_pawns)

    return pawn_score

# === Combined Evaluation Function ===

def evaluate_board(board):
    """
    Combines material, positional (piece-square tables), mobility, king safety,
    and pawn structure into a single evaluation score. A positive score favors White.
    """
    score = 0
    # Convert board string to a 2D array (8x8)
    board_2d = np.array(str(board).split()).reshape(8, 8)
    for i in range(8):
        for j in range(8):
            piece = board_2d[i][j]
            if piece != '.':
                piece_val = PIECE_VALUES.get(piece, 0)
                table = PIECE_SQUARE_TABLES.get(piece, None)
                if table:
                    pos_val = table[i][j]
                    piece_val += pos_val
                score += piece_val

    score += evaluate_mobility(board)
    score += evaluate_king_safety(board)
    score += evaluate_pawn_structure(board)
    return score

# === Minimax with Alpha-Beta Pruning ===

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing:
        max_eval = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval_value = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval_value = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            if beta <= alpha:
                break
        return min_eval

def best_move(board, depth=3):
    best_val = -float("inf")
    best_mv = None
    for move in board.legal_moves:
        board.push(move)
        move_val = minimax(board, depth - 1, -float("inf"), float("inf"), False)
        board.pop()
        if move_val > best_val:
            best_val = move_val
            best_mv = move
    return best_mv

# === Interactive Game: Input Moves for Both Colors, with Suggestion for White ===

def interactive_game_with_white_suggestion():
    """
    In this interactive mode, the program takes input from both White and Black.
    - On White's turn, it first displays the best move suggestion (using the engine) but
      does not update the board with it.
    - You then enter White's move manually (using standard algebraic notation).
    - On Black's turn, you enter the move normally.
    The board updates only when you input a move.
    """
    board = chess.Board()
    move_count = 0

    while not board.is_game_over():
        print("\nCurrent Board:\n")
        print(board, "\n")

        if board.turn == chess.WHITE:
            suggestion = best_move(board, depth=3)
            if suggestion:
                print("Engine suggests for White: ", board.san(suggestion))
            else:
                print("No legal moves available for White!")
            user_move = input("Enter White's move (SAN, e.g., e4, Nf3): ")
        else:
            user_move = input("Enter Black's move (SAN, e.g., e5, Nc6): ")

        try:
            move = board.parse_san(user_move)
            if move in board.legal_moves:
                board.push(move)
                move_count += 1
            else:
                print("Illegal move. Please try again.")
        except Exception as e:
            print("Invalid move notation. Please try again.")

    print("Game over after", move_count, "moves. Result:", board.result())

if __name__ == "__main__":
    interactive_game_with_white_suggestion()
