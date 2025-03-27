import time
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
        [10, 15, 20, 30, 30, 20, 15, 10],
        [5, 10, 15, 25, 25, 15, 10, 5],
        [0, 0, 10, 20, 20, 10, 0, 0],
        [5, -5, -10, 5, 5, -10, -5, 5],
        [5, 10, 10, -20, -20, 10, 10, 5],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ],
    'N': [  # White Knight
        [-50, -40, -30, -30, -30, -30, -40, -50],
        [-40, -20, 0, 5, 5, 0, -20, -40],
        [-30, 5, 20, 20, 20, 20, 5, -30],
        [-30, 10, 20, 25, 25, 20, 10, -30],
        [-30, 5, 20, 25, 25, 20, 5, -30],
        [-30, 0, 10, 20, 20, 10, 0, -30],
        [-40, -20, 0, 5, 5, 0, -20, -40],
        [-50, -40, -30, -30, -30, -30, -40, -50]
    ],
    'B': [  # White Bishop
        [-20, -10, -10, -10, -10, -10, -10, -20],
        [-10, 5, 0, 0, 0, 0, 5, -10],
        [-10, 10, 10, 10, 10, 10, 10, -10],
        [-10, 5, 10, 15, 15, 10, 5, -10],
        [-10, 0, 10, 15, 15, 10, 0, -10],
        [-10, 5, 10, 10, 10, 10, 5, -10],
        [-10, 0, 0, 0, 0, 0, 0, -10],
        [-20, -10, -10, -10, -10, -10, -10, -20]
    ],
    'R': [  # White Rook
        [0, 0, 5, 10, 10, 5, 0, 0],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [-5, 0, 0, 5, 5, 0, 0, -5],
        [5, 10, 10, 10, 10, 10, 10, 5],
        [0, 0, 5, 10, 10, 5, 0, 0]
    ],
    'Q': [  # White Queen
        [-20, -10, -10, -5, -5, -10, -10, -20],
        [-10, 0, 5, 0, 0, 0, 0, -10],
        [-10, 0, 5, 5, 5, 5, 0, -10],
        [-5, 0, 5, 5, 5, 5, 0, -5],
        [-5, 0, 5, 5, 5, 5, 0, -5],
        [-10, 5, 5, 5, 5, 5, 0, -10],
        [-10, 0, 5, 0, 0, 0, 0, -10],
        [-20, -10, -10, -5, -5, -10, -10, -20]
    ],
    'K': [  # White King (Middle Game)
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
def order_moves(board):
    moves = list(board.legal_moves)
    opponent = not board.turn

    def move_score(move):
        score = 0
        is_capture = board.is_capture(move)
        victim_value = 0
        attacker_value = 0
        
        # Check captures using MVV-LVA before pushing the move
        if is_capture:
            victim = board.piece_at(move.to_square)
            attacker = board.piece_at(move.from_square)
            victim_value = PIECE_VALUES.get(victim.symbol(), 0) if victim else 0
            attacker_value = PIECE_VALUES.get(attacker.symbol(), 0) if attacker else 0
            score += (victim_value - attacker_value)
        
        board.push(move)
        # Check for checkmate (highest priority)
        if board.is_checkmate():
            board.pop()
            return float('inf')
        # Check if move gives check
        if board.is_check():
            score += 1000
        # Check castling
        if board.is_castling(move):
            score += 300
        # Check if moved piece is attacked by the original opponent
        if board.is_attacked_by(opponent, move.to_square):
            moved_piece = board.piece_at(move.to_square)
            if moved_piece:
                penalty = PIECE_VALUES.get(moved_piece.symbol().upper(), 0) * 0.5
                score -= penalty
        # Penalize hanging captures
        if is_capture and board.is_attacked_by(opponent, move.to_square):
            score -= attacker_value  # Attacker_value from before push
        board.pop()
        return score

    return sorted(moves, key=move_score, reverse=True)

def evaluate_mobility(board):
    original_turn = board.turn
    try:
        # White's mobility
        board.turn = chess.WHITE
        white_moves = board.legal_moves.count()
        # Black's mobility
        board.turn = chess.BLACK
        black_moves = board.legal_moves.count()
    finally:
        board.turn = original_turn
    return 15 * (white_moves - black_moves)

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
            symbol = piece.symbol().upper()
            value = PIECE_VALUES.get(symbol, 0)
            if piece.color == chess.BLACK:
                value = -value
            # Add piece-square table value (customize tables)
            row = chess.square_rank(square)
            col = chess.square_file(square)
            if piece.color == chess.BLACK:
                row = 7 - row
            # Example for pawns (modify with actual table)
            if symbol == 'P':
                value += (row - 2) * 10  # Encourage advancing pawns
            score += value
    score += evaluate_mobility(board)
    score += evaluate_king_safety(board)
    score += evaluate_pawn_structure(board)
    return score

def quiescence_search(board, alpha, beta, depth=3):
    stand_pat = evaluate_board(board)
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat
    if depth == 0:
        return alpha

    for move in order_moves(board):
        if not (board.is_capture(move) or board.gives_check(move)):
            continue
        board.push(move)
        score = -quiescence_search(board, -beta, -alpha, depth-1)
        board.pop()
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    return alpha

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return quiescence_search(board, alpha, beta, depth=2)  # Shallow quiescence

    moves = order_moves(board)
    if not moves:
        return evaluate_board(board)
    
    if maximizing:
        max_eval = -float('inf')
        for move in moves:
            board.push(move)
            eval_val = minimax(board, depth-1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval_val)
            alpha = max(alpha, eval_val)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in moves:
            board.push(move)
            eval_val = minimax(board, depth-1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval_val)
            beta = min(beta, eval_val)
            if beta <= alpha:
                break
        return min_eval

def best_move(board,depth,max_time=4):
    start_time = time.time()
    best_move = None
    best_score = -float('inf')
    depth = 1
    while time.time() - start_time < max_time:
        for move in order_moves(board):
            if time.time() - start_time >= max_time:
                break
            board.push(move)
            current_score = minimax(board, depth-1, -float('inf'), float('inf'), False)
            board.pop()
            if current_score > best_score:
                best_score = current_score
                best_move = move
        depth += 1
    return best_move if best_move else next(iter(board.legal_moves))























def interactive_game_with_white_suggestion():
    board = chess.Board()
    player_side = input("Choose your side (W/B): ").strip().upper()
    is_player_white = (player_side == "W")
    move_count = 0
    
    while not board.is_game_over():
        print("\nCurrent Board:\n")
        if  board.turn == chess.WHITE:
            print(board)
        else:
            print(board.transform(chess.flip_horizontal).transform(chess.flip_vertical)) 
        
        suggestion = False
        if (board.turn == chess.WHITE and is_player_white==False) or (board.turn == chess.BLACK and  is_player_white):
            suggestion = best_move(board, depth=3)
            if suggestion:
                print(f"Engine suggests for {'White' if board.turn == chess.WHITE else 'Black'}: {board.san(suggestion)}")
            else:
                print(f"No legal moves available for {'White' if board.turn == chess.WHITE else 'Black'}!")
        
        user_move = input(f"Enter {'White' if board.turn == chess.WHITE else 'Black'}'s move (SAN, e.g., e4, Nf3): ")
        
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

