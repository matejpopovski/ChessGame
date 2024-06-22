import pygame
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

        pygame.display.update()

if __name__ == '__main__':
    main()
