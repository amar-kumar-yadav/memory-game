def shuffle_cards(symbols):
    import random
    random.shuffle(symbols)
    return symbols

def generate_symbols(num_pairs):
    symbols = [f'Symbol {i}' for i in range(num_pairs)]
    return symbols * 2  # Create pairs of symbols

def create_game_board(num_pairs):
    symbols = generate_symbols(num_pairs)
    shuffled_symbols = shuffle_cards(symbols)
    return shuffled_symbols