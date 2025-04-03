import pygame
import chess
import chess.engine

# Initialize PyGame
pygame.init()

# Load piece images
piece_images = {}
piece_names = ["R", "N", "B", "Q", "K", "P"]
colors = ["w", "b"]

for color in colors:
    for piece in piece_names:
        image = pygame.image.load(f"pieces_png/{color}{piece}.png")  # Ensure you have images in 'pieces/' directory
        piece_images[f"{color}{piece}"] = pygame.transform.scale(image, (60, 60))

# Set up display
WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Colors
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)

# Chessboard setup
board = chess.Board()
selected_square = None

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Highlight previous move
    if board.move_stack:
        last_move = board.peek()  # Get last move without popping it
        from_sq, to_sq = last_move.from_square, last_move.to_square

        from_col, from_row = chess.square_file(from_sq), chess.square_rank(from_sq)
        to_col, to_row = chess.square_file(to_sq), chess.square_rank(to_sq)

        pygame.draw.rect(screen, (253, 253, 150, 150),  # Light blue highlight
                         (from_col * SQUARE_SIZE, (7 - from_row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(screen, (253, 253, 150, 150),  
                         (to_col * SQUARE_SIZE, (7 - to_row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Highlight selected piece
    if selected_square is not None:
        col, row = chess.square_file(selected_square), chess.square_rank(selected_square)
        pygame.draw.rect(screen, (255, 218, 185, 150),  # Yellow for selected piece
                         (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

        # Highlight legal moves
        for move in board.legal_moves:
            if move.from_square == selected_square:
                target_col, target_row = chess.square_file(move.to_square), chess.square_rank(move.to_square)
                pygame.draw.circle(screen, (0, 255, 0, 100),  # Green dots for valid moves
                                   (target_col * SQUARE_SIZE + SQUARE_SIZE // 2, 
                                    (7 - target_row) * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            color = "w" if piece.color == chess.WHITE else "b"
            piece_type = piece.symbol().upper()
            img = piece_images.get(f"{color}{piece_type}")
            if img:
                col, row = chess.square_file(square), chess.square_rank(square)
                screen.blit(img, (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE))

def handle_click(pos):
    global selected_square
    col, row = pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE
    square = chess.square(col, 7 - row)
    
    if selected_square is None:
        if board.piece_at(square) and board.piece_at(square).color == board.turn:
            selected_square = square
    else:
        move = chess.Move(selected_square, square)
        if move in board.legal_moves:
            board.push(move)
        selected_square = None

def main():
    running = True
    while running:
        draw_board()
        draw_pieces()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())

    pygame.quit()

if __name__ == "__main__":
    main()
