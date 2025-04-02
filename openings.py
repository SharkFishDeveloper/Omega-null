import chess
import random
from openingBook import OPENING_BOOK 

def best_opening_move(board: chess.Board):
    fen = board.fen()
    if fen in OPENING_BOOK:
        move_uci = random.choice(OPENING_BOOK[fen])  # Get UCI move string
        return chess.Move.from_uci(move_uci)  # Convert to Move object
    return None