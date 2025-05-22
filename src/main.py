# File: /memory-game/memory-game/src/main.py

import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # Example symbols
    game = Game(symbols)
    game.initialize_board()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(event.pos)
        
        game.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()