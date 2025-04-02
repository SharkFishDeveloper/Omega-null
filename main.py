import multiprocessing
import time
import chess
import numpy as np
import chess.polyglot
from openings import best_opening_move
PIECE_VALUES = {
    'P': 100, 'N': 300, 'B': 330, 'R': 500, 'Q': 900, 'K': 20000,
    'p': -100, 'n': -300, 'b': -330, 'r': -500, 'q': -900, 'k': -20000
}
PIECE_SQUARE_TABLES = {
    'P': np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [10, 15, 20, 30, 30, 20, 15, 10],
        [5, 10, 15, 25, 25, 15, 10, 5],
        [0, 0, 10, 20, 20, 10, 0, 0],
        [5, -5, -10, 5, 5, -10, -5, 5],
        [5, 10, 10, -20, -20, 10, 10, 5],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]),
    'N': np.array([
        [-50, -40, -30, -30, -30, -30, -40, -50],
        [-40, -20, 0, 5, 5, 0, -20, -40],
        [-30, 5, 20, 20, 20, 20, 5, -30],
        [-30, 10, 20, 25, 25, 20, 10, -30],
        [-30, 5, 20, 25, 25, 20, 5, -30],
        [-30, 0, 10, 20, 20, 10, 0, -30],
        [-40, -20, 0, 5, 5, 0, -20, -40],
        [-50, -40, -30, -30, -30, -30, -40, -50]
    ]),
    'B': np.array([
        [-20, -10, -10, -10, -10, -10, -10, -20],
        [-10, 5, 0, 0, 0, 0, 5, -10],
        [-10, 10, 10, 10, 10, 10, 10, -10],
        [-10, 5, 10, 15, 15, 10, 5, -10],
        [-10, 0, 10, 15, 15, 10, 0, -10],
        [-10, 5, 10, 10, 10, 10, 5, -10],
        [-10, 0, 0, 0, 0, 0, 0, -10],
        [-20, -10, -10, -10, -10, -10, -10, -20]
    ]),
    'R': np.array([
        [0, 0, 5, 10, 10, 5, 0, 0],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [5, 10, 10, 10, 10, 10, 10, 5],
        [0, 0, 5, 10, 10, 5, 0, 0]
    ]),
    'Q': np.array([
        [-20, -10, -10, -5, -5, -10, -10, -20],
        [-10, 0, 5, 0, 0, 0, 0, -10],
        [-10, 0, 5, 5, 5, 5, 0, -10],
        [-5, 0, 5, 5, 5, 5, 0, -5],
        [-5, 0, 5, 5, 5, 5, 0, -5],
        [-10, 5, 5, 5, 5, 5, 0, -10],
        [-10, 0, 5, 0, 0, 0, 0, -10],
        [-20, -10, -10, -5, -5, -10, -10, -20]
    ]),
    'K': np.array([
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-30, -40, -40, -50, -50, -40, -40, -30],
        [-20, -30, -30, -40, -40, -30, -30, -20],
        [-10, -20, -20, -20, -20, -20, -20, -10],
        [20, 20, 0, 0, 0, 0, 20, 20],
        [20, 30, 10, 0, 0, 10, 30, 20]
    ])
}

for piece in ['P', 'N', 'B', 'R', 'Q', 'K']:
    PIECE_SQUARE_TABLES[piece.lower()] = PIECE_SQUARE_TABLES[piece][::-1]



killer_moves = {}
history_heuristic = {}    

def static_exchange_evaluation(board, square):
    """
    Evaluates whether capturing a piece at 'square' results in a material gain or loss.
    Uses a naive Static Exchange Evaluation (SEE) method.
    """
    victim = board.piece_at(square)
    if not victim:
        return 0  # No piece to capture

    victim_value = PIECE_VALUES.get(victim.symbol(), 0)
    attackers = sorted(board.attackers(board.turn, square), key=lambda sq: PIECE_VALUES.get(board.piece_at(sq).symbol(), float('inf')))
    defenders = list(board.attackers(not board.turn, square))

    if not attackers:
        return 0  # No way to capture

    attacker = attackers[0]
    attacker_value = PIECE_VALUES.get(board.piece_at(attacker).symbol(), 0)

    if abs(attacker_value) < abs(victim_value):
        return victim_value - attacker_value  # Winning trade
    elif len(defenders) >= len(attackers):
        return -attacker_value  # Losing trade
    else:
        return 0  # Neutral trade


def is_hanging(board, square):
    """
    Checks if a piece on the given square is hanging (undefended and can be captured).
    """
    piece = board.piece_at(square)
    if not piece:
        return False  # No piece to check

    attackers = board.attackers(not board.turn, square)
    defenders = board.attackers(board.turn, square)

    return len(defenders) == 0 and len(attackers) > 0  # Undefended but attacked


