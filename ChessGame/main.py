import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')

# Load images
piece_images = {}
current_dir = os.path.dirname(os.path.abspath(__file__))

def load_images():
    pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
    for piece in pieces:
        try:
            white_piece_path = os.path.join(current_dir, f'images/white_{piece}.png')
            black_piece_path = os.path.join(current_dir, f'images/black_{piece}.png')
            print(f'Loading {white_piece_path}')
            print(f'Loading {black_piece_path}')
            piece_images[f'white_{piece}'] = pygame.image.load(white_piece_path)
            piece_images[f'black_{piece}'] = pygame.image.load(black_piece_path)
        except FileNotFoundError as e:
            print(e)
            pygame.quit()
            sys.exit()

load_images()

# Draw board function
def draw_board(window):
    colors = [pygame.Color(235, 236, 208), pygame.Color(119, 149, 86)]
    square_size = height // 8

    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(window, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

# Initial board state
board_state = [
    ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight", "black_rook"],
    ["black_pawn"] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["white_pawn"] * 8,
    ["white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight", "white_rook"]
]

# Draw pieces function
def draw_pieces(window, board):
    square_size = height // 8
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "":
                window.blit(piece_images[piece], pygame.Rect(col * square_size, row * square_size, square_size, square_size))

# Check if the move is valid
def is_valid_move(piece, start_pos, end_pos, board):
    start_col, start_row = start_pos
    end_col, end_row = end_pos
    piece_color = piece.split('_')[0]
    piece_type = piece.split('_')[1]
    
    if start_pos == end_pos:
        return False

    if board[end_row][end_col] != "" and board[end_row][end_col].split('_')[0] == piece_color:
        return False

    if piece_type == 'pawn':
        direction = 1 if piece_color == 'white' else -1
        if start_col == end_col:
            if board[end_row][end_col] == "" and (end_row - start_row == direction):
                return True
            if start_row == (6 if piece_color == 'white' else 1) and board[end_row][end_col] == "" and (end_row - start_row == 2 * direction):
                return True
        if abs(start_col - end_col) == 1 and end_row - start_row == direction and board[end_row][end_col] != "" and board[end_row][end_col].split('_')[0] != piece_color:
            return True

    elif piece_type == 'rook':
        if start_row == end_row or start_col == end_col:
            if not any(board[r][c] != "" for r in range(min(start_row, end_row) + 1, max(start_row, end_row)) for c in range(min(start_col, end_col) + 1, max(start_col, end_col))):
                return True

    elif piece_type == 'knight':
        if (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2):
            return True

    elif piece_type == 'bishop':
        if abs(start_row - end_row) == abs(start_col - end_col):
            if not any(board[start_row + i * (1 if end_row > start_row else -1)][start_col + i * (1 if end_col > start_col else -1)] != "" for i in range(1, abs(start_row - end_row))):
                return True

    elif piece_type == 'queen':
        if start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(start_col - end_col):
            if not any(board[start_row + i * (1 if end_row > start_row else -1)][start_col + i * (1 if end_col > start_col else -1)] != "" for i in range(1, abs(start_row - end_row) if abs(start_row - end_row) == abs(start_col - end_col) else max(abs(start_row - end_row), abs(start_col - end_col)))):
                return True

    elif piece_type == 'king':
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            return True

    return False

# Move piece function
def move_piece(board, start_pos, end_pos):
    piece = board[start_pos[1]][start_pos[0]]
    board[start_pos[1]][start_pos[0]] = ""
    board[end_pos[1]][end_pos[0]] = piece

# Main game loop
def main():
    selected_piece = None
    selected_square = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // (width // 8)
                row = pos[1] // (height // 8)
                if selected_piece:
                    if is_valid_move(board_state[selected_piece[1]][selected_piece[0]], selected_piece, (col, row), board_state):
                        move_piece(board_state, selected_piece, (col, row))
                    selected_piece = None
                else:
                    if board_state[row][col] != "":
                        selected_piece = (col, row)

        draw_board(window)
        draw_pieces(window, board_state)
        pygame.display.update()

if __name__ == '__main__':
    main()
