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

# Main game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board(window)
        draw_pieces(window, board_state)
        pygame.display.update()

if __name__ == '__main__':
    main()
