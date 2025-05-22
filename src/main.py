import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    symbols = ['A', 'B', 'C', 'D', 'E', 'F']  # Example symbols
    game = Game(screen, symbols)
    game.initialize_board()
    font = pygame.font.SysFont(None, 72)
    celebration_shown = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game.is_game_won():
                game.handle_click(event.pos)
        
        game.draw()
        if game.is_game_won():
            if not celebration_shown:
                # Draw celebration message
                text = font.render("You Win!", True, (255, 215, 0))
                text_rect = text.get_rect(center=(400, 300))
                screen.blit(text, text_rect)
                celebration_shown = True
            else:
                # Keep showing the message
                text = font.render("You Win!", True, (255, 215, 0))
                text_rect = text.get_rect(center=(400, 300))
                screen.blit(text, text_rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()