def is_blunder(board, move):
    """
    Checks if a move leaves the piece hanging or results in a significant material loss.
    """
    board.push(move)
    moved_piece = board.piece_at(move.to_square)

    if moved_piece and is_hanging(board, move.to_square):
        board.pop()
        return True  # Moved piece is now hanging

    # Use ordered moves for better trade assessment
    ordered_moves = sorted(board.legal_moves, key=lambda m: static_exchange_evaluation(board, m.to_square), reverse=True)
    
    material_loss = static_exchange_evaluation(board, move.to_square)
    board.pop()

    return material_loss < 0  # If negative, move results in a net material loss

def order_moves(board):
    """
    Orders moves based on Static Exchange Evaluation (SEE).
    Prioritizes captures and favorable trades.
    """
    moves = list(board.legal_moves)
    return sorted(
        moves,
        key=lambda move: static_exchange_evaluation(board, move.to_square),
        reverse=True  # Higher SEE values first (better trades)
    )

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

    return 12* (white_moves - black_moves)

def evaluate_king_safety(board):
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

def evaluate_board(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            score += PIECE_VALUES.get(piece.symbol(), 0)

    score += evaluate_mobility(board)
    score += evaluate_king_safety(board)
    score += evaluate_pawn_structure(board)
    return score

transposition_table = {}

def minimax(board, depth, alpha, beta, maximizing):
    key = (chess.polyglot.zobrist_hash(board), depth, maximizing)

    if key in transposition_table:
        return transposition_table[key]
    
    if depth == 0 or board.is_game_over():
        eval_score = evaluate_board(board)
        transposition_table[key] = eval_score
        return eval_score

    moves = order_moves(board)
    moves[:10]
    if maximizing:
        max_eval = -float("inf")
        for move in moves:
            board.push(move)
            eval_value = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            if beta <= alpha:
                break
        transposition_table[key] = max_eval
        return max_eval
    else:
        min_eval = float("inf")
        for move in moves:
            board.push(move)
            eval_value = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            if beta <= alpha:
                break
        transposition_table[key] = min_eval
        return min_eval

def best_move(board, depth):
    """Finds the best move using parallelized minimax."""
    best_mv = None
    best_val = -float("inf")

    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None

    board_fen = board.fen()  # Store board state for multiprocessing

    # Multiprocessing for first layer of minimax
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        move_values = pool.map(
            minimax_worker, 
            [(move, board_fen, depth - 1, -float("inf"), float("inf"), False) for move in legal_moves]
        )

    for i, move in enumerate(legal_moves):
        if move_values[i] > best_val:
            best_val = move_values[i]
            best_mv = move

    return best_mv

def minimax_worker(args):
    """Helper function for multiprocessing minimax."""
    move, board_fen, depth, alpha, beta, is_maximizing = args
    board = chess.Board(board_fen)
    board.push(move)
    return minimax(board, depth, alpha, beta, is_maximizing)

def interactive_game_with_white_suggestion():
    mode = input("Start with FEN position or normal play? (f/n): ").strip()
    if mode == "f":
        fen = input("Enter FEN position: ").strip()
        try:
            board = chess.Board(fen)
        except ValueError:
            print("Invalid FEN. Using default starting position.")
            board = chess.Board()
    else:
        board = chess.Board()

    player_side = input("Choose your side (W/B): ").strip().upper()
    is_player_white = (player_side == "W")
    move_count = 0

    while not board.is_game_over():
        print("\nCurrent Board:\n")
        print(board.transform(chess.flip_horizontal).transform(chess.flip_vertical)) 
        
        if (board.turn == chess.WHITE and is_player_white) or (board.turn == chess.BLACK and not is_player_white):
            # Player's turn
            user_move = input(f"Enter move for {'White' if board.turn == chess.WHITE else 'Black'} (SAN format, e.g., e4, Nf3): ")
        else:
            # AI's turn
            suggestion = None
            if move_count < 5:  # Use opening moves for first 5 moves
                suggestion = best_opening_move(board)
            
            if not suggestion:  # If no opening move available, use engine
                start_time = time.time()
                suggestion = best_move(board, depth=4)
                elapsed = time.time() - start_time
                print(f"\nEngine calculation time: {elapsed:.2f}s")
            
            if suggestion:
                print(f"AI plays: {board.san(suggestion)}")
                user_move = board.san(suggestion)
            else:
                print(f"No legal moves available for {'White' if board.turn == chess.WHITE else 'Black'}!")
                break
        
        try:
            move = board.parse_san(user_move)
            if move in board.legal_moves:
                board.push(move)
                move_count += 1
            else:
                print("Illegal move. Please try again.")
        except Exception:
            print("Invalid move notation. Please try again.")

    print("Game over after", move_count, "moves. Result:", board.result())

if __name__ == "__main__":
    interactive_game_with_white_suggestion()