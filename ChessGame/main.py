import pygame
print(pygame.__version__)

import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')

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



def draw_board(window):
    colors = [pygame.Color(235, 236, 208), pygame.Color(119, 149, 86)]
    square_size = height // 8

    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(window, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

piece_images = {}

def load_images():
    pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
    for piece in pieces:
        piece_images[f'white_{piece}'] = pygame.image.load(f'images/white_{piece}.png')
        piece_images[f'black_{piece}'] = pygame.image.load(f'images/black_{piece}.png')

load_images()

board_state = [
    ["b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook"],
    ["b_pawn"] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["w_pawn"] * 8,
    ["w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook"]
]

def draw_pieces(window, board):
    square_size = height // 8
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "":
                window.blit(piece_images[piece], pygame.Rect(col * square_size, row * square_size, square_size, square_size))

selected_piece = None
selected_pos = None

def main():
    global selected_piece, selected_pos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // (width // 8)
                row = pos[1] // (height // 8)

                if selected_piece is None:
                    selected_piece = board_state[row][col]
                    selected_pos = (row, col)
                else:
                    if (selected_piece and board_state[row][col] == ""):
                        board_state[row][col] = selected_piece
                        board_state[selected_pos[0]][selected_pos[1]] = ""
                    selected_piece = None
                    selected_pos = None

        draw_board(window)
        draw_pieces(window, board_state)
        pygame.display.update()
