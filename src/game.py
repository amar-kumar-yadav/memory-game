import pygame

class Game:
    def __init__(self, symbols):
        self.symbols = symbols
        self.cards = self.initialize_board()
        self.flipped_cards = []
        self.matched_pairs = 0

    def initialize_board(self):
        import random
        deck = self.symbols * 2  # Each symbol appears twice
        random.shuffle(deck)
        return deck

    def flip_card(self, index):
        if index not in self.flipped_cards:
            self.flipped_cards.append(index)
            return self.cards[index]
        return None

    def check_match(self):
        if len(self.flipped_cards) == 2:
            first_card = self.flipped_cards[0]
            second_card = self.flipped_cards[1]
            if self.cards[first_card] == self.cards[second_card]:
                self.matched_pairs += 1
                return True
            else:
                return False
        return None

    def reset_flipped_cards(self):
        self.flipped_cards = []

    def is_game_won(self):
        return self.matched_pairs == len(self.symbols)

    def draw(self, screen):
        CARD_WIDTH = 100
        CARD_HEIGHT = 150
        PADDING = 20
        ROWS = 4
        COLS = 4

        screen.fill((30, 30, 30))
        font = pygame.font.SysFont(None, 72)

        for i, symbol in enumerate(self.cards):
            row = i // COLS
            col = i % COLS
            x = PADDING + col * (CARD_WIDTH + PADDING)
            y = PADDING + row * (CARD_HEIGHT + PADDING)
            rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

            if i in self.flipped_cards:
                pygame.draw.rect(screen, (200, 200, 200), rect)
                text = font.render(str(symbol), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, (70, 130, 180), rect)
                
    def handle_click(self, pos):
        CARD_WIDTH = 100
        CARD_HEIGHT = 150
        PADDING = 20
        ROWS = 4
        COLS = 4

        x, y = pos
        for i in range(len(self.cards)):
            row = i // COLS
            col = i % COLS
            rect_x = PADDING + col * (CARD_WIDTH + PADDING)
            rect_y = PADDING + row * (CARD_HEIGHT + PADDING)
            rect = pygame.Rect(rect_x, rect_y, CARD_WIDTH, CARD_HEIGHT)
            if rect.collidepoint(x, y):
                if i not in self.flipped_cards and len(self.flipped_cards) < 2:
                    self.flip_card(i)
                # Check for match after flipping two cards
                if len(self.flipped_cards) == 2:
                    pygame.time.wait(500)
                    if not self.check_match():
                        self.reset_flipped_cards()
                break