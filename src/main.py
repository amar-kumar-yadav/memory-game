import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # Example symbols
    game = Game(screen, symbols)  # Pass screen to Game
    game.initialize_board()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(event.pos)
        
        game.draw()  # draw() no longer needs screen as argument
        pygame.display.flip()

if __name__ == "__main__":
    main()